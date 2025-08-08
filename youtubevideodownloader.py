#!/usr/bin/env python3.9

import yt_dlp
youtube = yt_dlp.YoutubeDL({'extractor_args': {'youtube': {'player_client': ['web']}}})
youtube.verbose = False

def search(string_search, num):
    global youtube
    videos = []
    info = youtube.extract_info('ytsearch{0}:{1}'.format(num,string_search), download=False)
    for video in info['entries']:
        videos.append({'title': video['title'], 'thumbnail': video['thumbnail'],  'description': video['description'], 'view_count': video['view_count'], 'channel': video['channel'], 'id': video['id']})
    return videos

info = search("pope leo xiv", 10)
print(info)
