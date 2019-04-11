import requests

OFFICES = ['Kazan', 'Moscow', 'Samara']
URL_TEMPLATE = 'http://wttr.in/{}'
PARAMS = {
    'lang': 'ru',
    'n': '',
    'T': '',
    'q': '',
    'm': ''
}


def get_weather(office=None):
    if office:
        url = URL_TEMPLATE.format(office)
        req = requests.get(url, params=PARAMS)
        print(req.text)
    else:
        for office in OFFICES:
            url = URL_TEMPLATE.format(office)
            req = requests.get(url, params=PARAMS)
            print(req.text)


if __name__ == '__main__':
    get_weather()
