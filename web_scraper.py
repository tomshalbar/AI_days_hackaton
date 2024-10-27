from ntscraper import Nitter
import json

scraper = Nitter(log_level = 1, skip_instance_check = False);

fema_tweets = scraper.get_tweets("FEMA", mode = 'user', number = 20)

data = {
    "user": [],
    "text": [],
    "date": []
}

for tweet in fema_tweets['tweets']:

    data["user"].append(tweet["user"]),
    data["text"].append(tweet["text"]),
    data["date"].append(tweet["date"]),

with open("twitterRawData.json", "w") as outfile:
    json.dump(data, outfile)


