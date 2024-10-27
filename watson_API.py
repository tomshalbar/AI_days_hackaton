import json 
import requests
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from flask import Flask, render_template


app = Flask(__name__)


def watsonResponse() -> dict:
    #accessing the Watson dataBase and retrieving a generated response


    #just a practice JSON, update when twitterAPI is up
    with open("fake-json-data.json", "r") as json_file:
        data = json.load(json_file)

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


    #generate responses, and return a JSON
    response = data["response"]
    probability_json = {}
    for content in response:
        disaster = content["title"]
        prompt = prompt_input = f"""You are an environmental science expert, attempting to distinguish between natural disaster and unrelated news. You will be given a title of a news article. Please say if you think the article is about a natural disaster or not. Keep in mind that a natural is an event that was not caused by human error, or by anything related to humans. so a school shooting is not a natural disaster, and a murder is not a natural disaster. Very important: you can repond in only one word!!
        Input: Huge fire in california!
        Output: Yes

        Input: Burning man festival is on its way!
        Output: No
        
        Input: {disaster}
        Output:"""

        watsonNonSene = model.generate_text(prompt)
        realResult = watsonNonSene[:2]
        probability_json[disaster] = (realResult)
    return (probability_json)

def get_watsonResponse():
    AI_returned_data = watsonResponse()
    all_disasters_keys = []
    all_disaster_content = []
    for disaster, content in AI_returned_data.items():
        if content == " y" or content == " Y":
            all_disasters_keys.append(disaster)
            all_disaster_content.append(content)
    return all_disasters_keys[0], all_disaster_content[0], all_disasters_keys[1], all_disaster_content[1], all_disasters_keys[2], all_disaster_content[2]


@app.route("/")
def index():
    disaster_title, disaster_content, disaster_title2, disaster_content2 , disaster_title3, disaster_content3= get_watsonResponse()
    return render_template("index.html", disaster_title = disaster_title, disaster_content = disaster_content, disaster_title2 = disaster_title2, disaster_content2 = disaster_content2, disaster_title3 = disaster_title3, disaster_content3 = disaster_content3)
 

app.run(host="0.0.0.0", port=5001)