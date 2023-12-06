import os
from pytube import Playlist
from colorama import Fore, init
init(autoreset=True)

os.system("clear")
print(Fore.BLUE + "--------------------------------------------------------")
print(Fore.CYAN+'''
__   _______  ______ _             _ _     _    ______                    _                 _           
\ \ / /_   _| | ___ \ |           | (_)   | |   |  _  \                  | |               | |          
 \ V /  | |   | |_/ / | __ _ _   _| |_ ___| |_  | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \ /   | |   |  __/| |/ _` | | | | | / __| __| | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | |   | |   | |   | | (_| | |_| | | \__ \ |_  | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/   \_/   \_|   |_|\__,_|\__, |_|_|___/\__| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                              __/ |                                                                     
                             |___/                                                                      
      ''')
print("Created by:", Fore.GREEN + "Rajkishor Patra")
print("-------------------------------------------------------------------")

def make_alpha_numeric(string):
    return ''.join(char for char in string if char.isalnum())

link = input(Fore.YELLOW+ "Enter YouTube Playlist URL: ")

yt_playlist = Playlist(link)

# Modify the storage path for Termux
storage_path = "/data/data/com.termux/files/home/storage/downloads/playlist"

folderName = make_alpha_numeric(yt_playlist.title)
os.makedirs(os.path.join(storage_path, folderName), exist_ok=True)

totalVideoCount = len(yt_playlist.videos)
print(Fore.CYAN +"Total videos in playlist: 🎦", str(totalVideoCount))

for index, video in enumerate(yt_playlist.videos, start=1):
    print(Fore.MAGENTA+"Downloading:-", video.title)

    # Get the video stream with audio, starting from 720p and falling back
    video_stream = video.streams.filter(file_extension="mp4", resolution="720p").first()
    if not video_stream:
        video_stream = video.streams.filter(file_extension="mp4", resolution="480p").first()
    if not video_stream:
        video_stream = video.streams.filter(file_extension="mp4", resolution="360p").first()

    # Download the selected stream
    video_size = video_stream.filesize
    print(Fore.LIGHTGREEN_EX+"Size:", video_size // (1024 ** 2), "🗜 MB")
    video_stream.download(output_path=os.path.join(storage_path, folderName))
    print("Downloaded:", video.title, "✨ successfully!")
    print(Fore.YELLOW+"Remaining Videos:", totalVideoCount - index)

print(Fore.LIGHTBLUE_EX+ "All videos downloaded successfully! 🎉")
