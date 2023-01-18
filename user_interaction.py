from engine_classes import *
from utils import *
import os.path


def creating_files():
    while True:
        site_selection = input('1. hh.ru\n2. superjob.ru\nВведите номер сайта, вакансии которого хотите найти: [1] ')

        if site_selection == '1' or site_selection == '':
            area = HH
            break
        elif site_selection == '2':
            area = Superjob
            break
        else:
            print('Введен некорректный номер')

    keyword = input('Введите ключевое слово для поиска: [python] ').lower()
    if keyword == '':
        area.key_word = 'python'
    else:
        area.key_word = keyword

    while True:
        number_of_vacancies = input('Введите количество вакансий для записи в файл: [100] ')
        if number_of_vacancies == '':
            area.vacancies_count = 100
            break
        else:
            if number_of_vacancies.isdigit():
                area.vacancies_count = int(number_of_vacancies)
                break
            else:
                print('Введены некорректные данные. Повторите ввод.')

    if area == HH:
        print(area().get_request())
        return init_hh_vacancy_class()
    elif area == Superjob:
        print(area().get_request())
        return init_sj_vacancy_class()


def find_file():
    find = ''
    answer = []
    if os.path.exists('sj_vacancies.json'):
        find += 'Найден файл sj_vacancies.json'
        answer.append(2)
    if os.path.exists('hh_vacancies.json'):
        if find == '':
            find += 'Найден файл hh_vacancies.json'
        else:
            find += ' и hh_vacancies.json'
        answer.append(1)
    if find:
        inp = input(f'{find}. Хотите продолжить работу с ними? [Д/н] ')
        if inp.lower() == 'д' or inp.lower() == '' or inp.lower() == 'да':
            return answer
    return []
