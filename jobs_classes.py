from connector import Connector


class Vacancy:
    start = 0
    __slots__ = ('name_vacancy', 'url_vacancy', 'description_vacancy', 'salary_vacancy')

    def __init__(self, name_vacancy: str, url_vacancy: str, description_vacancy: str, salary_vacancy: str):
        self.name_vacancy = name_vacancy
        self.url_vacancy = url_vacancy
        self.description_vacancy = description_vacancy
        self.salary_vacancy = salary_vacancy

    def __lt__(self, other):
        return self.salary_vacancy < other.salary_vacancy

    def __gt__(self, other):
        return self.salary_vacancy > other.salary_vacancy

    def __eq__(self, other):
        return self.salary_vacancy == other.salary_vacancy

    def __str__(self):
        return f'{self.name_vacancy} | ссылка на вакансию - {self.url_vacancy} | описание: {self.description_vacancy} | ЗП: {self.salary_vacancy} руб/мес'

    def __repr__(self):
        return f'{self.name_vacancy} | ссылка на вакансию - {self.url_vacancy} | описание: {self.description_vacancy} | ЗП: {self.salary_vacancy} руб/мес'

    def __iter__(self):
        self.value = -1
        return self

    def __next__(self):
        if self.value + 1 < len(self.data):
            self.value += 1
            return self.data[self.value]
        else:
            raise StopIteration


class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        connector = Connector()
        connector.data_file = self.json_file_name
        return len(connector.read_file()[0])


class HHVacancy(Vacancy, CountMixin):
    """
    HeadHunter Vacancy
    """
    json_file_name = 'hh_vacancies.json'
    data = []

    def __init__(self, name_vacancy: str, url_vacancy: str, description_vacancy: str, salary_vacancy: str,
                 company_name: str):
        super().__init__(name_vacancy, url_vacancy, description_vacancy, salary_vacancy)
        self.company_name = company_name

    def __str__(self):
        return f'HH | {self.company_name} | ' + super().__str__()


class SJVacancy(Vacancy, CountMixin):
    """
    SuperJob Vacancy
    """
    json_file_name = 'sj_vacancies.json'
    data = []

    def __init__(self, name_vacancy: str, url_vacancy: str, description_vacancy: str, salary_vacancy: str,
                 company_name: str):
        super().__init__(name_vacancy, url_vacancy, description_vacancy, salary_vacancy)
        self.company_name = company_name

    def __str__(self):
        return f'SJ | {self.company_name} | ' + super().__str__()
