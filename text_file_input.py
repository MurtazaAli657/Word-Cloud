import sys
import os
from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory where it is.
currdir = os.path.dirname('__file__')

# get path of text file
dataset = open("new.txt", "r").read()

def create_wordcloud(text):
    # create numpy araay for wordcloud mask image getting from same working directory
    mask = np.array(Image.open(path.join(currdir, "cloud.png")))

    # create set of stopwords. it is used for don't use "is, are, was, were etc" this type of words
    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color="white",
                    max_words=2000, 
                    mask=mask,
                    stopwords=stopwords)
    
    # generate wordcloud
    wc.generate(text)

    # save wordcloud image in same working directory
    wc.to_file(path.join(currdir, "wc.png"))

    #run the program
create_wordcloud(dataset)
