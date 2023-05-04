#   vid02.py
#   python vid02.py
#   https://codeby.net/threads/rabota-s-videofajlami-s-pomoschju-python.80169/
#   Работа с видеофайлами
#   Python Moviepy длительность видео




import os.path

import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


get_length(v01.mp4)