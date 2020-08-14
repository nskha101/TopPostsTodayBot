from __future__ import unicode_literals

import youtube_dl
import sys
import re

def downloadvideos():
    urls = []
    urls.append(url)
    ydl_opts = {
                'cookiefile': 'cookies.txt',
                'force_generic_extractor': True,
                'outtmpl' : re.sub('[?/:]', '', name) + '.%(ext)s',
                'sleep_interval': 10,
                'retries': 10,
                'allsubtitles': True,
                'verbose': False,
                'quiet': True,
                'writesubtitles': True,
                'no_warnings': True,
                'ffmpeg-location': 'C:\\ffmpeg\\bin\\'
            }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
            print('\033[92m[Done \u2713]\033[0m')
    except Exception as e:
        print('\033[91m[Fail]\033[0m')
        pass      