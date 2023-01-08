from user_interaction import *
from utils import *

if __name__ == '__main__':
    file_lst = find_file()
    data = []
    if len(file_lst) > 1:
        while True:
            site_selection = input(
                '1. hh.ru\n2. superjob.ru\nВведите номер сайта, вакансии которого хотите вывести: [1] ')

            if site_selection == '1' or site_selection == '':
                print(
                    f'В файле найдено {HHVacancy("name", "url", "description_vacancy", "salary_vacancy", "company_name").get_count_of_vacancy} вакансий')
                data = init_hh_vacancy_class()
                break
            elif site_selection == '2':
                print(
                    f'В файле найдено {SJVacancy("name", "url", "description_vacancy", "salary_vacancy", "company_name").get_count_of_vacancy} вакансий')
                data = init_sj_vacancy_class()
                break
            else:
                print('Введен некорректный номер')
    elif len(file_lst) == 1:
        if file_lst[0] == 1:
            print(
                f'В файле найдено {HHVacancy("name", "url", "description_vacancy", "salary_vacancy", "company_name").get_count_of_vacancy} вакансий')
            data = init_hh_vacancy_class()
        else:
            print(
                f'В файле найдено {SJVacancy("name", "url", "description_vacancy", "salary_vacancy", "company_name").get_count_of_vacancy} вакансий')
            data = init_sj_vacancy_class()
    else:
        data = creating_files()

    inp_sort = input('Хотите отфильтровать вакансии по ЗП? [Д/н] ')
    if inp_sort.lower() == 'д' or inp_sort.lower() == '' or inp_sort.lower() == 'да':
        sort_data = sorting(data)
    else:
        sort_data = data

    count = 0
    while True:
        count_vacancies = input('Введите количество вакансий для вывода в терминал: ')
        if count_vacancies.isdigit():
            count = int(count_vacancies)
            break
        else:
            print('Необходимо ввести целое число')

    get_top(sort_data, count)
