import requests
import random
import json

# Определение функции для фильтрации аниме
def filter_anime(year=None, score=None):
    url = "https://api.jikan.moe/v4/anime"
    params = {}

    # Установка параметров фильтрации, если они заданы
    if year:
        start_date = f"{year}-01-01"
        params['start_date'] = start_date
    if score:
        params['min_score'] = score

    # Получение списка аниме с заданными параметрами
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()


        # Запись JSON-данных в файл для отладки
        with open('response_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        anime_list = data.get('data', [])

        if not anime_list:
            print("No anime found with the given filters.")
            return None

        # Выбор случайного аниме из списка
        random_anime = random.choice(anime_list)
        return random_anime

    else:
        print(f"Error: {response.status_code}")
        return None

# Получение ввода от пользователя
print('Выберете год (необязательно): ')
year = str(input())
print('Выберете минимальную оценку (необязательно) : ')
score = input()

# Поиск аниме
anime = filter_anime(year=year if year else None, score=score if score else None)

if anime:
    print(f"Title: {anime.get('title')}")
    print(f"Year: {anime.get('year')}")
    print(f"Score: {anime.get('score')}")
    print(f"URL: {anime.get('url')}")
