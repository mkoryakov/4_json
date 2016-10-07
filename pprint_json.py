import json
import argparse


def load_data(filepath):
    with open(filepath) as jsonObj:
        data = json.load(jsonObj)
    return data


def pretty_print_json(data):
    for d in data:
        print(json.dumps(data, ensure_ascii=False, indent=4))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Удобный для чтения вывод информации в формате json')
    parser.add_argument('--json_file_name', '-jsf', type=str, 
                            default='bars.json', help='Имя файла json')
    args = parser.parse_args()
    data = load_data(args.json_file_name)
    pretty_print_json(data)
