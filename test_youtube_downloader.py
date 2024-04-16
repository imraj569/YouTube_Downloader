"""Unit testing suite"""
import time
import os
import pytest
from dotenv import load_dotenv

from lib.arguments import parse_and_validate
from lib.downloader import download_video
from lib import youtube

load_dotenv()
API_KEY = os.getenv("API_KEY")

def test_exception_raised_when_no_video_is_found() -> None:
    """Downloading the video when there are no videos matching the search"""
    with pytest.raises(Exception, match="No videos found for 'some_query_with_no_videos'"):
        youtube.get_most_relevant_video_url("some_query_with_no_videos", API_KEY)


def test_exception_raised_when_invalid_api_key_is_passed() -> None:
    """Downloading the video with an invalid API Key"""
    with pytest.raises(
        Exception,
        match="YouTube API request failed: API key not valid. Please pass a valid API key."
    ):
        youtube.get_most_relevant_video_url("some_video", "BAD_API_KEY")


def test_parsing_invalid_args() -> None:
    """Passing different sets of invalid parameters
    to the arguments.parse_and_validate() method.
    """

    # Setting both 'latest' and 'most_viewed' to True
    args = {
        "latest": True,
        "most_viewed": True,
        "search_for": "channel",
        "search_term": "some_channel"
    }

    parsed_args = parse_and_validate(
        args["latest"], args["most_viewed"], args["search_for"], args["search_term"]
    )

    assert parsed_args.valid is False

    # Setting both 'latest' and 'most_viewed' to False
    args["latest"] = args["most_viewed"] = False

    parsed_args = parse_and_validate(
        args["latest"], args["most_viewed"], args["search_for"], args["search_term"]
    )

    assert parsed_args.valid is False


def test_parsing_and_validation_of_args_happy_path() -> None:
    """Passing valid set of parameters to the arguments.parse_and_validate() method"""

    args = {
        "latest": True,
        "most_viewed": None,
        "search_for": "channel",
        "search_term": "some_channel"
    }

    parsed_args = parse_and_validate(
        args["latest"], args["most_viewed"], args["search_for"], args["search_term"]
    )

    assert parsed_args.channel is True
    assert parsed_args.filter == "latest"
    assert parsed_args.search_term == "some_channel"
    assert parsed_args.valid is True
    assert parsed_args.video is False


def test_getting_relevant_youtube_video_url() -> None:
    """Fetching the URL of the most relevant video matching the search"""
    expected_youtube_video_url = "https://www.youtube.com/watch?v=o7DVxMXiISk"

    video_url = youtube.get_most_relevant_video_url("TechFTW Intro", API_KEY)

    assert video_url == expected_youtube_video_url

def test_getting_latest_youtube_video_url() -> None:
    """Fetching the URL of the most recent Veritasium video"""
    latest_veritasium_video_id = "2FLqOI9jw-E"

    video_url = youtube.get_latest_video_url("Veritasium", API_KEY)

    assert video_url == (youtube.YOUTUBE_VIDEO_BASE_URL + latest_veritasium_video_id)


def test_getting_most_viewed_youtube_video_url() -> None:
    """Fetching the URL of the most viewed Veritasium video"""
    most_popular_veritasium_video_id = "uxPdPpi5W4o"
    video_url = youtube.get_most_viewed_video_url("Veritasium", API_KEY)

    assert video_url == (youtube.YOUTUBE_VIDEO_BASE_URL + most_popular_veritasium_video_id)


def test_download_video() -> None:
    """Downloading a video to the default 'videos/' directory"""
    shortest_youtube_video_url = "https://www.youtube.com/watch?v=tPEE9ZwTmy0"

    assert os.path.exists("videos/Shortest Video on Youtube.mp4") is False
    download_video(shortest_youtube_video_url)
    time.sleep(2)
    assert os.path.exists("videos/Shortest Video on Youtube.mp4") is True

    os.remove("videos/Shortest Video on Youtube.mp4")
