import argparse

from twitter_wordcloud.get_tweets import get_tweets
from twitter_wordcloud.data_cleaning import clean_data
from twitter_wordcloud.make_wordcloud import make_wordcloud

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', type=str, help='Twitter Handle')
    # "--" makes the argument optional
    parser.add_argument('-n', '--num_tweets',
                        type=int,
                        default=100000,
                        help='Number of tweets you want to download, default \
                                will download max tweets allowed by twitter')

    args = parser.parse_args()

    csv_path = get_tweets(args.username, args.num_tweets)
    clean_path = clean_data(csv_path)
    make_wordcloud(clean_path)

if __name__=='__main__':
    main()
