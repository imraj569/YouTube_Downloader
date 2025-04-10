import os
import sys
import subprocess
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def banner():
    clear_screen()
    print(Fore.BLUE + '''
╭╮╱╱╭┳━━━━╮╭━━━╮╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮
┃╰╮╭╯┃╭╮╭╮┃╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱┃┃
╰╮╰╯╭┻╯┃┃╰╯╱┃┃┃┣━━┳╮╭╮╭┳━╮┃┃╭━━┳━━┳━╯┣━━┳━╮
╱╰╮╭╯╱╱┃┃╱╱╭╯╰╯┃╭╮┃╰╯╰╯┃╭╮┫┃┃╭╮┃╭╮┃╭╮┃┃━┫╭╯
╱╱┃┃╱╱╱┃┃╱╱╰━━━┻━━╯╰╯╰╯╰╯╰┻━┻━━┻╯╰┻━━┻━━┻╯
-------------------------------------------
Author - Rajkishor Patra
GitHub - imrj569
-------------------------------------------
    ''')
    print(Fore.YELLOW + "This script downloads a YouTube video with the following resolution preference:")
    print(Fore.YELLOW + "720p (if available), then 480p, then 360p (all with audio).\n")

def get_output_path():
    # For Windows/macOS/Linux use the "videos" folder in the current directory,
    # For Termux adjust accordingly.
    if os.name == "nt" or os.name == "posix":
        path = os.path.join(os.getcwd(), "videos")
    else:
        path = "/data/data/com.termux/files/home/storage/downloads/YT_Downloader"
    os.makedirs(path, exist_ok=True)
    return path

def build_command(url, resolution):
    # Build a yt-dlp command with resolution fallback.
    # The command tries the preferred resolution stream with best audio.
    # If not available, it falls back to a lower resolution.
    if resolution == "720p":
        fmt = "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif resolution == "480p":
        fmt = "bestvideo[height<=480]+bestaudio/best[height<=480]"
    elif resolution == "360p":
        fmt = "bestvideo[height<=360]+bestaudio/best[height<=360]"
    else:
        fmt = "bestvideo+bestaudio/best"
    command = [
        "yt-dlp",
        "--no-warnings",
        "--quiet",
        "--no-progress",
        "-f", fmt,
        "--merge-output-format", "mp4",
        "-o", os.path.join(get_output_path(), "%(title)s.%(ext)s"),
        url
    ]
    return command

def download_video(url):
    # Try 720p first; if that fails, try 480p; then 360p.
    for res in ["720p", "480p", "360p"]:
        print(Fore.CYAN + f"Trying to download in {res}...")
        cmd = build_command(url, res)
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(Fore.GREEN + f"Download in {res} succeeded.\n")
            return
        else:
            print(Fore.RED + f"Download in {res} failed; trying lower resolution...\n")
    print(Fore.RED + "All resolution downloads failed for this URL.")

def process_urls_file(file_path):
    if not os.path.isfile(file_path):
        print(Fore.RED + f"'{file_path}' not found.")
        sys.exit(1)
    with open(file_path, "r") as f:
        links = [line.strip() for line in f if line.strip()]
    if not links:
        print(Fore.RED + "No URLs found in the file!")
        sys.exit(1)
    for url in links:
        download_video(url)
    print(Fore.GREEN + "All videos from the file have been downloaded.")

if __name__ == "__main__":
    banner()
    output_path = get_output_path()
    print(Fore.CYAN + f"Videos will be saved in: {output_path}\n")
    print(Fore.BLUE + "Choose input option:")
    print(Fore.GREEN + "1. Enter a single YouTube video URL")
    print(Fore.YELLOW + "2. Read URLs from 'urls.txt'")
    choice = input(Fore.CYAN + "Enter choice (1 or 2): ").strip()

    if choice == "1":
        video_url = input(Fore.YELLOW + "\nEnter YouTube video URL: ").strip()
        if video_url:
            download_video(video_url)
        else:
            print(Fore.RED + "No URL provided. Exiting.")
    elif choice == "2":
        process_urls_file("urls.txt")
    else:
        print(Fore.RED + "Invalid choice. Exiting.")
