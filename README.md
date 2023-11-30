# YouTube Video Downloader

This script downloads videos from YouTube based on a list of URLs provided in a 'urls.txt' file. It prioritizes downloading videos in 720p resolution, but if 720p is not available, it will try 480p. If 480p is not available either, it will download the best available resolution (360p or lower) with audio.

## Requirements

* Python 3.6 or higher
* pytube library (install using pip: `pip install pytube`)

## Usage

1. Create a file named 'urls.txt' and add the URLs of the videos you want to download, one URL per line.

2. Download and install the pytube library using pip:

```bash
pip install pytube

python download_videos.py


## Output

The script will print the status of each video download to the console.

## Errors

If any errors occur during the download process, the script will print an error message to the console.

## License

This script is licensed under the MIT License.

## Contributing

If you would like to contribute to this script, please fork the repository and make your changes. Create a pull request to submit your changes for review.
