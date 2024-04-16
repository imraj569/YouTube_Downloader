"""Defining custom exceptions that get raised when either the
query to the YouTube API fails or when the video-download fails.
"""

class DownloadError(Exception):
    """Raised when downloading the video fails"""


class YouTubeAPIQueryError(Exception):
    """Raised when the YouTube API query fails"""
