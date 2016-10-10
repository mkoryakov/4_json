import json
import argparse


def load_data(filepath):
    with open(filepath) as json_handler:
        data = json.load(json_handler)
    return data


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Удобный для чтения вывод информации в формате json')
    parser.add_argument('--json_file_name', '-jfn', type=str, 
                            default='bars.json', help='Имя файла json')
    args = parser.parse_args()
    data = load_data(args.json_file_name)
    pretty_print_json(data)
