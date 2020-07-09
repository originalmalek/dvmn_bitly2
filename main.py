import argparse
import os
import requests
from dotenv import load_dotenv


def shorten_link(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    header = {'Authorization': f'Bearer {token}'}
    payload = {"long_url": long_url}

    response = requests.post(url, headers = header, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(short_url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_url}/clicks/summary'
    header = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=header)
    response.raise_for_status()
    return response.json()['total_clicks']


def correct_bitly_link(url):
    if 'https' in url:
        return url[8:]
    else:
        return url


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')

    parser = argparse.ArgumentParser(description='The programm create short link or show clicks on short link')
    parser.add_argument('url', help='Enter short or long url')
    args = parser.parse_args()
    url = args.url

    if url.startswith('bit.ly') or url.startswith('https://bit.ly'):
        try:
            print('Total clicks: ', count_clicks(correct_bitly_link(url), token))
        except requests.exceptions.HTTPError as e:
            print(e)
    else:
        try:
            print('Bitlink: ', shorten_link(url, token))
        except requests.exceptions.HTTPError as e:
            print(e)


if __name__ == '__main__':
    main()
