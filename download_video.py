import os

from requests.adapters import HTTPAdapter
from tqdm import tqdm
from urllib3 import Retry

from get_url import get_urls
import requests

def download(*, file=None, url=None):
    urls = get_urls(file_path=file, url=url)
    print(f'[+] Quantity videos: {len(urls)} [+]')

    with tqdm(total=len(urls), desc='Proccesing...') as pbar:
        for url in urls:
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=1)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            response = session.get(url)

            if not os.path.isdir('temp'):
                os.mkdir('temp')

            with open(f'temp/video_{urls.index(url)}.mp4', 'wb') as file:
                file.write(response.content)

            pbar.update(1)

        pbar.set_description('Success!')