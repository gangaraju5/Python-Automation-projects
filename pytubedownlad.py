import yt_dlp
from pytube import YouTube

link = input("---> please paste the link here:")
yt = YouTube(link)
print("Title of the video:", yt.title)
print("Total views of the video:", yt.views)

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Downloads best video + best audio and merges them
    'merge_output_format': 'mp4',          # Ensures output is in mp4 format
    'outtmpl': 'c:/Users/Rajuyadav/Desktop/Youtubevideodownloader/%(title)s.%(ext)s',  # Output folder
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferredformat': 'mp4',  # Ensure video is converted to mp4
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
