from abc import ABC, abstractmethod
from connector import Connector
import requests


class Engine(ABC):
    _key_word = 'python'
    _per_page = 20
    _vacancies_count = 100

    @abstractmethod
    def get_request(self):
        """
        Реализвация взаимодействия с API (определяется в каждом классе)
        """
        pass

    @staticmethod
    def get_connector(file_name: str):
        """
        Возвращает экземпляр класса Connector
        """
        connector = Connector()
        connector.data_file = file_name
        return connector

    @property
    def key_word(self):
        return self._key_word

    @key_word.setter
    def key_word(self, key_word):
        self._key_word = key_word

    @property
    def per_page(self):
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        self._per_page = per_page

    @property
    def vacancies_count(self):
        return self._vacancies_count

    @vacancies_count.setter
    def vacancies_count(self, vacancies_count):
        self._vacancies_count = vacancies_count

    def helper_func_request(self, url: str, headers: dict, get_vacancies: str):
        """
        Вспомогательный метод для взаимодействия с API,
        создает файл с данными по N вакансий (количество определяется параметром - vacancies_count, ключевое слово - key_word)
        """
        page = 1
        result = []
        # response = requests.get(url=url + f'&page={page}', headers=headers)
        # if response.status_code == 200:
        #     json_file = response.json()
        #     if json_file.get('found') < self.vacancies_count:
        #         self.vacancies_count = json_file.get('found')
        while self.per_page * page <= self.vacancies_count:
            response = requests.get(url=url + f'&page={page}', headers=headers)
            if response.status_code == 200:
                json_file = response.json()
                result += json_file.get(get_vacancies)
                print('Страница: ', page)
                page += 1
        create_file = self.get_connector(self.json_file_name)
        create_file.insert(result)
        return len(result)


class HH(Engine):
    """
    Класс дополняет функциональность родительской функции helper_func_request под
    параметры площадки hh.ru
    """

    __url = 'https://api.hh.ru/vacancies'
    json_file_name = 'hh_vacancies.json'

    def get_request(self):
        url = f'{self.__url}?text={self.key_word}'
        headers = {}
        get_vacancies = 'items'
        return f'В файл {self.json_file_name} записано {self.helper_func_request(url, headers, get_vacancies)} вакансий'


class Superjob(Engine):
    """
    Класс дополняет функциональность родительской функции helper_func_request под
    параметры площадки hh.ru
     """

    __url = 'https://api.superjob.ru/2.0/vacancies'
    __key = 'v3.r.137229459.1330497a7378b4af7fae677f8ae08af64403cb2c.eb3c90a837615680d558721cc148022ea5aaa98b'
    json_file_name = 'sj_vacancies.json'

    def get_request(self):
        url = f'{self.__url}?keyword={self.key_word}'
        headers = {'X-Api-App-Id': self.__key,
                   'Authorization': 'Bearer r.000000010000001.example.access_token',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        get_vacancies = 'objects'
        return f'В файл {self.json_file_name} записано {self.helper_func_request(url, headers, get_vacancies)} вакансий'


if __name__ == '__main__':
    hh = HH()
    sj = Superjob()
    print(hh.get_request())
    print(sj.get_request())
