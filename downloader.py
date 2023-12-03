'''
------------------------------------------------------------------------------------
This script is for downloading youtube videos from a text file name urls
you just have to past all urls you want to download in urls.txt then run the script 
it will try to download all videos in 720p if not available in try 480p or 360p.
------------------------------------------------------------------------------------
⚠️Do not past youtube playlist urls 
if you want to download youtube whole playlist use
git@github.com:imraj569/YT_Playlist_Downloader.git 
------------------------------------------------------------------------------------
'''
import pytube
import os
from colorama import Fore,init
init(autoreset=True)
from time import sleep

def Banner():
    screen_clear()
    print(Fore.CYAN+'''
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╱┃┃┃┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╭╯╰╯┃╰╯┣╮╭╮╭┫┃┃┃╰┫╰╯┃╭╮┃╰╯┃┃━┫┃
╱╱╰╯╱╱╱╰╯╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
-------------------------------------------
Author - Rajkishor Patra
Ig - @im.raj.569
-------------------------------------------
          ''')

    sleep(1)
    print(Fore.RED+"Fatching all YouTube Urls please wait a sec...")

def screen_clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def download_videos():
    Banner()
    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    total_videos = len(urls)
    if total_videos == 0:
        screen_clear()
        print(Fore.RED+"No urls available please add urls first then try agin...")
        sleep(1)

    downloaded_videos = 0
    errors = 0
 
    for url in urls:
        try:
            yt = pytube.YouTube(url)
            # Try to download the highest resolution video (720p)
            video = yt.streams.get_by_resolution("720p")

            if not video:
                # If 720p is not available, try 480p
                video = yt.streams.get_by_resolution("480p")

            if not video:
                # If 480p is not available, download 360p with audio
                video = yt.streams.filter(progressive=True, file_extension="mp4").first()

            video_size = os.path.getsize(video.default_filename)
            remaining_videos = total_videos - downloaded_videos - errors
            video_details = f"Downloading video {downloaded_videos + 1}/{total_videos} ({remaining_videos} videos remaining) - {video.title} ({video_size} bytes)"
            print(Fore.GREEN+video_details)

            video.download()

            # Create the 'Youtube_Videos' folder if it doesn't exist
            if not os.path.exists('Youtube_Videos'):
                os.makedirs('Youtube_Videos')

            # Move the downloaded video to the 'Youtube_Videos' folder
            os.rename(video.default_filename, os.path.join('Youtube_Videos', video.default_filename))

            # Remove the downloaded URL from the 'urls.txt' file
            with open('urls.txt', 'r') as f_in, open('temp_urls.txt', 'w') as f_out:
                for line in f_in:
                    if line != url:
                        f_out.write(line)

            os.rename('temp_urls.txt', 'urls.txt')

            downloaded_videos += 1
        except Exception as e:
            errors += 1
            error_details = f"Error downloading video {downloaded_videos + 1}: {e}"
            print(Fore.RED+error_details)

if __name__ == '__main__':
    download_videos()
