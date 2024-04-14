from download_video import download
from clip_video import concat_video

name = input('Video Name >>> ')
url = input('m3u8 URL (if the path is to files, click enter) >>> ')
file_path = input('file_path URL >>> ')

download(
    file=file_path if not file_path == '' else None,
    url=url if not url == '' else None,
)

concat_video(
    output_file=name
)