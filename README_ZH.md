如何下载 youtube 带中英文字幕的视频， 并同时合并中英文字幕到视频中，制作成内嵌中英文字幕的视频。

其他多语言同理。

https://github.com/davideuler/subtitle_merger
 
## 1.下载自动中英文字幕
如果没有 srt 字幕， 使用选项强制转换成 srt 字幕：

```Bash
yt-dlp --write-subs --write-auto-subs --sub-format srt --convert-subs "srt" --sub-langs "en,en-orig,zh-Hans" --write-thumbnail --write-description "https://www.youtube.com/watch?v=ZA9K0JMrbWg"
```

## 2.合并中英文字幕文件为一个字幕文件
```bash
python merge_subtitle.py <srt_file1> <srt_file2> merged_subtitles.srt
```

输出的字幕文件内容样例：
```
    1
    00:00:00,000 --> 00:00:02,430
    自计算机开始以来，编码
    Coding has been the bread and butter for 
    2
    00:00:02,430 --> 00:00:04,290
    一直是开发人员的必需品。
    developers since the dawn of computing. 

```

## 3.合并字幕和视频为内嵌字幕的 mp4
```bash
ffmpeg -i input_video.mp4 -vf "subtitles=merged_subtitles.srt" -c:a copy output_video.mp4
```

## 前提条件
```Bash
$ pip install -r requirements.txt

# install ffmpeg on mac:
$ brew install ffmpeg

# for Ubuntu/Debian, install by apt:
$ sudo apt-get install ffmpeg
```
