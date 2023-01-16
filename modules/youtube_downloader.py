import pyperclip
import pytube
from pathlib import Path


def download_video():
    downloads_path = str(Path.home() / "Downloads")

    url = pyperclip.paste()
    if 'youtu' not in url:
        raise Exception("Wrong URL copied")

    video = pytube.YouTube(url)
    video. \
        streams. \
        filter(progressive=True, file_extension="mp4"). \
        first(). \
        download(output_path=downloads_path)
