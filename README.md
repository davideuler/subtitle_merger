
How to download a YouTube video with Chinese and English subtitles, and merge both Chinese and English subtitles into the video to create a video with embedded bilingual subtitles.

The same applies to other languages.

## 1.Download youtube videos with subtitle in multi languages.

```Bash
yt-dlp --write-subs --write-auto-subs --sub-format SRT --sub-langs "en,en-orig,zh-Hans" --write-thumbnail --write-description https://www.youtube.com/xxxxx

# or:
yt-dlp --write-subs --write-auto-subs --sub-format srt --convert-subs "srt" --sub-langs "en,en-orig,zh-Hans" --write-thumbnail --write-description "https://www.youtube.com/watch?v=ZA9K0JMrbWg"

```

## 2.To merge two subtitle files into one:

```bash
python merge_subtitle.py <srt_file1> <srt_file2> merged_subtitles.srt
```

The output file content is like this:
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

## 3.Then you can merge the subtitle file and origin video file.
Thus you can get a video file with embedded subtitles in two languages.

```
ffmpeg -i input_video.mp4 -vf "subtitles=merged_subtitles.srt" -c:a copy output_video.mp4
```

## Prerequisites
```Bash
$ pip install -r requirements.txt

# install ffmpeg on mac:
$ brew install ffmpeg

# for Ubuntu/Debian, install by apt:
$ sudo apt-get install ffmpeg
```