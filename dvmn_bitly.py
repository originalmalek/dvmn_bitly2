import argparse
from dotenv import load_dotenv
import os
import requests


def get_info(token):
    url = 'https://api-ssl.bitly.com/v4/user'
    header = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=header)
    print(response.json())


def shorten_link(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    header = {'Authorization': f'Bearer {token}'}
    payload = {"long_url": long_url}

    response = requests.post(url, headers = header, json=payload).json()
    if 'message' in response:
        return response['message']
    return response['link']


def count_clicks(short_url, token):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{short_url}/clicks/summary'
    header = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=header).json()
    if 'message' in response:
        return response['message']
    return response['total_clicks']


def correct_bitly_link(url):
    if 'https' in url:
        return url[8:]
    else:
        return url


def main():
    load_dotenv()
    token = os.getenv('TOKEN')

    parser = argparse.ArgumentParser(description='The programm create short link or show clicks on short link')
    parser.add_argument('--url', help='Enter short or long url')
    args = parser.parse_args()
    url = args.url
    print(url)
    if url ==None:
        url = input('Enter link: ')
    # long_url = 'http://originalmalek.ru/'
    # short_url = 'bit.ly/2NW3suW' 'https://bit.ly/2NW3suW'

    if url.startswith('bit.ly') or url.startswith('https://bit.ly'):
        print('Total clicks: ', count_clicks(correct_bitly_link(url), token))
    else:
        print('Bitlink: ', shorten_link(url, token))


if __name__ == '__main__':
    main()
