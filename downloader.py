from pytube import YouTube
import os
from colorama import Fore, init
init(autoreset=True)
import sys

total_videos = 0
downloaded_videos = 0

def banner():
    clear_screen()
    print(Fore.BLUE + '''
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╭╯╰╯┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
-------------------------------------------
Author -Rajkishor Patra
GitHub -imrj569
------------------------------------------- 
    ''')
    print(Fore.YELLOW + '''This script is download all youtube videos in 720p 
if not available in 720p it try 480p/360p''')
    print(Fore.CYAN + "Please wait a sec fetching all urls...")

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def download_video(url, output_path):
    global total_videos, downloaded_videos

    total_videos += 1

    yt = YouTube(url)

    stream = yt.streams.filter(progressive=True, resolution="720p").filter(only_audio=False).first()

    # Try to find a 720p video with audio
    if not stream:
        stream = yt.streams.filter(progressive=True, resolution="480p").filter(only_audio=False).first()

    # If no 480p video found, try 360p
    elif not stream:
        stream = yt.streams.filter(progressive=True, resolution="360p").filter(only_audio=False).first()

    # Download the stream
    if stream:
        video_title = f"Please wait downloading-{stream.title} in {stream.resolution}"
        print(Fore.YELLOW + video_title)
        stream.download(output_path)
        print(Fore.GREEN + "Download Completed✅")
        downloaded_videos += 1
    else:
        failed_info = f"Couldn't find video in 480p or 360p with audio."
        print(Fore.RED + failed_info)

def delete_first_line(filename):
    with open(filename, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate(0)
        f.writelines(lines[1:])

if __name__ == "__main__":
    banner()
    try:
        # Example usage
        with open("urls.txt", "r") as f:
            links = f.readlines()

        if len(links) == 0:
            print(Fore.RED + "There are no urls available in urls.txt")
            sys.exit()

        print(f"Total videos: {total_videos}")

        for link in links:
            video_url = link.strip()

            if os.name == "nt":
                output_path = "videos"
            else:
                output_path = "/data/data/com.termux/files/home/storage/downloads/YT_Downloader"

            download_video(video_url, output_path)
            delete_first_line("urls.txt")

        print(f"Downloaded videos: {downloaded_videos}")

        if downloaded_videos == total_videos:
            print(Fore.GREEN + "All videos downloaded✅")

    except:
        sys.exit()
