from download_video import download
from clip_video import concat_video
from time import time

import glob

filenames = glob.glob('*.m3u8')
filenames = list(map(lambda x: x.replace("\\", "/"), filenames))

for filename in filenames:
    print(f'[+] Processing: {filename} [+]')

    start_time = time()

    name = filename.removeprefix('temp/').removesuffix('.m3u8')
    file_path = filename

    download(
        file=file_path,
        url=None,
    )

    print('[+] Short videos downloaded! [+]')

    concat_video(
        output_file=name + '.mp4',
        auto=True
    )

    print(
        f'[+] Video {name} is generated! Spent time: {round(time() - start_time)} ceкунд! [+]\n')
