import glob
import os
import subprocess
import shutil


def concat_video(output_file='result.mp4', auto=False):
    def get_video_number(filename):
        return int(filename.split('_')[1].split('.')[0])

    filenames = glob.glob('temp/*.mp4')
    sorted_filenames = sorted(filenames, key=get_video_number)
    sorted_filenames = list(
        map(lambda x: x.replace("\\", "/"), sorted_filenames))

    for file in sorted_filenames:
        with open('urls.txt', 'a') as file:
            file = file.replace("\\", "/")
            file.write(f"file '{file}'\n")

    command = f'ffmpeg -f concat -i urls.txt -c copy "{output_file}" -loglevel quiet'

    subprocess.call(command, shell=True)

    os.remove('urls.txt')

    if not auto:
        if input('Delete video (from temp dir)? (y/n) >>> ').lower() == 'y':
            shutil.rmtree('temp')
            os.mkdir('temp')
            print('Program finished!')

        else:
            print('Program finished!')

    else:
        shutil.rmtree('temp')
        os.mkdir('temp')
