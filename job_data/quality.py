from pandas import DataFrame


def check_nulls(df: DataFrame, nombre_de_campo: str) -> str:
    if not isinstance(nombre_de_campo, str):
        raise TypeError('Error: El nombre de campo no es una cadena (str).')
    if nombre_de_campo not in df.columns:
        raise ValueError(f'Error: El campo "{nombre_de_campo}" no se encuentra en el DataFrame.')
    
    if df[nombre_de_campo].isnull().any():
        return 'KO'
    else:
        return 'OK'


def df_is_empty(df: DataFrame) -> bool:
    return df.empty


def check_type(df, column_name, data_type) -> str:
    if column_name not in df.columns:
        raise ValueError(f'Error: La columna "{column_name}" no se encuentra en el DataFrame')
    filtered_values = df[df[column_name].notnull()]
    if filtered_values[column_name].apply(lambda x: isinstance(x, data_type)).all():
        return 'OK: Todos los registros son del tipo especificado'
    else:
        raise ValueError('KO: Al menos un registro no es del tipo especificado')
