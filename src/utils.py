import json
from datetime import datetime
from operator import itemgetter


def open_data(path):

    """"Достаем данные из json"""
    with open(path, "r", encoding="utf-8") as file:
        list_json = json.load(file)
        return list_json


def get_executed_operation(data):
    """
     Фильтрует данные с добавлением в список выполненные операции
    """
    executed_list = []

    for key in data:
        if key.get('state') == 'EXECUTED':
            executed_list.append(key)
    return (executed_list)


# out_filter = filter(get_executed_operation, new_list)

def sort_operations_by_date(data):
    """
    сортировка  по дате в порядке возрастания
    """
    data = [trans for trans in data if trans]
    data_new = sorted(data, key=itemgetter("date"))
    return data_new


def quantity_sort_operations_by_date(list, last_count):
    """
    вывод последних пять выполненных операций
    """
    five_sort = list[-last_count:]
    # res = ' '.join(reversed(five_sort))
    return five_sort


def format_date(date):
    """
     принимает значение ключа 'date' и форматирует дату в нужный формат для вывода
    """
    dt = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return (dt.strftime('%d.%m.%Y'))


def account_mask(account):
    """
    значение ключа 'from' в виде строки, если в строке есть слово Счет то делает модификатор строки счета
    иначе делает модификатор строки под карты
    """
    if len(account) == 0:
        return account
    if 'Счет' in account:
        check = "".join([account[:-20], '**', account[-4:]])
        return check
    else:
        check_card = " ".join([account[:-12], '**', '****', account[-4:]])
        return check_card
