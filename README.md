# 🎬 YouTube Video Downloader

## 🌐 Overview
This script allows you to download YouTube videos using the Pytube library. It reads a list of YouTube video URLs from a file (`urls.txt`) and attempts to download each video in the highest resolution possible (720p, 480p, or 360p with audio)also able to download whole youtube playlist.

## ✅ Prerequisites
- Run `pip install requirements.txt`

## ✨ Usage

### 🔹 Download list of videos
1. Create a text file named `urls.txt` in the same directory as the script.
2. Add one YouTube video URL per line in the `urls.txt` file.
3. Run the script using the command `python downloader.py` in your terminal or command prompt.

### 🔹 Download a playlist
1. Run the script using the command `python playlist.py` in your terminal or command prompt.
2. Enter the playlist URL when prompted.

## 📤 Output
- Downloaded videos will be stored in the 'Youtube_Videos' folder in the script's directory.
- The script will remove successfully downloaded video URLs from the `urls.txt` file.
- If an error occurs during the download, the script will print an error message and continue to the next video.

## 🖊️ Note
- If the 'Youtube_Videos' folder does not exist, the script will create it.
- The script prioritizes downloading videos in the following resolutions: 720p, 480p, and 360p with audio.
- If a video cannot be downloaded due to an error, the error message will be displayed, and the script will proceed to the next video.

## ⚠️ Disclaimer
This script is for educational and personal use only. Respect the intellectual property rights of the content creators and adhere to YouTube's terms of service.

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🖥️ Author
Rajkishor Patra

## Contributors 🍉
Thanks goes to these wonderful people ([:hugs:](https://allcontributors.org/docs/en/emoji-key)):
<table>
    <tbody>
        <tr>
        <td align="center">
            <a href="https://github.com/imraj569">
                <img src="https://avatars.githubusercontent.com/u/53007802?v=4" width="50px;" alt="Harsh Pandey"/>
                <br />
                <sub><b>Rajkishor Patra</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/BenoitPrmt">
                <img src="https://avatars.githubusercontent.com/u/46625877?v=4" width="50px;" alt="Harsh Pandey"/>
                <br />
                <sub><b>BenoitPrmt</b></sub>
            </a>
        </td>
      </tr>
    </tbody>
</table>

