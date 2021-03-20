import json
from string import ascii_letters


with open('parser_result.json', 'r', encoding='utf-8') as f:
    animals = json.load(f)


# что бы было меньше путаницы с результами будем брать в расчет только животных с русскими именами
result_dict = {}
for animal in animals:
    if animal[0] in ascii_letters:
        continue
    try:
        result_dict[animal[0]] += 1
    except KeyError:
        result_dict[animal[0]] = 1


# Сделаем сортировку 
keys = [key for key in result_dict.keys()]
keys.sort()
sorted_result_dict = {key: result_dict[key] for key in keys}


with open('final_result.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_result_dict, f, ensure_ascii=False, indent=4)