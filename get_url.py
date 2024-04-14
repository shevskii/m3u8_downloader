import re

import requests


def recognize(*, file_path=None, url=None):
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif url:
        return requests.get(url).content.decode('utf-8')


def get_urls(*, file_path=None, url=None):
    text = recognize(file_path=file_path, url=url)

    pattern = re.compile(r'https?://[^\s]+')
    urls: list = re.findall(pattern, text)
    return urls
