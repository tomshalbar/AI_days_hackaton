import tweepy

api_key = "Y3tVqGSLUdEvCuYuJ5m7NIoAt" #Your API/Consumer key 
api_key_secret = "HcMo1Utle3m95IzKJNXn9qSpuNaGCCh17f5lUFSKCviwii9VY3" #Your API/Consumer Secret Key
access_token = "1810424105482784768-0vRw1I8Er2dKuJogCNFz3mybKyJA3o" #Your Access token key
access_token_secret = "IUID4xcIq9aZG06XNr6lggsmhffO1TRcvk7ki1Vm3dRNI" #Your Access token Secret key

# filtered data will be used to generate posts

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def post_tweet(content):
    try:
        api.update_status(content)
        print("posted tweet")
    except tweepy.errors.TweepyException as error:
        print(f"Error posting tweet: {error}")

post_tweet("Hello this is a test post")
