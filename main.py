import watsonInteraction
import web_scraper
import time

while True:
    web_scraper.lookThroughWeb()
    watsonInteraction.create_disaster_response()
    time.sleep(300)


