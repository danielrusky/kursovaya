import json
from datetime import datetime


def read_file():
    with open('operations.json', 'r') as file:
        return json.load(file)

def five_operations(data):
    data_ = []
    for i in data:
        try:
            i['date'] = datetime(i['date'])
            if i['state'] == 'EXECUTED':
                data_.append(i)
        except KeyError:
            continue
    return sorted(data_, key=lambda x: x['date']).reverse()[:5]


def print_operation(operation):
    '''
    14.10.2018 Перевод организации
    Visa Platinum 7000 79** **** 6361 -> Счет **9638
    82771.72 руб.
    :param operation:
    :return:
    '''
    acc_from = operation["from"].split(' ')[-1]
    acc_to = operation["to"].split(' ')[-1]
    print(f'{operation["date"].strftime("%m.%d.%Y")} {operation["description"]}\n'
          f'{operation["from"].replase(acc_from, "")} {acc_from[:6]}** ****{acc_from[-5:]} ->'
          f'{operation["to"].replase(acc_to, "")} **{acc_to[-5:]}\n'
          f'{operation["operationAmount"]["amount"]} ')




