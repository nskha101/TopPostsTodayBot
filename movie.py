from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from datetime import date

from datetime import date

date = date.today()
date = str(date)


def makemovie(reddict):

    urls = reddict['url']
    titles = reddict['title']
    file_list = os.listdir(os.getcwd() + os.path.sep + date)
    videoclips = []
    for file in file_list:
        clip = VideoFileClip(os.getcwd() + os.path.sep +
                             date + os.path.sep + file)
        if (clip.duration < 30):
            videoclips.append(clip)
        else:
            videoclips.append(clip.subclip(0, 30))

    final_clip = concatenate_videoclips(videoclips,
                               method='compose')
    final_clip.write_videofile('mymovie.mp4')
