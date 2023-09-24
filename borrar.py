import pandas

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
