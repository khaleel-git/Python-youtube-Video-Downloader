import json
import sys
import os
from pytube import YouTube
import ffmpeg
from pathlib import Path

url = sys.argv[1]
itag = sys.argv[2]

yt = YouTube(url)
stream = yt.streams

# download() function documentation ->
# download(output_path: Optional[str] = None, filename: Optional[str] = None, 
# filename_prefix: Optional[str] = None, skip_existing: bool = True, 
# timeout: Optional[int] = None, max_retries: Optional[int] = 0)

if(itag != '22'): 
	# First Download Audio at bit-rate @
	title = yt.title.replace(" ", "_")
	title_audio = title + "_audio_only.webm"
	dl = yt.streams.get_by_itag(251) # itag = 251 is for audio @160 kbps
	dl.download('videos', title_audio)
	# Now Download mp4 Just Video without audio
	title = yt.title.replace(" ", "_")
	title_video = title + "_video_only.mp4"
	dl = yt.streams.get_by_itag(itag) # Download video only 
	dl.download('videos', title_video)
	# Combine mp4 video & webm audio -> .mp4 (final video)
	video_path = Path("/home/apkfuel/public_html/yt/videos/" + title + ".mp4")
	# print(video_path)
	if (video_path.is_file()):
		# print(title + ".mp4 already exists.")
		# print("Download Link is: https://apkfuel.com/yt/videos/" + title + ".mp4")
		sys.exit()
	else:
		from subprocess import *
		p = Popen(['/usr/bin/php','/home/apkfuel/public_html/yt/ffmpeg.php',title],stdout=PIPE)
		print (p.stdout.read())

else: # audio & video -> 720p
	title = yt.title.replace(" ", "_")
	# title = title + ".mp4"
	dl = yt.streams.get_by_itag(22)
	dl.download('videos', title)

print("Download link: https://apkfuel.com/yt/videos/" + title + ".mp4")