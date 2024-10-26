import json 
import requests
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

with open("fake-json-data.json", "r") as json_file:
    data = json.load(json_file)


credentials = Credentials(
    url = "https://us-south.ml.cloud.ibm.com",
    api_key = "kk-R4zCw_li1eSehAixwX3M15OkVpR0dMLt2AAloX57q",
)

client = APIClient(credentials)

model = ModelInference(
  model_id="ibm/granite-13b-chat-v2",
  api_client=client,
  project_id="123a2a50-82f2-4fc8-bd6e-aebd36c91c1b",
  params = {
      "max_new_tokens": 100
  }
)

disaster = data["response"][1]["title"]
print(disaster)
prompt = f"How likely is {disaster} to be a natural disaster case?"
print(model.generate(prompt))
print(model.generate_text(prompt))