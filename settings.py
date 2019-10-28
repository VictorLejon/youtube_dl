# Setting file
PATH = 'C:\\Users\\victorln\\projekt\\python\\youtube_dl'  # IMPORTANT SET PATH

FFMPEG_LOCATION = 'C:\\ffmpeg\\bin'  # Location off ffmpeg's bin folder
FILE_EXTENSION = 'wav'               # File ending, converted by ffmpeg
PREFERRED_QUALITY = '192'            # Audio quality preffered
FILE_NAME = '%(title)s.%(ext)s'      # Name of outputted file, default: "VIDEO_NAME.FILE_EXTENSION"
NEVER_REDOWNLOAD = False             # If True program will never download a file already downloaded
DOWNLOAD_FOLDER = PATH+'\\output'    # Set custom output folder, OBS! Make sure folder has an absolute path
