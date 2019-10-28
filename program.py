from __future__ import unicode_literals
from settings import FFMPEG_LOCATION, FILE_EXTENSION, PREFERRED_QUALITY, FILE_NAME, NEVER_REDOWNLOAD, DOWNLOAD_FOLDER, PATH

import youtube_dl, os, sys


def playlist(x):
    videos = [x]
    ydl_opts = {
        'nooverwrites': True,
        'outtmpl': FILE_NAME,
        'download_archive': '../check.txt',
        'geo-bypass': True,
        'ffmpeg_location': FFMPEG_LOCATION,
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': FILE_EXTENSION,
            'preferredquality': PREFERRED_QUALITY,
        }]
    }
    os.chdir(DOWNLOAD_FOLDER)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(videos)
    if (NEVER_REDOWNLOAD == False):
      open(PATH+'\\check.txt', 'w').close() 
    return


playlist(sys.argv[1])
