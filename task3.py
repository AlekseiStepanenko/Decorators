import datetime
import requests


def logger(old_function):

    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        name = old_function.__name__
        key = f'{args}, {kwargs}'
        result = old_function(*args, **kwargs)
        with open('main2.log', 'a', encoding='utf-8') as f:
            f.write(f'Время вызова функции - {start}, '
                    f'имя функции - {name}, '
                    f'аргументы функции - {key}, '
                    f'значение функции - {result}')
        return result

    return new_function


@logger
def hero(url):
    # url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    if response.status_code > 200:
        print(f'Запрос не успешный')
    if response.status_code == 200:
            # pprint(response.json())
        list_superhero = response.json()
        dict_intelligence = {}
        for hero in list_superhero:
            if hero['name'] == 'Hulk' or hero['name'] == 'Captain America' or hero['name'] == 'Thanos':
                dict_intelligence[hero['name']] = hero['powerstats']['intelligence']

        return (f'Самый умный супергерой - {max(dict_intelligence)}')


result = hero('https://akabab.github.io/superhero-api/api/all.json')
print(result)