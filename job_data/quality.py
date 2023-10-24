import pandas as pd
from pandas import DataFrame,Timestamp

def check_nulls(df: DataFrame, columna: str) -> bool:
    if columna not in df.columns:
        raise ValueError(f'La columna "{columna}" no existe en el DataFrame.')
    return df[columna].isnull().any()

#Comprobar si el df esta vacio
def df_is_empty(df: DataFrame) -> bool:
    return df.empty

def validar_fecha(df: DataFrame, nombre_de_campo: str) -> str:
    values = df[nombre_de_campo]
    
    if values.isnull().all():
        return 'KO'
    
    if all(isinstance(value, Timestamp) for value in values):
        return 'OK'
    
    return 'KO'