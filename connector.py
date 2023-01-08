import json


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        """
        try:
            with open(self.__data_file, 'r', encoding='utf-8') as open_file:
                json.load(open_file)
        except:
            with open(self.__data_file, 'w+', encoding='utf-8') as open_fil:
                json.dump('[]', open_fil)

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__data_file, 'w', encoding='utf-8') as open_file:
            try:
                file = json.load(open_file)
                file.append(data)
                json.dump(file, open_file)
            except:
                file = [data]
                json.dump(file, open_file)

    def read_file(self):
        with open(self.__data_file, 'r', encoding='utf-8') as open_file:
            file = json.load(open_file)
            return file

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        with open(self.__data_file, 'r', encoding='utf-8') as open_file:
            file = json.load(open_file)
            key = list(query.keys())
            if len(key) == 0:
                new_file = []
                return new_file
            new_file = [x for x in file if x[key[0]] == query[key[0]]]
            return new_file

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        write_data = []
        with open(self.__data_file, 'r', encoding='utf-8') as open_file:
            file = json.load(open_file)
            if len(query) != 0:
                for i in file:
                    if i[list(query.keys())[0]] != query[list(query.keys())[0]]:
                        write_data.append(i)
            else:
                write_data = file
        with open(self.__data_file, 'w', encoding='utf-8') as write_file:
            json.dump(write_data, write_file)


if __name__ == '__main__':
    df = Connector()
    df.data_file = 'df.json'

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)

    data_from_file = df.select({'id': 1})
    assert data_from_file == [data_for_file]

    df.delete({'id': 1})
    data_from_file = df.select(dict())
    assert data_from_file == []
