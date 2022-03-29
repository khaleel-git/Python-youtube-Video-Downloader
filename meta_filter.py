import json
import sys
from pytube import YouTube

url = sys.argv[1]

yt = YouTube(url)
stream = yt.streams
title = yt.title.replace(" ", "_")
video = yt.streams.order_by('resolution').desc()
# print(yt.thumbnail_url)
# print(video)


print(len(video))

final_list = []

for j in range(0,len(video)):

    detail = str(video[j])

    lines = detail.split(' ')
    print(len(lines))

    keys = ['0']*8
    values = ['0']*8

    for i in range(1,len(lines)):
        # print(lines[i])
        keys[i-1] = lines[i].split('=')[0]
        values[i-1] = lines[i].split('=')[1].replace('"', '')
    video_dict = dict(zip(keys, values))
    
    # print(video_dict)
    # print('\n')
    final_list.append(video_dict)

# print(final_list)
json_string = json.dumps(final_list, indent=4)
# print(json_string)
with open('/home/apkfuel/public_html/yt/json/' + title + '.json', 'w') as f:
#     json.dump(final_list,indent=4,  f)
	 f.write(json_string)

print("https://apkfuel.com/yt/json/" + title + ".json")