import json
import sys
from pytube import YouTube

url = sys.argv[1]

yt = YouTube(url)
title = yt.title.replace(" ", "_")
stream = yt.streams

video = yt.streams.order_by('resolution').desc()
# print(yt.thumbnail_url)
# print(video)


# print(len(video))

final_list = []

# meta_dict = {'title': yt.title, 'thumbnail': yt.thumbnail_url}
# final_list.append(meta_dict)

for j in range(0,len(video)):

    detail = str(video[j])

    lines = detail.split(' ')
    # print(len(lines))

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
# json_string = json.dumps(final_list, indent=4)
json_string = json.dumps(final_list)
json_string_postman = json.dumps(final_list, indent=4)
# print(json_string_postman)
print(json_string)
# with open('/home/apkfuel/public_html/yt/json/' + title + '.json', 'w') as f:
#     json.dump(json_string, f)
with open('/home/apkfuel/public_html/yt/json/' + title + '.json', 'w') as f:
    json.dump(final_list,f, indent=4)
	 # # f.write(json_string)
	 # json.dump(json_string, f, ensure_ascii=False, indent=4)

# print("https://apkfuel.com/yt/json/" + title + ".json")

# with open("user_content/apk_json/" + appIds_array[i] + '.json', 'w', encoding='utf-8') as f:
#                         json.dump(details, f, ensure_ascii=False, indent=4)

# print("https://apkfuel.com/yt/json/" + title + ".json")
