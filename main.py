"""Entry point to the YouTube video downloader"""
import argparse
import os
import sys

from colorama import Fore, init
from dotenv import load_dotenv

from lib import arguments, youtube
from lib.downloader import download_video
from lib.errors import DownloadError, YouTubeAPIQueryError

init(autoreset=True)
load_dotenv()

parser = argparse.ArgumentParser(description="Program to Download a YouTube Video")
parser.add_argument(
    "search_for",
    choices=["channel", "video"],
    type=str,
    help="Choose between 'channel' or 'video' to search YouTube for"
)
parser.add_argument("search_term", type=str, help="The search term")
parser.add_argument(
    "-l",
    "--latest",
    action="store_true",
    help="Optional: Pass only when searching for a channel"
)
parser.add_argument(
    "-mv",
    "--most_viewed",
    action="store_true",
    help="Optional: Pass only when searching for a channel"
)

args_namespace = parser.parse_args()

args = arguments.parse_and_validate(
    args_namespace.latest,
    args_namespace.most_viewed,
    args_namespace.search_for,
    args_namespace.search_term
)

if not args.valid:
    print(
        Fore.RED +
        "Please pass ONE OF (-l, --latest, -mv, --most_viewed) " \
        "along with the name of the YT channel to search for"
    )
    sys.exit(0)

api_key = os.getenv("API_KEY")
try:
    if args.channel:
        if args.filter == "latest":
            video_url = youtube.get_latest_video_url(args.search_term, api_key)
        elif args.filter == "most_viewed":
            video_url = youtube.get_most_viewed_video_url(args.search_term, api_key)
    elif args.video:
        video_url = youtube.get_most_relevant_video_url(args.search_term, api_key)
except YouTubeAPIQueryError as e:
    print(Fore.RED + str(e))
    sys.exit()

try:
    download_video(video_url)
except DownloadError as e:
    print(Fore.RED + "Download failed: " + str(e))
    sys.exit()
