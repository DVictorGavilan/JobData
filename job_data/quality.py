import pandas as pd
from pandas import DataFrame,Timestamp

def check_nulls(df: DataFrame, columna: str) -> bool:
    if columna not in df.columns:
        raise ValueError(f'La columna "{columna}" no existe en el DataFrame.')
    return df[columna].isnull().any()

#Comprobar si el df esta vacio
def df_is_empty(df: DataFrame) -> bool:
    return df.empty

def validar_fecha(fecha: Timestamp) -> str:
    if pd.isna(fecha):
        return "Valor faltante (NaN)"
    elif isinstance(fecha, Timestamp):
        return "Cumple con el formato YYYY-MM-DD"
    else:
        return "No cumple con el formato requerido"