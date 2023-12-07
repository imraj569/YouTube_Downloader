import os
from pytube import Playlist
from colorama import Fore, init
init(autoreset=True)
from time import sleep

def main():   
    clear_screen()
    print(Fore.BLUE + "--------------------------------------------------------")
    print(Fore.MAGENTA+'''
    ╔══╗
    ╚╗╔╝
    ╔╝(¯`v´¯)
    ╚══`.¸.[YT Playlist Downloader]
    ''')
    print("Created by:", Fore.GREEN + "Rajkishor Patra")
    print(Fore.GREEN+"Github-imraj569")
    print("-------------------------------------------------------------------")

    def make_alpha_numeric(string):
        return ''.join(char for char in string if char.isalnum())

    link = input(Fore.YELLOW+ "Enter YouTube Playlist URL🔗: ")
    clear_screen()
    print(Fore.BLUE+'''
     ~
    ~
  .---.
  `---'=.
  |RP | |
  |   |='
  `---'
          ''')
    print("Take a coffe i will do all work for you ☺️🐈")
    sleep(1)
    yt_playlist = Playlist(link)

    if os.name == "nt":
        storage_path = "YT_Playlist"

    # Modify the storage path for Termux
    storage_path = "/data/data/com.termux/files/home/storage/downloads/playlist"

    folderName = make_alpha_numeric(yt_playlist.title)
    os.makedirs(os.path.join(storage_path, folderName), exist_ok=True)

    totalVideoCount = len(yt_playlist.videos)
    print(Fore.CYAN +"Total videos in playlist: 🎦", str(totalVideoCount))

    for index, video in enumerate(yt_playlist.videos, start=1):
        clear_screen()
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

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    main