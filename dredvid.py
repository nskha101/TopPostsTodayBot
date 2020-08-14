from __future__ import unicode_literals

import youtube_dl
import sys
import re
import os
from datetime import date

date = date.today()
date = str(date)

if not os.path.exists(date):
    os.makedirs(re.sub('[?/:]', '', date))

def downloadvideos(dict):
    urls = dict['url']
    titles = dict['title']
    
    for index, url in enumerate(urls, start=0):
        temp_list = [urls[index]]
        print('downloading for ' + titles[index])

        ydl_opts = {
                    'cookiefile': 'cookies.txt',
                    'force_generic_extractor': True,
                    'sleep_interval': 10,
                    'retries': 10,
                    'outtmpl' :  os.getcwd() + os.path.sep + date + os.path.sep + titles[index] +'.%(ext)s',                
                    'allsubtitles': True,
                    'verbose': False,
                    'quiet': True,
                    'writesubtitles': True,
                    'no_warnings': True
                }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(temp_list)
                print('\033[92m[Done \u2713]\033[0m')
        except Exception as e:
            print('\033[91m[Fail]\033[0m' 'Name: '+ titles[index])
            pass      
    removeallpng()

def removeallpng():
    dir_name = os.getcwd() + os.path.sep + date
    test = os.listdir(dir_name)
    for item in test:
        if not(item.endswith(".mp4")):
            os.remove(os.path.join(dir_name, item))
        