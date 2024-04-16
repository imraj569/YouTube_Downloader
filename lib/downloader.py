"""Method for downloading high resolution YouTube videos"""

from colorama import Fore
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

from lib.errors import DownloadError

def download_video(url: str, output_path: str = "videos") -> None:
    """Downloads the video from the given URL into the specified output directory

    Args:
        url: str -> URL of the YouTube video that is to be downloaded
        output_path: str -> Intended location of the downloaded video.
                            Defaults to "videos"
    
    Raises:
        DownloadError -> Raised when the video couldn't be downloaded
                         without logging in
    """

    yt = YouTube(url)

    # List defining the priority of video resolutions when
    # attempting to download the video
    resolutions = ["720p", "480p", "360p"]
    video_found = False

    for resolution in resolutions:
        try:
            stream = yt.streams.filter(
                progressive=True, resolution=resolution).filter(only_audio=False
            ).first()
        except AgeRestrictedError as e:
            raise DownloadError(
                "Video is age restricted. Can't be downloaded without logging in"
            ) from e
        if stream:
            video_found = True
            break

    if not video_found:
        failed_info = "Couldn't find video in 720p or 480p or 360p with audio."
        print(Fore.RED + failed_info)

    video_title = f"Downloading {stream.title} in {stream.resolution}"
    print(Fore.YELLOW + video_title)

    stream.download(output_path)
    print(Fore.GREEN + "Download Completed ✅")
