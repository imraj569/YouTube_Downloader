"""
Methods to query YouTube's Serach v3 API
and return the URL of the desired video.
"""
from typing import Dict
import requests

from lib.errors import YouTubeAPIQueryError


YOUTUBE_API_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_VIDEO_BASE_URL = "https://www.youtube.com/watch?v="

def _get_channel_id(channel_name: str, api_key: str) -> str:
    """Returns the channel_id best matching the given channel name
    
    Args:
        channel_name: str -> Name of the channel to search YouTube for

    Returns: str -> ID of the channel best matching the name
    
    Raises:
        YouTubeAPIQueryError -> When the YouTube API query fails
    """
    params = {"key": api_key, "q": channel_name, "type": "channel"}

    try:
        response = requests.get(
            url=YOUTUBE_API_URL, params=params, timeout=10
        )
    except (ConnectionError, TimeoutError) as e:
        raise YouTubeAPIQueryError("Error querying YouTube API") from e

    response_json = response.json()
    if not response.status_code == 200:
        raise YouTubeAPIQueryError(
            "YouTube API request failed: " + str(response_json["error"]["message"])
        )

    try:
        channel_id: str = response_json["items"][0]["id"]["channelId"]
        return channel_id
    except (IndexError, KeyError) as e:
        raise YouTubeAPIQueryError("Failed to retrieve the channel") from e


def _get_video_url(params: Dict[str, str]) -> str:
    """Returns the URL of the YouTube video by querying
    the YouTube API with the specified params
    """
    try:
        response = requests.get(
            url=YOUTUBE_API_URL, params=params, timeout=10
        )
    except (ConnectionError, TimeoutError) as e:
        raise YouTubeAPIQueryError("Error querying YouTube API: ") from e

    response_json = response.json()
    if not response.status_code == 200:
        raise YouTubeAPIQueryError(
            "YouTube API request failed: " + str(response_json["error"]["message"])
        )

    if not response_json["items"]:
        raise YouTubeAPIQueryError("No videos found for '" + str(params["q"] + "'"))

    try:
        video_id: str = response_json["items"][0]["id"]["videoId"]
    except (IndexError, KeyError) as e:
        raise YouTubeAPIQueryError("Failed to retrieve the YouTube video's ID") from e

    video_url =  YOUTUBE_VIDEO_BASE_URL + video_id

    return video_url

def get_latest_video_url(channel_name: str, api_key: str) -> str:
    """Returns the URL of the latest video from the given YouTube channel
    
    Args:
        channel_name: str -> Name of the channel to search YouTube for

    Returns: URL of the latest video from the given YouTube channel
    
    Raises:
        YouTubeAPIQueryError -> When the YouTube API query fails
    """
    channel_id = _get_channel_id(channel_name, api_key)
    # params = _get_params_for_latest_video(channel_id)
    params_for_latest_video = {
        "channelId": channel_id,
        "key": api_key,
        "order": "date",
        "type": "video"
    }
    video_url = _get_video_url(params_for_latest_video)

    return video_url



def get_most_viewed_video_url(channel_name: str, api_key: str) -> str:
    """Returns the URL of the video with the highest
    number of views from the given YouTube channel
    
    Args:
        channel_name: str -> Name of the channel to search YouTube for

    Returns: URL of the most popular video from the given YouTube channel
    
    Raises:
        YouTubeAPIQueryError -> When the YouTube API query fails
    """
    channel_id = _get_channel_id(channel_name, api_key)
    # params = _get_params_for_most_viewed_video(channel_id)
    params_for_most_viewed_video = {
        "channelId": channel_id,
        "key": api_key,
        "order": "viewCount",
        "type": "video"
    }
    video_url = _get_video_url(params_for_most_viewed_video)

    return video_url

def get_most_relevant_video_url(search_term: str, api_key: str) -> str:
    """Returns the URL of the YouTube video best matching the search term
    
    Args:
        search_term: str -> Video to search YouTube for

    Returns: URL of the YouTube video most relevant to the search term
    
    Raises:
        YouTubeAPIQueryError -> When the YouTube API query fails
    """
    params = {"key": api_key, "q": search_term, "type": "video"}
    video_url = _get_video_url(params)

    return video_url
