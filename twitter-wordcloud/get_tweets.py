import tweepy
import csv
import os

CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def get_tweets(username):

    for tweet in tweepy.Cursor(api.user_timeline, id=username, tweet_mode='extended', exclude_replies=True, include_rts=False).items():
        tweets_for_csv.append([tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")])

    csv_path = f"{username}_tweets.csv"

    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at", "text"])
        writer.writerows(tweets_for_csv)

def main():
    get_tweets('CNN')

if __name__ == "__main__":
    main()
