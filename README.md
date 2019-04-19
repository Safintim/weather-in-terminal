# weather-in-terminal
Консольная программа, которая дает прогноз погоды на три дня.

Использует сервис http://wttr.in/

## Требования

Для запуска программы требуется:

1. Python 3.6
2. Terminal

## Как установить:

1. Установить Python3:

(Windows):[python.org/downloads](https://www.python.org/downloads/windows/)

(Debian):
```sh
sudo apt-get install python3
sudo apt-get install python3-pip
```
2. Установить зависимости и скачать сам проект:

```sh
git clone https://github.com/Safintim/weather-in-terminal.git
pip3 install -r requirements.txt
```

## Как использовать: 
***
```sh
python3 term_weather.py Moscow
python3 term_weather.py Moscow Samara Kazan
```

Пример:
![Alt Text](http://ipic.su/img/img7/fs/weather.1555669725.gif)