import tweepy

api_key = #Your API/Consumer key 
api_key_secret = #Your API/Consumer Secret Key
access_token = #Your Access token key
access_token_secret = #Your Access token Secret key

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
