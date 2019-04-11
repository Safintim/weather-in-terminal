import requests
import argparse


OFFICES = ['Kazan', 'Moscow', 'Samara']
URL_TEMPLATE = 'http://wttr.in/{}'
PARAMS = {
    'lang': 'ru',
    'n': '',
    'T': '',
    'q': '',
    'm': ''
}


def get_weather():
    for office in OFFICES:
        url = URL_TEMPLATE.format(office)
        req = requests.get(url, params=PARAMS)
        print(req.text)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--city', nargs='+', default=['Kazan'])
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    OFFICES = namespace.city
    get_weather()

