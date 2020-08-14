import pullred
import dredvid
import movie
import uptube
import os
import sys

top100 = pullred.pullredall()
dredvid.downloadvideos(top100)
movie.makemovie(top100)

upopts = {'file' : os.getcwd() + os.path.sep + 'mymovie.mp4', 
        'title' : "Today's top posts",
        'description' : "Please enjoy today's top trending posts!",
        'keywords' : "top, posts, today, daily",
        'category' : "22",
        'privacyStatus' : "private"
        }

uptube.upload(upopts)