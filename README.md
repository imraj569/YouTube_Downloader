# 🎬 YouTube Video, Playlist & Music Downloader

## 🌐 Overview

This project contains powerful Python scripts that allow you to download YouTube **videos**, **playlists**, and **music tracks** using [yt-dlp](https://github.com/yt-dlp/yt-dlp), with audio merging, resolution fallback logic, and colorful terminal UI using [colorama](https://pypi.org/project/colorama/).  
It supports both **Windows** and **Termux (Android)**.

### 🔧 Features

- ✅ Download individual YouTube videos or entire playlists
- 🎵 Download YouTube music into organized categories (e.g., LoFi, Hindi 90s)
- 📉 Fallback resolution logic: 720p/360p preferred, gracefully falls back
- 🎨 Beautiful CLI with colorized output
- 📂 Auto-create folders and smart output paths
- 📦 Works on **Windows** and **Termux (Android)**

---

## ✅ Prerequisites

Install Python dependencies:

```bash
pip install yt-dlp colorama
```

For **Termux** (Android), install additional tools:

```bash
pkg install ffmpeg python
termux-setup-storage  # (for access to Downloads folder)
```

---

## ✨ Scripts & Usage

### 🔹 `playlist.py` – Download Full YouTube Playlists

1. Run the script:

   ```bash
   python playlist.py
   ```

2. Paste the playlist URL.
3. Select quality:
   - `1. High` – Best available video + audio
   - `2. Medium (720p)` – Falls back if 720p not available
   - `3. Low (360p)` – Falls back if 360p not available

4. Output folder is automatically created from the playlist title:
   - **Windows:** `~/Downloads/<Playlist Name>`
   - **Termux:** `/Download/<Playlist Name>`

---

### 🔹 `downloader.py` – Download Multiple Videos via Text File

1. Create a `urls.txt` in the same folder.
2. Add YouTube video URLs (one per line).
3. Run the script:

   ```bash
   python downloader.py
   ```

4. Videos will be downloaded into:
   - `Youtube_Videos/` (auto-created)
5. Successfully downloaded URLs are removed from `urls.txt`.

---

### 🔹 `music_downloader.py` – 🎵 Music Downloader with Categories

1. Run the music downloader:

   ```bash
   python music_downloader.py
   ```

2. Paste any **YouTube or music URL** (`youtube.com`, `youtu.be`, `music.*`).
3. Choose a category like:
   - `Odia`, `Hindi 90s`, `Bengali`, `DJ Songs`, `LoFi`
   - ➕ Add your own custom category!
4. Output path:
   - **Windows:** `~/Downloads/musics/<Category>`
   - **Termux:** `/downloads/musics/<Category>`

🎧 Downloads are saved in high-quality `.mp3` format using `ffmpeg`.

---

## 📁 Output Summary

| Script               | Output Location (Windows)                | Output Location (Termux)                                   |
|----------------------|------------------------------------------|-------------------------------------------------------------|
| `playlist.py`        | `Downloads/<Playlist Name>`              | `/sdcard/Download/<Playlist Name>`                          |
| `downloader.py`      | `Youtube_Videos/`                        | `Youtube_Videos/`                                           |
| `music_downloader.py`| `Downloads/musics/<Category>`            | `~/storage/downloads/musics/<Category>`                     |

---

## 🖼️ Terminal UI Preview

```plaintext
╔══════════════════════════════════════╗
║     🎵 YouTube Music Downloader      ║
╠══════════════════════════════════════╣
║ GitHub: https://github.com/imraj569 ║
╚══════════════════════════════════════╝

🎶 Select a music category:
1. Hindi 90s
2. Bengali
3. DJ Songs
4. ➕ Add new category
```

---

## ⚠️ Disclaimer

This project is for **educational and personal use only**. Please respect copyright laws and YouTube's [Terms of Service](https://www.youtube.com/t/terms).

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🖥️ Author

**Rajkishor Patra**

---

## 🍉 Contributors

Thanks to these awesome contributors:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/imraj569">
        <img src="https://avatars.githubusercontent.com/u/53007802?v=4" width="50px;" alt="Rajkishor"/>
        <br />
        <sub><b>Rajkishor Patra</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/BenoitPrmt">
        <img src="https://avatars.githubusercontent.com/u/46625877?v=4" width="50px;" alt="Benoit"/>
        <br />
        <sub><b>BenoitPrmt</b></sub>
      </a>
    </td>
  </tr>
</table>
