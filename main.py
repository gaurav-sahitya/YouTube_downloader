from pytube import YouTube
url=input("Enter YouTube URL: ")#"https://www.youtube.com/watch?v=P6au4e5SDA8"
yt=YouTube(url)
print(yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution"))