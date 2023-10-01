import json
import pandas


def count_repeated_values(lista: list) -> dict:
    """ Devuelve un diccionario con la siguiente estructura:
        elemento_de_la_lista: n_repeticiones_del_elemento """
    return {i: lista.count(i) for i in set(lista)}


def print_pretty_dict(dictionary: dict) -> None:
    print(json.dumps(dictionary, indent=4))


def read_json(path: str) -> dict:
    with open(file=path, mode='r', encoding='utf-8') as f:
        return json.load(f)


def normalized_technology_name(raw_name: str, normal: dict) -> str:
    if raw_name in normal.keys():
        return normal[raw_name]
    else:
        return raw_name


df = pandas.read_csv('data\empleos_info_2023-09-30.csv', sep=';')
normalize = read_json('config/normalized_names.json')

technologies_raw = [
    technology.lower() for technologies in df['tecnologias'].to_list()
    for technology in technologies.split(' - ')
]


technologies = [normalized_technology_name(
    technology, normalize) for technology in technologies_raw]

count_values = count_repeated_values(technologies)
for tech, n in count_values.items():
    if 1000 < n:
        print(tech, n)

print(len(set(technologies_raw)))
print(len(set(technologies)))

pandas.DataFrame({'Technology': count_values.keys(), 'Count': count_values.values()}).to_csv(
    'data/technologies_raw.csv', index=False)

# 1176
# 1129
# 1105
# 1077
# 1072
