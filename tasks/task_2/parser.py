import requests
import json

from bs4 import BeautifulSoup


base_url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'


def parse_page(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'lxml')
    divs = soup.find_all('div', class_='mw-category-group')
    ul = []
    for div in divs:
        ul += div.find_all('li')
    animals = [li.text for li in ul]

    return animals


def pars_all_pages():
    animals = parse_page(base_url)
    last_iteration_last_animal_name = ''
    while True:
        last_animal_name = animals[-1]

        # Проверка на повторение
        if last_iteration_last_animal_name == last_animal_name:
            break
        else:
            last_iteration_last_animal_name = last_animal_name
        
        last_animal_name = last_animal_name.replace(' ', '+').replace('+(', '%20(')
        url = f'{base_url}&pagefrom={last_animal_name}'
        animals += parse_page(url)

    return list(set(animals))


def save_pars_results_to_json(file_name='parser_result.json'):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(pars_all_pages(), f, ensure_ascii=False, indent=4)

save_pars_results_to_json()