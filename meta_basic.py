import json
import sys
from pytube import YouTube

url = sys.argv[1]

yt = YouTube(url)
title = yt.title.replace(" ", "_")
stream = yt.streams

video = yt.streams.order_by('resolution').desc()

basic_dict = {'title': title, 'description': '', 'thumbnail': yt.thumbnail_url }
# print(yt.thumbnail_url)
# print(title)
print(basic_dict)

# print(len(video))