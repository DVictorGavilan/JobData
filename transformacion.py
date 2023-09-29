import pandas as pd
# Ejemplo con punto y coma como delimitador
data_job = pd.read_csv('/content/drive/MyDrive/ProyectoX/empleos_info_2023-09-24.csv', sep=';')
data_job
# Crea una copia del DataFrame para mantener el original intacto
data_job_copia = data_job.copy()

# Aplica strip() a la columna "descripcion" de la copia para eliminar espacios en blanco al principio y al final
data_job_copia['descripcion'] = data_job_copia['descripcion'].str.strip()

# Si deseas verificar los cambios en la copia
print(data_job_copia.head(2))

# Extraer los primeros diez caracteres de la columna "descripcion" y convertirlos a tipo datetime
data_job_copia['fecha_publicacion'] = pd.to_datetime(data_job_copia['descripcion'].str[:10], format='%d/%m/%Y')

# Si deseas verificar los cambios
print(data_job_copia.head())
print(data_job_copia['fecha_publicacion'].dtype)
import re

# Función para dividir palabras combinadas
def separar_palabras_combinadas(texto):
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', texto)

# Aplicar la función a la columna "descripcion"
data_job_copia['descripcion'] = data_job_copia['descripcion'].apply(separar_palabras_combinadas)

# Verificar los cambios
data_job_copia