import json

'''
person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}
'''


def load_json(path_to_file):
    with open(path_to_file, encoding='utf8') as f:
        data = json.load(f)
    return data


def write_json(path_to_file, data):
    with open(path_to_file, 'w', encoding='utf8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
