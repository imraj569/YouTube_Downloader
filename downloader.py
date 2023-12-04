import pytube
import os


# Text file path
urls_file = "urls.txt"

# Download directory
download_dir = "/data/data/com.termux/files/home/storage/downloads"
if not os.path.exists(download_dir):
    download_dir = os.getcwd()

# Error log file
error_log = "download_errors.log"

# Initialize variables
total_videos = 0
downloaded_videos = 0
failed_videos = 0

# Read URLs from file
with open(urls_file, "r") as f:
    urls = [line.strip() for line in f]
    total_videos = len(urls)

# Iterate over URLs
for url in urls:
    try:
        # Get video object
        yt = pytube.YouTube(url)

        # Check if video already exists
        file_path = os.path.join(download_dir, yt.title + "." + yt.streams.filter(progressive=True).first().extension)
        if os.path.exists(file_path):
            # Resume download if partially downloaded
            if os.path.getsize(file_path) < yt.streams.filter(progressive=True).first().filesize:
                print(f"Resuming download: {yt.title}")
                yt.streams.filter(progressive=True).first().download(filename=file_path, resume=True)
            else:
                print(f"Skipping already downloaded: {yt.title}")
                continue

        # Try downloading 480p
        stream = yt.streams.filter(resolution="480p").first()

        # Fallback to 360p if 480p not available
        if not stream:
            stream = yt.streams.filter(resolution="360p").first()

        # Download video
        print(f"Downloading: {yt.title}")
        stream.download(filename=file_path)

        downloaded_videos += 1
    except Exception as e:
        # Log error
        with open(error_log, "a") as f:
            f.write(f"Error downloading {url}: {e}\n")
        failed_videos += 1
        print(f"Error downloading: {yt.title}")

# Print summary
print(f"\nDownload completed. Downloaded {downloaded_videos}/{total_videos} videos. Failed: {failed_videos}")

