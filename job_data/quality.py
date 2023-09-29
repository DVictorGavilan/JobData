from pandas import DataFrame

def check_nulls(df: DataFrame, columna: str) -> bool:
    if columna not in df.columns:
        raise ValueError(f'La columna "{columna}" no existe en el DataFrame.')
    return df[columna].isnull().any()
