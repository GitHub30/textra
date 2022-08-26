import argparse
import requests
from requests_oauthlib import OAuth1


def trans():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default='tra')
    parser.add_argument(
        '--key', default='dc8f758149be1e05fec938b7e1aa829f06308ffe1')
    parser.add_argument('--secret', default='cb508033fe4c5ddd9744b1aa82589a98')
    parser.add_argument('-s', '--source', default='en')
    parser.add_argument('-t', '--target', default='ja')
    parser.add_argument('text')
    args = parser.parse_args()

    url = f'https://mt-auto-minhon-mlt.ucri.jgn-x.jp/api/mt/generalNT_{args.source}_{args.target}/'
    data = {
        'key': args.key,
        'name': args.name,
        'text': args.text,
        'type': 'json'
    }
    r = requests.post(url, data=data, auth=OAuth1(
        args.key, args.secret)).json()
    print(r['resultset']['result']['text'])


if __name__ == '__main__':
    trans()
