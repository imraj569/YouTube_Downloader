from yt_dlp import YoutubeDL
import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# -------- Banner -------- #
def show_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{Fore.CYAN}{Style.BRIGHT}")
    print("╔══════════════════════════════════════╗")
    print("║     🎵 YouTube Music Downloader      ║")
    print("╠══════════════════════════════════════╣")
    print(f"║ GitHub: {Fore.YELLOW}https://github.com/imraj569{Fore.CYAN} ║")
    print("╚══════════════════════════════════════╝\n")
    print(f"{Style.RESET_ALL}")

# -------- Helpers -------- #
def is_termux():
    return "com.termux" in os.getcwd()

def get_base_folder():
    if is_termux():
        return os.path.join("data", "data", "com.termux", "files", "home", "storage", "downloads")
    return os.path.expanduser("~/Downloads")

# -------- Category Selection -------- #
def get_music_category(categories):
    while True:
        show_banner()
        print(f"{Fore.MAGENTA}Select a music category:\n")
        for i, category in enumerate(categories, 1):
            print(f"{Fore.YELLOW}{i}. {category}")
        print(f"{Fore.GREEN}{len(categories)+1}. ➕ Add new category")

        try:
            choice = int(input(f"\n{Fore.BLUE}Your choice: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            elif choice == len(categories) + 1:
                new_category = input(f"{Fore.CYAN}Enter new category name: ").strip()
                if new_category:
                    categories.append(new_category)
                    return new_category
                else:
                    print(f"{Fore.RED}⚠️ Category name cannot be empty!")
                    time.sleep(2)
            else:
                print(f"{Fore.RED}⚠️ Invalid choice.")
                time.sleep(2)
        except ValueError:
            print(f"{Fore.RED}⚠️ Please enter a number.")
            time.sleep(2)

# -------- Music Downloader -------- #
def download_music(url, folder, base_folder):
    print(f"{Fore.MAGENTA}Finding URL source: YouTube Music")
    try:
        target_folder = os.path.join(base_folder, "musics", folder)
        os.makedirs(target_folder, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{target_folder}/%(title)s.%(ext)s',
            'quiet': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'postprocessor_args': ['-ar', '44100'],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown Title')
            print(f"{Fore.GREEN}✅ Downloaded: {title}.mp3")
            print(f"{Fore.BLUE}📁 Saved to: {target_folder}")
            time.sleep(3)

    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")
        time.sleep(3)

# -------- Video Downloader -------- #
def download_video(url, folder, base_folder):
    print(f"{Fore.MAGENTA}Finding URL source: YouTube")
    try:
        target_folder = os.path.join(base_folder, "musics", folder)
        os.makedirs(target_folder, exist_ok=True)

        options = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{target_folder}/%(title)s.%(ext)s',
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])
        print(f"{Fore.GREEN}✅ Download complete.")
        print(f"{Fore.BLUE}📁 Saved to: {target_folder}")
        time.sleep(3)

    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")
        time.sleep(3)

# -------- Main App -------- #
if __name__ == "__main__":
    base_folder = get_base_folder()
    categories = ["Odia", "Hindi 90s", "Bengali", "DJ Songs", "Lofi"]

    while True:
        show_banner()
        url = input(f"{Fore.BLUE}Enter YouTube/YouTube Music URL (or type 'exit'): ").strip()

        if url.lower() == "exit":
            print(f"{Fore.YELLOW}👋 Exiting. See you again!")
            break

        folder = get_music_category(categories)

        if "youtube.com" in url or "youtu.be" in url:
            download_video(url, folder, base_folder)
        elif "music." in url:
            download_music(url, folder, base_folder)
        else:
            print(f"{Fore.RED}⚠️ Invalid URL format.")
            time.sleep(2)
