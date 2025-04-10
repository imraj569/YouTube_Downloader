# 🎬 YouTube Video & Playlist Downloader

## 🌐 Overview

This project contains Python scripts that allow you to download YouTube videos or entire playlists using [yt-dlp](https://github.com/yt-dlp/yt-dlp) with fallback logic to ensure that every video is downloaded with audio. Videos will be downloaded in the chosen resolution with the following priorities:

- **High:** Best available video and audio streams (or best combined format).
- **Medium:** 720p is preferred. If 720p with separate audio is not available, a lower‑resolution video with audio is downloaded.
- **Low:** 360p is preferred. If not available, a lower‑resolution video with audio is downloaded.

The scripts feature a colorful terminal UI using [colorama](https://pypi.org/project/colorama/), a clear screen function, and a custom banner displaying your GitHub information. The downloader works on both Windows and Termux (Android).

## ✅ Prerequisites

1. Install required packages by running:

   ```bash
   pip install yt-dlp colorama
   ```

2. On Termux (Android), ensure you install `ffmpeg` (and Python if needed):

   ```bash
   pkg install ffmpeg python
   ```

## ✨ Usage

### 🔹 Download a Playlist

1. Run the playlist downloader script using:

   ```bash
   python playlist.py
   ```

2. When prompted, enter the YouTube playlist URL.  
   Then, select one of the following video quality options:

   - **1. High:** Downloads using the best available video & audio.
   - **2. Medium (720p):** Prefers 720p with audio; if not available, downloads a lower resolution that includes audio.
   - **3. Low (360p):** Prefers 360p with audio; if not available, downloads a lower resolution that includes audio.

3. The script will automatically fetch the playlist metadata, create a download folder (with a sanitized version of the playlist title), and download all videos with audio merged in MP4 format.

### 🔹 Download a List of Videos

*Note: The project also includes an individual video downloader (`downloader.py`) that uses a text file with URLs. See below for additional info.*

1. Create a text file named `urls.txt` in the script's directory.
2. Add one YouTube video URL per line.
3. Run the script using:

   ```bash
   python downloader.py
   ```

4. Downloaded videos are stored in the `Youtube_Videos` folder (the folder is created automatically if missing) in the project directory.
5. Successfully downloaded video URLs are removed from `urls.txt`.  
   If an error occurs during a download, the error message is displayed, and the script continues to the next video.

## 📤 Output

- **Playlist Downloads:**  
  Videos are stored in a folder named after the sanitized playlist title within your Downloads folder. On Windows this defaults to your Downloads folder (e.g., `C:\Users\<YourUsername>\Downloads`), while on Termux, videos are saved in `/sdcard/Download`.

- **Video Downloads (Individual):**  
  Downloaded videos are stored in the `Youtube_Videos` folder in the project's directory.

## 🖊️ Additional Features

- **Clear Screen & Banner:**  
  When a script is started, it clears the terminal screen and displays a custom banner along with your GitHub information.

- **Fallback Resolution Logic:**  
  For Medium and Low quality options, if a video in the preferred resolution is unavailable with proper audio, the script automatically falls back to a lower resolution that includes audio.

## ⚠️ Disclaimer

This project is for educational and personal use only. Please respect the intellectual property rights of content creators and ensure you adhere to YouTube's Terms of Service.

## 📝 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## 🖥️ Author

**Rajkishor Patra**

## Contributors 🍉

Thanks to these wonderful contributors:

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/imraj569">
          <img src="https://avatars.githubusercontent.com/u/53007802?v=4" width="50px" alt="Rajkishor Patra"/>
          <br />
          <sub><b>Rajkishor Patra</b></sub>
        </a>
      </td>
      <td align="center">
        <a href="https://github.com/BenoitPrmt">
          <img src="https://avatars.githubusercontent.com/u/46625877?v=4" width="50px" alt="BenoitPrmt"/>
          <br />
          <sub><b>BenoitPrmt</b></sub>
        </a>
      </td>
    </tr>
  </tbody>
</table>
