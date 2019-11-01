# Python program to generate WordCloud

# importing all necessery modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

path = "CNN_tweets_clean.csv"

df = pd.read_csv(path)

comment_words = ' '
stopwords = set(STOPWORDS)

#iterate through the csv file
for val in df.text:

    # typecaste each val to string
    val = str(val)

    # split the value
    tokens = val.split()

    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

    for words in tokens:
        comment_words = comment_words + words + ' '


wordcloud = WordCloud(width = 800, height = 800,
                min_font_size = 10,
                random_state = 42,
                background_color ='black',
                stopwords = stopwords).generate(comment_words)
# print(wordcloud.words_)
# plot the WordCloud image
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

#plt.show()
img_path = path[:-10] + ".png"
wordcloud.to_file(img_path)
