import pandas
import json

df_provincias = pandas.read_csv('data\provincias_info_2023-09-24.csv', sep=';')
df = pandas.read_csv('data\empleos_info_2023-09-24.csv', sep=';')

provincias = df_provincias['provincia'].to_list()

for provincia in provincias:
    print(
        df_provincias[df_provincias['provincia']
                      == provincia]['num_ofertas'].values[0],
        df[df['provincia'] == provincia].shape[0],
        df_provincias[df_provincias['provincia'] ==
                      provincia]['num_ofertas'].values[0] == df[df['provincia'] == provincia].shape[0]
    )


with open(file='data/provincia_info.json', mode='r', encoding='utf-8') as f:
  data = json.load(f)
  
for provincia in data['provincias']:
   print(provincia['name'], provincia['id'])