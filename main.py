try:
    from pytube import YouTube

    url=input("Enter YouTube URL: ")
    yt=YouTube(url)
    vid_str=yt.streams.filter(type="video",audio_codec="mp4a.40.2").order_by("resolution").desc()
    aud_str=yt.streams.filter(type="audio").order_by("abr").desc()

    vid_qul=[str(i).split()[3].split('"')[1] for i in vid_str]
    aud_qul=[str(i).split()[3].split('"')[1] for i in aud_str]

    print("\nAVAILABLE QUALITIES:")
    print("VIDEO:",sorted(set(vid_qul),key=lambda x:int(x[0:-1]),reverse=True))
    print("AUDIO:",sorted(set(aud_qul),key=lambda x:int(x[0:-4]),reverse=True))

    c=0
    while 1:
        qul=input("\nEnter the quality: ").lower().strip()
        if qul in vid_qul:
            print("\nVIDEO DOWNLOADED :)\nAt:",vid_str[vid_qul.index(qul)].download())
            break
        elif qul in aud_qul:
            print("\nAUDIO DOWNLOADED :)\nAt:",aud_str[aud_qul.index(qul)].download())
            break
        else:
            c+=1
            print("Check your input :(")
            if c==3:
                print("\nPlease Retry :(")
                break

except Exception as e:
    print(e)