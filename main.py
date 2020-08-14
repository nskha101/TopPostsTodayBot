import pullred
import dredvid
import movie
import uptube
import os
import sys

top = pullred.pullredall()
dredvid.downloadvideos(top)
movie.makemovie(top)

upopts = {'file' : os.getcwd() + os.path.sep + 'mymovie.mp4', 
        'title' : "Today's Top Posts",
        'description' : "Please enjoy today's top trending posts!",
        'keywords' : "top, posts, today, daily",
        'category' : "22",
        'privacyStatus' : "private"
        }
input("please review video, then press enter to continue...")
uptube.upload(upopts)