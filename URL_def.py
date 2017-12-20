# Галкин Антон 
# Задание - На основе кода с выполнением предыдущего задания (см. тему 18) 
# реализуйте получение JSON с удаленного хоста и красивый вывод информации на экран (через функцию). 

from urllib.request import urlopen 
import pprint
import json


def hacker_man(id):   # на вход подаём цифру-id пользователя на выходе имеем некоторые основные данные (возможен вывод большего числа данных)
    inquiry = "https://api.vk.com/method/users.get?user_ids={id}&fields=education&v=5.69".format(id = id)

    try:
        inquiry_obj = urlopen(inquiry)
        obj = json.loads(inquiry_obj.read())
    except:
        print('Ошибка')
    return obj


if __name__ == "__main__":
    id = input(' Введите id: \n')
    print('Ответ сервера: \n')
    pprint.pprint(hacker_man(id))
