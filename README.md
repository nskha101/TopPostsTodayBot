# The Top Posts Today Bot

This bot was created to pull the top ten reddit video posts of the day, compile them into a short video with each clip limited at 30 seconds, and upload it to youtube for consumption anywhere. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To use this software you'll need a few things:
```
acquire a reddit API key for a script application
```
and also
```
a google api Key, located in a json file in the root directory, please refer to the youtube API page for details. 
'''

### Installing

simply download the repository, fill in the praw data line from reddit in the pullredall.py and add the google api client secret json file to the root directory. 

## Running

The program will make a folder with today's date as its name, where it will store the video content that it scrapes from reddit.

Afterwards, it will output the trimmed and edited video as "mymovie.mp4", and upload it to youtube using the parameters in the main.py file. 

##Dependencies

This program has a bunch of dependencies to get it working, alot of which are from the API usage, so be sure to check those carefully in the respective documentation!

Most notably however:
* Moviepy - for editing the videos
* pyttsx3 - for tts implementtion
* youtube_dl - for downloading media


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Other Notes

The uptube.py is a reworked script off of googles example script for uploading using the google API. It now doesn't use arguments, instead it runs off a dictionary of options, and is in python 3.

This project was my attempt at learning proper API usage in a fun way. Hope someone can make use of it!
