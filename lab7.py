import requests
import json



def pages():
    next_page = 'https://rickandmortyapi.com/api/character'
    pages_list = []
    for i in range(42):
        response = requests.get(next_page)
        response = response.json()
        next_page = response['info']['next']
        [pages_list.append(response['results'][i]) for i in range(len(response['results']))]
    return pages_list


def search(character=str):
    PARAM_LIST = ['id', 'name', 'status', 'species', 'type', 'gender', 'image']
    KEY_RY = {'id':'id', 'name':'Имя', 'status':'Статус', 'species':'Вид', 
              'type':'Тип (при наличии)', 'gender':'Гендер', 'image':'Ссылка на изображение'}

    flag = 0
    for j in range(len(PAGES_LIST)):
        if PAGES_LIST[j]['name'] == character:
            flag = 1
            for key in PARAM_LIST:
                print(f'{KEY_RY[key]}: {PAGES_LIST[j][key]}')
            print()
        elif flag == 1:
            flag == -1
            break
    print("===================That's all====================\n")


CHARACTERS = ['Baby Legs', 'Beth Smith', 'Abradolf Lincler']
PAGES_LIST = pages()


for character in CHARACTERS:
    search(character)


# ['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'image', 'episode', 'url', 'created']