import tweepy

API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def fetch_tweets(keyword, count=10):
    try:
        tweets = api.search_tweets(q=keyword, count=count, lang="en")
        return tweets
    except Exception as e:
        print(f"Error fetching tweets: {e}")
        return []

def respond_to_tweets(keyword, response_text):
    tweets = fetch_tweets(keyword)
    for tweet in tweets:
        try:
            print(f"Responding to: {tweet.text}")
            api.update_status(
                status=f"@{tweet.user.screen_name} {response_text}",
                in_reply_to_status_id=tweet.id
            )
        except Exception as e:
            print(f"Error responding to tweet: {e}")

if __name__ == "__main__":
    keyword_to_search = "Python"
    response_message = "Python is awesome! 🚀"
    respond_to_tweets(keyword_to_search, response_message)