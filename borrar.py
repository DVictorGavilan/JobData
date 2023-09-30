import json
import pandas


def count_repeated_values(lista: list) -> dict:
    """ Devuelve un diccionario con la siguiente estructura:
        elemento_de_la_lista: n_repeticiones_del_elemento """
    return {i: lista.count(i) for i in set(lista)}


def print_pretty_dict(dictionary: dict) -> None:
    print(json.dumps(dictionary, indent=4))


def normalized_technology_name(raw_name: str) -> str:
    if raw_name in ['python', 'pyhton', 'phyton']:
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
    elif raw_name in ['springboot', 'spring boot', 'springboot.']:
        return 'SpringBoot'
    elif raw_name in ['php']:
        return 'PHP'
    elif raw_name in ['laravel']:
        return 'Laravel'
    elif raw_name in ['c#']:
        return 'C#'
    elif raw_name in ['html', 'html5']:
        return 'HTML'
    elif raw_name in ['css', 'css3']:
        return 'CSS'
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
    elif raw_name in ['pl/sql', 'plsql']:
        return 'PL/SQL'
    elif raw_name in ['mysql']:
        return 'MySQL'
    elif raw_name in ['PostgreSQL', 'postgres']:
        return 'PostgreSQL'
    elif raw_name in ['oracle']:
        return 'Oracle'
    elif raw_name in ['sql server', 'sqlserver']:
        return 'SQL Server'
    elif raw_name in ['datalake', 'data lake', 'datalakes']:
        return 'Data Lake'
    elif raw_name in ['sap']:
        return 'SAP'
    elif raw_name in ['sap s4']:
        return 'SAP S/4HANA'
    elif raw_name in ['docker', 'docke', 'dockers']:
        return 'Docker'
    elif raw_name in ['powerbi']:
        return 'PowerBI'
    elif raw_name in ['tableau']:
        return 'Tableau'
    elif raw_name in ['datastudio', 'data studio']:
        return 'Data Studio'
    elif raw_name in ['databricks', 'data bricks']:
        return 'DataBricks'
    elif raw_name in ['data science', 'data scientist']:
        return 'Data Science'
    elif raw_name in ['data analytics']:
        return 'Data Analytics'
    elif raw_name in ['data governance']:
        return 'Data Governance'
    elif raw_name in ['data visualization']:
        return 'Data Visualization'
    elif raw_name in ['microsoft', 'microsoft 365', 'microsoft office', 'microsoft office 365']:
        return 'Microsoft 365'
    elif raw_name in ['excel', 'microsoft excel']:
        return 'Microsoft Excel'
    elif raw_name in ['word']:
        return 'Microsoft Word'
    elif raw_name in ['access', 'microsoft access']:
        return 'Microsoft Access'
    elif raw_name in ['microsoft d365', 'microsoft dynamics', 'microsoft dynamics 365', 'm365']:
        return 'Microsoft Dynamics'
    elif raw_name in ['microsoft teams']:
        return 'Microsoft Teams'
    elif raw_name in ['microservices', 'microservicios']:
        return 'Microservicios'
    elif raw_name in ['microiformatica', 'microinformatica', 'microinformática']:
        return 'Microinformática'
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

pandas.DataFrame({'Technology': sorted(list(set(technologies)))}).to_csv(
    'data/technologies_raw.csv', index=False)
