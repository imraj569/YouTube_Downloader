import os
import subprocess
import json
import platform
from colorama import Fore, Style, init

# Initialize colorama for colored text output.
init(autoreset=True)

# Clear screen function for Windows and Unix-based systems (including Termux)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Clear screen on startup
clear_screen()

# Display banner with your GitHub info.
print(Fore.MAGENTA + '''
    ╔══╗
    ╚╗╔╝
    ╔╝(¯`v´¯)
    ╚══`.¸.[YT Playlist Downloader]
    ''')
print("---------------------------------------------")
print("Created by:", Fore.GREEN + "Rajkishor Patra")
print("Github:", Fore.GREEN + "imraj569")
print(Fore.YELLOW + "Just paste your favorite YouTube playlist URL and it's done ☺️🐈")
print("---------------------------------------------")

# Detect platform and set base path for downloads
if "com.termux" in os.getenv("PREFIX", "") or "Android" in platform.platform():
    base_path = "/data/data/com.termux/files/home/storage/downloads/"
    is_termux = True
else:
    uname = os.getlogin()
    base_path = f"C:\\Users\\{uname}\\Downloads"
    is_termux = False

print(Fore.CYAN + f"📱 Detected platform: {'Termux (Android)' if is_termux else 'Windows'}")
print(Fore.CYAN + f"💾 Download folder set to: {base_path}")

# Ask user for the YouTube playlist URL
playlist_url = input(Fore.YELLOW + "\n🔗 Enter YouTube playlist URL: ").strip()

# Ask for resolution (quality) choice
print(Fore.BLUE + "\n🎞 Choose video quality:")
print(Fore.GREEN + "1. High   = highest available")
print(Fore.YELLOW + "2. Medium = 720p (or lower if not available)")
print(Fore.MAGENTA + "3. Low    = 360p (or lower if not available)")

quality_choice = input(Fore.CYAN + "\nChoose (1/2/3): ").strip()

# Define format string based on user's quality choice:
if quality_choice == "1":
    # High quality: best video and best audio available (fallback to best combined)
    format_string = "bestvideo+bestaudio/best"
    quality_label = "High"
elif quality_choice == "2":
    # Medium quality: 720p preferred. Try to get m4a audio first, then any available audio.
    format_string = ("bestvideo[height<=720]+bestaudio[ext=m4a]/"
                     "bestvideo[height<=720]+bestaudio/best[height<=720]")
    quality_label = "Medium (720p)"
elif quality_choice == "3":
    # Low quality: 360p preferred. Same fallback structure.
    format_string = ("bestvideo[height<=360]+bestaudio[ext=m4a]/"
                     "bestvideo[height<=360]+bestaudio/best[height<=360]")
    quality_label = "Low (360p)"
else:
    print(Fore.RED + "❌ Invalid choice. Exiting.")
    exit(1)

print(Fore.GREEN + f"\n✔ Selected quality: {quality_label}")

# Fetch playlist metadata to retrieve the playlist title (used for folder naming)
print(Fore.BLUE + "\n📂 Fetching playlist metadata...\n")
try:
    result_meta = subprocess.run(
        ["yt-dlp", "--dump-single-json", playlist_url],
        capture_output=True,
        text=True,
        check=True
    )
    playlist_meta = json.loads(result_meta.stdout)
    playlist_title = playlist_meta.get("title", "playlist")
except subprocess.CalledProcessError as e:
    print(Fore.RED + "❌ Failed to fetch playlist metadata.")
    print(e)
    exit(1)

# Sanitize the playlist title for folder naming (replace spaces and slashes with underscores)
sanitized_title = playlist_title.replace(" ", "_").replace("/", "_").replace("\\", "_")
output_dir = os.path.join(base_path, sanitized_title)
os.makedirs(output_dir, exist_ok=True)

print(Fore.GREEN + f"📁 Folder: {output_dir}")

# Fetch list of video entries from the playlist
print(Fore.BLUE + "\n🔍 Fetching video entries...\n")
try:
    result = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--dump-json", playlist_url],
        capture_output=True,
        text=True,
        check=True
    )
    videos_json = result.stdout.strip().splitlines()
    total_videos = len(videos_json)
except subprocess.CalledProcessError as e:
    print(Fore.RED + "❌ Failed to fetch playlist info.")
    print(e)
    exit(1)

print(Fore.MAGENTA + f"🎬 Total videos found: {total_videos}\n")

# Download each video one-by-one ensuring video and audio are merged in MP4 format.
for idx, video_entry in enumerate(videos_json, start=1):
    video_id = json.loads(video_entry).get("id")
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    videos_left = total_videos - idx

    print(Fore.YELLOW + f"⬇ Downloading video {idx}/{total_videos} (Remaining: {videos_left})...")

    command = [
        "yt-dlp",
        "--no-warnings",
        "--quiet",
        "--no-progress",
        "-f", format_string,
        "--merge-output-format", "mp4",
        "-o", os.path.join(output_dir, f"{idx:02d} - %(title)s.%(ext)s"),
        video_url
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(Fore.GREEN + "\n✅ All videos downloaded successfully!")
