import os
from os import path as mpath


def ffmpeg_transform(path ,coderStr ,oldFormat ,newFormat ):
    # 获取文件路径
    source = mpath.normpath(path)
    #获取文件名称列表
    videoList = os.listdir(source)
    videoListTemp = [];

    # 只选择目录下的oldformat参数格式文件
    for formatname in videoList:
        if formatname.endswith(oldFormat):
            videoListTemp.append(formatname)

    # 执行ffmpeg命令
    for i in videoListTemp:
        oldname = i
        oldname = os.path.join(path,oldname)
        
        output  = i[0:-4]
        newname = output + newFormat
        newname = os.path.join(path,newname)
        
        otherStr = " "
        cmd = "ffmpeg -y -i "+"\""+ oldname +"\" "+ coderStr +" \""+ newname + "\""
        os.system(cmd)
        print(cmd)
        
    
    pass


# 在这里输入你要转换文件所在的文件夹路径    
path = r'E:\dsmbili\save'

# 这里改为现在的格式
oldFormat = '.mp3'

# 这里改为你需要的格式
newFormat = '.wav'

# ffmpeg方法的一些参数 自行选择
coderStr = " -acodec pcm_s16le -f s16le -ac 1 -ar 16000 "


ffmpeg_transform(path,coderStr,oldFormat,newFormat)   
