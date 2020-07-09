import json


def read_json(filename):
    filepath = '../data/' + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == '__main__':
    datas = read_json('calc.json')
    arrs = []
    for data in datas.values():
        arrs.append((data['num1'], data['num2'], data['expect']))
    print(arrs)