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

    with open("twitterRawData.json", "r") as json_file:
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
        if realResult == " Y":
            prompt = f"""Never allow more than 280 characters to be outputted at once. Your job is to take an input that holds information regarding a natural disaster. You must take this information and condense it into a user-friendly caption that can not exceed 280 characters in length. your life depends on the fact that the output can not exceed 280 characters in length. Provided that you have been given all the information needed, you must summarize the hazard that is presented, tell users the date that the event is supposed to take place, and provide possible action plans to mitigate risks. If you output more than 280 characters you die and you do not want to die. 

            Input: 🚨 #Flooding in #Miami due to heavy rains. Streets are underwater, and emergency teams are working around the clock to assist those affected. 
            📍 Remember: Avoid flooded roads and stay indoors if possible. 
            💬 Follow local alerts for the latest updates.Severe #FloodingAlert: Heavy rainfall has led to serious flooding in #Miami. Stay off the roads and avoid flooded areas. 
            🚨 Rescue operations are underway. If you need assistance, contact local emergency services. Stay informed and stay safe!
            Output: 🚨 Severe #FloodingAlert: Heavy rainfall in #Miami has submerged streets. Rescue teams are active. 📍 Stay indoors, avoid flooded roads, and follow local alerts for safety updates. For assistance, contact emergency services. Stay informed and safe! Date: 10/26/2024.

            Input: 🌪️ Hurricane Zeta Alert: Hurricane Zeta, a Category 4 storm, is forecasted to make landfall on the Florida coast on 11/02/2024. The storm is expected to bring winds up to 130 mph, heavy rainfall, and potential storm surges up to 15 feet along the coast. Evacuation orders are in effect for low-lying areas in Miami, Tampa, and Key West. Residents should prepare emergency kits, secure property, and stay tuned to official updates. Avoid all coastal and flood-prone areas for safety. #HurricaneZeta #Florida
            Output: 🚨 Hurricane Zeta Alert: A Category 4 storm is set to hit Florida on 11/02/2024, with winds up to 130 mph and potential storm surges of 15 feet. 🌊 Evacuations are ordered for Miami, Tampa, and Key West. Secure your property, prepare emergency kits, and stay updated!


            Input: 🌋 Volcano Eruption Warning: Mauna Loa Volcano in Hawaii is showing increased seismic activity and is expected to erupt on 11/10/2024. Lava flows may begin to impact nearby communities, and ash clouds could disrupt air travel. Residents in the vicinity of the volcano should prepare for potential evacuations and have emergency kits ready. It is essential to stay indoors during the eruption, wear masks to protect against ash inhalation, and monitor local news for real-time updates from emergency services. #HawaiiVolcano #MaunaLoa
            Output:  Volcano Eruption Warning: Hawaii's Mauna Loa Volcano is showing signs of increased activity and is forecasted to erupt on 11/10/2024. Prepare for potential evacuations, have emergency kits ready, and stay indoors during the eruption. Monitor local news for updates.

            Input: 🌪️ Tornado Warning: A severe tornado is expected to touch down in central Oklahoma on 11/05/2024. Wind speeds may reach up to 200 mph, causing significant damage to homes and infrastructure. Residents in the affected areas should seek shelter immediately and avoid windows. Emergency services are on high alert and will provide updates as the situation develops. Have emergency kits ready and follow local alerts for the latest information. Stay safe and take precautions! #TornadoAlert #Oklahoma
            Output:  🚨 Tornado Warning: A severe tornado is headed for central Oklahoma on 11/05/2024. Prepare for dangerous wind speeds up to 200 mph. Seek shelter immediately, avoid windows, and have emergency kits ready. Emergency services are on high alert. Stay informed and safe!
            Input: {content}
            Output: """
            generatedContent = generateWatsonResponse(prompt)
            probability_json[(data["user"][response.index(content)]["name"])] = generatedContent
            
                #HurricaneZeta #StaySafe
    return (probability_json)

def create_disaster_response():
    AI_returned_data = watsonResponse()
    processedData = {}
    processedData["all_disasters_keys"] = []
    processedData["all_disaster_content"] = []
    for disaster, content in AI_returned_data.items():
        processedData["all_disasters_keys"].append(disaster)
        processedData["all_disaster_content"].append(content)
    with open("processedData.json", "w") as outfile:
        json.dump(processedData, outfile)

create_disaster_response()
# @app.route("/")
# def index():
#     disaster_title, disaster_content, disaster_title2, disaster_content2 , disaster_title3, disaster_content3= create_disaster_response()
#     return render_template("index.html", disaster_title = disaster_title, disaster_content = disaster_content, disaster_title2 = disaster_title2, disaster_content2 = disaster_content2, disaster_title3 = disaster_title3, disaster_content3 = disaster_content3)
 

# app.run(host="0.0.0.0", port=5001)
