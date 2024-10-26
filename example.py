from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

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

prompt = 'How far is Paris from Bangalore?'
print(model.generate(prompt))
print(model.generate_text(prompt))