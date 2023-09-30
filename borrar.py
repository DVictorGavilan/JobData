import json
import pandas


def count_repeated_values(lista: list) -> dict:
    """ Devuelve un diccionario con la siguiente estructura:
        elemento_de_la_lista: n_repeticiones_del_elemento """
    return {i: lista.count(i) for i in set(lista)}


def print_pretty_dict(dictionary: dict) -> None:
    print(json.dumps(dictionary, indent=4))


def normalized_technology_name(raw_name: str) -> str:
    if raw_name in ['python', 'pyhton']:
        return 'Python'
    elif raw_name in ['javascript', 'javascri', 'javacrip', 'javascrip', 'js']:
        return 'JavaScript'
    elif raw_name in ['angular', 'angularjs', 'angular js', 'angular front end']:
        return 'Angular'
    elif raw_name in ['react', 'reactjs', 'react js', 'react.js']:
        return 'React'
    elif raw_name in ['react native']:
        return 'React Native'
    elif raw_name in ['nextjs', 'next js', 'nuxt.js']:
        return 'NextJS'
    elif raw_name in ['node', 'nodejs', 'node js', 'node.js']:
        return 'NodeJS'
    elif raw_name in ['vue', 'vuejs', 'vue js', 'vue.js']:
        return 'VueJS'
    elif raw_name in ['typescript']:
        return 'TypeScript'
    elif raw_name in ['java']:
        return 'Java'
    elif raw_name in ['spring', 'java spring']:
        return 'Spring'
    elif raw_name in ['springboot', 'spring boot']:
        return 'SpringBoot'
    elif raw_name in ['php']:
        return 'PHP'
    elif raw_name in ['laravel']:
        return 'Laravel'
    elif raw_name in ['c#']:
        return 'C#'
    elif raw_name in ['kotlin', 'kotling']:
        return 'Kotlin'
    elif raw_name in ['net', '.net', 'visual studio.net']:
        return '.Net'
    elif raw_name in ['aws']:
        return 'AWS'
    elif raw_name in ['azure']:
        return 'Azure'
    elif raw_name in ['gcp', 'google cloud', 'google cloud platform']:
        return 'GCP'
    elif raw_name in ['sql']:
        return 'SQL'
    elif raw_name in ['mysql']:
        return 'MySQL'
    elif raw_name in ['PostgreSQL', 'postgres']:
        return 'PostgreSQL'
    elif raw_name in ['oracle']:
        return 'Oracle'
    elif raw_name in ['sql server']:
        return 'SQL Server'
    elif raw_name in ['sap']:
        return 'SAP'
    elif raw_name in ['sap s4']:
        return 'SAP S/4HANA'
    elif raw_name in ['docker', 'docke']:
        return 'Docker'
    else:
        return raw_name


df = pandas.read_csv('data\empleos_info_2023-09-30.csv', sep=';')

technologies_raw = [
    technology.lower() for technologies in df['tecnologias'].to_list()
    for technology in technologies.split(' - ')
]


technologies = [normalized_technology_name(
    technology) for technology in technologies_raw]

for tech, n in count_repeated_values(technologies).items():
    if 'visual' in tech:
        print(tech, n)

print(len(set(technologies_raw)))
print(len(set(technologies)))
