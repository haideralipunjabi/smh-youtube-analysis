import os
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import json

mask = np.array(Image.open("mask.png"))
data = json.load(open("wordcount.json","r"))


wc = WordCloud(width=3888,height=5180, background_color="white", max_words=6000,mask=mask,max_font_size=1000, random_state=32)

wc.generate_from_frequencies(data)
wc.to_file("cloud.png")