# vid.py
#   https://codeby.net/threads/rabota-s-videofajlami-s-pomoschju-python.80169/
#   Работа с видеофайлами
#   Python Moviepy длительность видео



import os.path
import time
from numpy import arange

from colorama import Fore
from colorama import init
from moviepy.editor import


import subprocess

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)


    if os.path.exists(path_directory):
        print(Fore.CYAN + '[+] Сканирование директории')
        clip_in_dir = os.listdir(path_directory)
        clip_to_merge = []
        for clip in clip_in_dir:
            if clip.endswith(".mp4") or clip.endswith(".avi"):
                VideoFileClip(os.path.join(path_directory, clip))
                clip_to_merge.append(VideoFileClip(os.path.join(path_directory, clip)))


if len(clip_to_merge) <= 1:
            print(Fore.RED + '[-] В указанной директории нечего объединять')
            main()
            return
        else:
            print(Fore.YELLOW + f'[+] Найдено фалов: {len(clip_to_merge)}')
            merge_final = concatenate_videoclips(clip_to_merge)
            print(Fore.YELLOW + f'[+] Длительность объединяемого видео: '
                  f'{time.strftime("%H:%M:%S", time.gmtime(merge_final.duration))}\n[+] Начинаю объединение файлов...\n')
            merge_final.write_videofile(os.path.join(os.getcwd(), f'{res_name}.mp4'))
            print(Fore.GREEN + '\n[+] Объединение файлов завершено')
            print(Fore.GREEN + f'[+] Видео сохранено в папку: "{os.path.join(os.getcwd(), f"{res_name}.mp4")}"')
            main()
            return