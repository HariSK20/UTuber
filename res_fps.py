from pytube import YouTube
def res(obj):
    #count = 1
    available_resolutions = []
    #available_fps = []
    resolutions=["2160p","1440p","1080p","720p","360p","240p","144p"]
    #framerates=["24","25","30","48","50","60"]
    print("Select desired resolutions:")
    #print(len(resolutions))
    for i in range(len(resolutions)):
        temp = obj
        #if(len(temp.streams.filter(res=resolutions[i],file_extension='mp4'))>0):
        if(len(temp.streams.filter(res=resolutions[i],file_extension='mp4'))>0):
            available_resolutions.append(i)
            print(len(available_resolutions),". ",resolutions[i])
            #print(temp.streams.filter(res=resolutions[i]))
            #count = count+1
    #index = int(input())-1
    index = available_resolutions[int(input())-1]
    #Frame rate selection required
    return(resolutions[index])
if(__name__=='__main__'):
    URL = input()
    yt = YouTube(URL)
    res(yt)