import pandas as pd
import numpy as np
import re



def clean_data(path):
    df = pd.read_csv(path) #encoding = "ISO-8859-1")
    text = df['text']

    replace = []

    url_replace = r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?'
    url_replace_2 = r'(http|ftp|https)s*:*(\/)*\w*'
    # unicode_replace = r'\\xe2\\\w{3}\\\w{3}'
    unicode_replace = r'\\x\S+\\x\S{2}'
    tag_replace = r'@\w+:?'
    escape_char_replace = r'\\[^x]'
    start_replace = r'"*[b|B]\W'
    retweet_replace = r'RT\b'

    replace.append(url_replace)
    replace.append(url_replace_2)
    replace.append(unicode_replace)
    replace.append(tag_replace)
    replace.append(escape_char_replace)
    replace.append(start_replace)
    replace.append(retweet_replace)

    for replace_regex in replace:
        df = df.replace(to_replace=replace_regex, value='', regex=True)

    output_path = path[:-4] + "_clean.csv"
    df.to_csv(output_path)

def main():
    path = "CNN_tweets.csv"
    clean_data(path)

if __name__ == "__main__":
    main()
