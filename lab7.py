import requests
import json



def pages(next_page):
    pages_list = []
    for i in range(42):
        response = requests.get(next_page)
        response = response.json()
        next_page = response['info']['next']
        [pages_list.append(response['results'][i]) for i in range(len(response['results']))]
    return pages_list


def search(character=str, mode=1):
    if mode == 0:    
        response = requests.get(f'https://rickandmortyapi.com/api/character/?name={character}')
        response = response.json()
        for j in range(len(response['results'])):
            for key in PARAM_LIST:
                print(f'{KEY_RY[key]}: {response['results'][j][key]}')
            print()
    else:
        for j in range(len(pages_list)):
            if pages_list[j]['name'] == character:
                for key in PARAM_LIST:
                    print(f'{KEY_RY[key]}: {pages_list[j][key]}')
                print()
    print("===================That's all====================\n")
    

CHARACTERS = ['Baby Legs', 'Beth Smith', 'Abradolf Lincler']
PARAM_LIST = ['id', 'name', 'status', 'species', 'type', 'gender', 'image']
KEY_RY = {'id':'id', 'name':'Имя', 'status':'Статус', 'species':'Вид', 
          'type':'Тип (при наличии)', 'gender':'Гендер', 'image':'Ссылка на изображение'}



if __name__ == '__main__':
    mode = 1 # режим работы - быстрый-0 или расширенный-1
    if mode == 1:
        pages_list = pages('https://rickandmortyapi.com/api/character')

    for character in CHARACTERS:
        search(character, mode)