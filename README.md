# 🎬 YouTube Video Downloader

## 🌐 Overview

This script allows you to download YouTube videos using the Pytube library and the YouTube API.

The following features are supported:

1. Searching for a video and downloading the one that's most relevant to the search.
1. Passing the name of a YouTube channel and downloading:
   1. The most recently uploaded video on the channel.
   1. The most viewed video on the channel.

The script attempts to download each video in the highest resolution possible (720p, 480p, or 360p with audio).

## ✅ Prerequisites

- Run `python -m venv .venv` to create a virtual environment.
- To activate the created virtual environment, run `source .venv/bin/activate`.
- Run `pip install requirements.txt` to install the dependencies required to run the script.
- Ensure that the `.env` file in the root of the project's directory follows the `.env.template`
  and has a valid YouTube API Key.

## 🛠️ How to Get a YouTube API Key

1. Log in to the [Google Developers Console](https://console.cloud.google.com/welcome).
1. Create a [new project](https://console.cloud.google.com/projectcreate).
1. On the new project dashboard, click Explore & Enable APIs.
1. In the library, navigate to YouTube Data API v3 under YouTube APIs.
1. Enable the API.
1. Create a credential.
1. A screen will appear with the API key!

For detailed instructions on getting a YouTube API key, [follow this tutorial with screenshots](https://blog.hubspot.com/website/how-to-get-youtube-api-key) OR [watch this 2min video](https://www.youtube.com/watch?v=yuM7KH-JLu8) 😄

## ✨ Usage

#### Run `python main.py --help` to get an overview of the arguments that need to be passed.

### 🔹 Download a video by searching for it

Run `python main.py video <search_term>`

### 🔹 Download the most recetly uploaded video from a given YouTube channel

Run `python main.py channel <channel_name> --latest`

### 🔹 Download the most viewed video from a given YouTube channel

Run `python main.py channel <channel_name> --most_viewed`

## 📤 Output

By default, the downloaded videos will be stored in the 'videos' folder in the root of the project.

## 📝 Note

1. If the 'videos' folder does not exist, the script will create it.
1. The script prioritizes downloading videos in the following resolutions: 720p, 480p, and 360p with audio.
1. If a video cannot be downloaded due to an error, the error message will be displayed, and the script will gracefully exit.

## 🪄 Examples of how to execute the script

1. `python video "TechFTW Intro"` -> Downloads the TechFTW channel's intro video.
1. `python channel mkbhd --latest` -> Downloads MKBHD's most recent video.
1. `python channel mkbhd --most_viewed` -> Downloads MKBHD's most watched video.

## ⚠️ Disclaimer

This script is for educational and personal use only. Respect the intellectual property rights of the content creators and adhere to YouTube's terms of service.

## 🖥️ Author of the original project

[Rajkishor Patra](https://github.com/imraj569)
