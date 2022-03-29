<?php

	$title = $argv[1]; 

	$audio_path = "/home/apkfuel/public_html/yt/videos/$title" . "_audio_only.webm";
	$video_path = "/home/apkfuel/public_html/yt/videos/$title" . "_video_only.mp4";	
	$output_video = "/home/apkfuel/public_html/yt/videos/$title.mp4";

	$ffmpeg = shell_exec("ffmpeg -i '$video_path' -i '$audio_path' -c:v copy -c:a aac '$output_video'");

	unlink($audio_path);
	unlink($video_path);
?>
