import watsonInteraction
import web_scraper
import time

while True:
    watsonInteraction.create_disaster_response()
    web_scraper.lookThroughWeb()
    time.sleep(300)


