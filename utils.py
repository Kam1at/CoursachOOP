from jobs_classes import *
import json


def sorting(vacancies: list):
    """
    Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods)
    """
    return sorted(vacancies, reverse=True)


def get_top(vacancies: list, top_count: int):
    """
    Должен возвращать {top_count} записей из вакансий по зарплате
    """
    count = 0
    for vacancy in vacancies:
        if count >= top_count:
            break
        count += 1
        print(vacancy, end='\n\n')


def init_hh_vacancy_class():
    """
    Считывает данные из файла hh_vacancies.json, с вакансиями сайта hh.ru и добавляет ссылки на экземпляры
    класса HHVacancy со следующими данными: название кампании и вакансии, ссылка на вакансию, ЗП и описание в
    список HHVacancy.data
    """
    with open('hh_vacancies.json', 'r', encoding='utf-8') as file:
        file_read = json.load(file)
        for vacancy in file_read[0]:
            url = vacancy.get('alternate_url')
            name = vacancy.get('name')
            try:
                description = vacancy['snippet'].get('requirement') + ' ' + vacancy['snippet'].get('responsibility')
            except:
                description = None
            try:
                if vacancy['salary'].get('from'):
                    salary = vacancy['salary'].get('from')
                elif vacancy['salary'].get('to'):
                    salary = vacancy['salary'].get('to')
                if vacancy['salary'].get("currency") == 'USD':
                    salary *= 72
                elif vacancy['salary'].get("currency") == 'EUR':
                    salary *= 77
                elif vacancy['salary'].get("currency") == 'KZT':
                    salary *= 0.15
            except:
                salary = 0

            try:
                company_name = vacancy['employer'].get('name')
            except:
                company_name = None
            HHVacancy.data.append(HHVacancy(name, url, description, salary, company_name))
        return HHVacancy.data


def init_sj_vacancy_class():
    """
    Считывает данные из файла sj_vacancies.json, с вакансиями сайта sj.ru и добавляет ссылки на экземпляры
    класса SJVacancy со следующими данными: название кампании и вакансии, ссылка на вакансию, ЗП и описание в
    список SJVacancy.data
    """
    with open('sj_vacancies.json', 'r', encoding='utf-8') as file:
        file_read = json.load(file)
        for vacancy in file_read[0]:
            url = vacancy.get('link')
            name = vacancy.get('profession')
            try:
                description = vacancy.get('candidat')
            except:
                description = None
            try:
                if vacancy.get('payment_from'):
                    salary = vacancy.get('payment_from')
                elif vacancy.get('payment_to'):
                    salary = vacancy.get('payment_to')
            except:
                salary = 0

            try:
                company_name = vacancy.get('firm_name')
            except:
                company_name = None
            SJVacancy.data.append(SJVacancy(name, url, description, salary, company_name))
        return SJVacancy.data
