import json 
import requests
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from flask import Flask

app = Flask(__name__)


def watsonResponse():
    """accessing the Watson dataBase and retrieving a generated response"""


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
        "max_new_tokens": 100
    }
    )


    #generate responses.
    response = data["response"]
    probability_json = {}
    for content in response:
        disaster = content["title"]
        prompt = f"How likely is {disaster} to be a natural disaster case?. Please give the answer, as just one number, in the form of a probability."
        probability_json[disaster] = (model.generate_text(prompt))
    return (probability_json)



@app.route("/")
def index():
    return watsonResponse()

app.run(host="0.0.0.0", port=5001)

