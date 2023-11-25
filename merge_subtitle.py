import srt
import sys

def merge_srt(subtitle1, subtitle2):
    # 合并两个字幕条目
    return srt.Subtitle(
        index=subtitle1.index,
        start=subtitle1.start,
        end=subtitle1.end,
        content=f"{subtitle1.content}\n{subtitle2.content}",
        proprietary='',
    )

def load_srt(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(srt.parse(file.read()))

def save_srt(subtitles, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(srt.compose(subtitles))

def main(srt_file1, srt_file2, output_file):
    # 加载SRT文件
    subtitles1 = load_srt(srt_file1)
    subtitles2 = load_srt(srt_file2)

    # 确保字幕条目数量相同
    if len(subtitles1) != len(subtitles2):
        print("Warning:字幕文件中的条目数量不匹配。会尝试对齐字幕")

    base_subtitle, another_subtitle = (subtitles2, subtitles1) if len(subtitles1) > len(subtitles2) else (subtitles1, subtitles2)

    # 合并字幕
    for i in range(len(base_subtitle)):
        subtitle = base_subtitle[i]
        for sub in another_subtitle:
            if sub.start == subtitle.start and sub.end == subtitle.end:
                base_subtitle[i].content = sub.content + '\n' + base_subtitle[i].content.replace('\n', ' ')
                continue
                
    
    # 保存合并后的字幕
    save_srt(base_subtitle, output_file)
    print(f"合并的字幕已保存到 {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merge_subtitle.py <srt_file1> <srt_file2> <output_file>")
    else:
        srt_file1 = sys.argv[1]
        srt_file2 = sys.argv[2]
        output_file = sys.argv[3]
        main(srt_file1, srt_file2, output_file)
