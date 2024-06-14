import datetime
import xml.etree.ElementTree as ET

import requests

""" Задание 1 (парсинг)
Напишите скрипт, который будет производить сбор данных с выбранной вами
страницы на сайте ЦБ РФ либо осуществлять загрузку xsl, xslx, pdf, csv или иного
файла с данными в рабочую директорию с последующим его парсингом.
У класса должен быть только один публичный метод start(). Все остальные методы,
содержащие логику по выгрузке и сохранению данных, должны быть приватными.
Определите структуру для хранения. Для ключевой ставки ЦБ РФ это может быть
словарь (dict), где ключом будет выступать дата, а значением — размер ключевой
ставки на указанную дату.
 """


class ParserCBRF:

    def start(self):
        file_name = self.__make_a_req(datetime.datetime.today())
        return self.__read_xml(file_name)

    def __make_a_req(sellf, date):
        today = date.strftime('%d/%m/%Y')
        params = {'date_req': today}
        request = requests.get('https://www.cbr.ru/scripts/XML_daily.asp?', params=params)

        file_name = 'cb.xml'
        with open(file_name, 'wb') as f:
            f.write(request.content)
        return file_name

    def __read_xml(self, file_name):
        tree = ET.parse(file_name)
        root = tree.getroot()

        dictionary = dict()
        currency_name = ''
        currency_value = 0

        for elem in root.iter():
            if elem.tag == 'Name':
                currency_name = elem.text

            if elem.tag == 'Value':
                currency_value = elem.text
                dictionary[currency_name] = currency_value

        return dictionary


if __name__ == "__main__":
    parser = ParserCBRF()
    print(parser.start())
