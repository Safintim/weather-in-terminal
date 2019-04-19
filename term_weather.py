import requests
import argparse


def get_weather(url_template, params, offices):
    for office in offices:
        url = url_template.format(office)
        req = requests.get(url, params=params)
        print(req.text)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('city', nargs='+')
    return parser


def main():
    url_template = 'http://wttr.in/{}'
    params = {
        'lang': 'ru',
        'n': '',
        'T': '',
        'q': '',
        'm': ''
    }

    parser = create_parser()
    namespace = parser.parse_args()
    offices = namespace.city
    get_weather(url_template, params, offices)


if __name__ == '__main__':
    main()
