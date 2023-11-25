
## To merge two subtitle files into one:

python merge_srt.py <srt_file1> <srt_file2> merged_subtitles.srt

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

## Then you can merge the subtitle file and origin video file.
Thus you can get a video file with embedded subtitles in two languages.

```
ffmpeg -i input_video.mp4 -vf "subtitles=merged_subtitles.srt" -c:a copy output_video.mp4
```

