import pytube
import os

def download_videos():
    with open('urls.txt', 'r') as f:
        urls = f.readlines()

    total_videos = len(urls)
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

            print(f"Downloading video {downloaded_videos + 1}/{total_videos} ({remaining_videos} videos remaining) - {video.title} ({video_size} bytes)")

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
            print(f"Error downloading video {downloaded_videos + 1}: {e}")

if __name__ == '__main__':
    download_videos()