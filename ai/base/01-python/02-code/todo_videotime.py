import os
from moviepy.editor import VideoFileClip


def compute_video_time(path):
    type = ('.flv', '.mp4', '.ts', '.avi', '.rm', '3gp', '.rmvb', '.asf', '.mpg', '.wmv', 'mkv', '.vob')
    filelist = []

    for a, b, c in os.walk(path):
        for name in c:
            fname = os.path.join(a, name)
            fname = fname.lower()
            if fname.endswith(type):
                filelist.append(fname)
    print("------开始计算时间------")
    ftime = 0.0
    count = 0
    for item in filelist:
        try:
            clip = VideoFileClip(item)
            ftime += clip.duration
            count = count + 1
            print("已完成%.2f" % ((count / filelist.__len__()) * 100) + "%")
            clip.reader.close()  # 防止出现错误：句柄无效
            clip.audio.reader.close_proc()
        except:
            print(item)
    print("文件：", count)
    print(f"时长：{ftime / 3600}时, {ftime / 60}分, {ftime}秒")


if __name__ == "__main__":
    path = r"D:\01-Software\01-Installers\BaiduNetdisk\download"
    compute_video_time(path)
