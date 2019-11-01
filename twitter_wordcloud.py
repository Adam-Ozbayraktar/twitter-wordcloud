import argparse

#from twitter_wordcloud.get_tweets import get_tweets

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', type=str, help='Twitter Handle')
    # "--" makes the argument optional
    parser.add_argument('--num_tweets', type=int,
                        help='Number of tweets you want to download, default \
                                will download max tweets allowed by twitter')

    args = parser.parse_args()

    #print(args.username)

    #print(args.num_tweets) # None

    
if __name__=='__main__':
    main()
