import json 
import requests
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from flask import Flask, render_template


app = Flask(__name__)

def generateWatsonResponse(prompt):
    #generating a watson response given a prompt  
    credentials = Credentials(
        url = "https://us-south.ml.cloud.ibm.com",
        api_key = "kk-R4zCw_li1eSehAixwX3M15OkVpR0dMLt2AAloX57q",
    )

    client = APIClient(credentials)
        
    #defining which Watson model to use
    model = ModelInference(
    model_id="ibm/granite-13b-chat-v2",
    api_client=client,
    project_id="123a2a50-82f2-4fc8-bd6e-aebd36c91c1b",
    params = {
        "decoding_method": "sample",
        "max_new_tokens": 200,
        "temperature": 0.33,
        "top_k": 50,
        "top_p": 0.22,
        "repetition_penalty": 1
    }
    )
    return model.generate_text(prompt)


def watsonResponse() -> dict:

    with open("realData.json", "r") as json_file:
        data = json.load(json_file)

    probability_json = {}
    response = data["text"]
    for content in response:
        prompt = f"""You are an environmental science expert, attempting to distinguish between things that are urgent to tell the public, and things that are not as important. You will be given a text notification sent by a news organization. Please say yes if you beleive that it is urgent that the population should be informed about the event that the text points to, or say no if it is not as important. Very important: you can repond in only one word!!
        Input: Huge fire in california!
        Output: Yes

        Input: Burning man festival is on its way!
        Output: No
        
        Input: {content}
        Output:"""

        event_urgency = generateWatsonResponse(prompt)
        realResult = event_urgency[:2]
        probability_json[(data["user"][response.index(content)]["name"])] = realResult
    return (probability_json)
print(watsonResponse())

# def get_watsonResponse():
#     AI_returned_data = watsonResponse()
#     all_disasters_keys = []
#     all_disaster_content = []
#     for disaster, content in AI_returned_data.items():
#         if content == " y" or content == " Y":
#             all_disasters_keys.append(disaster)
#             all_disaster_content.append(content)
#     return all_disasters_keys[0], all_disaster_content[0], all_disasters_keys[1], all_disaster_content[1], all_disasters_keys[2], all_disaster_content[2]


# @app.route("/")
# def index():
#     disaster_title, disaster_content, disaster_title2, disaster_content2 , disaster_title3, disaster_content3= get_watsonResponse()
#     return render_template("index.html", disaster_title = disaster_title, disaster_content = disaster_content, disaster_title2 = disaster_title2, disaster_content2 = disaster_content2, disaster_title3 = disaster_title3, disaster_content3 = disaster_content3)
 

# app.run(host="0.0.0.0", port=5001)
