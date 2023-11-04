import unittest
import pandas as pd
from pandas import DataFrame
from quality import check_nulls, check_type,df_is_empty

class TestQuality(unittest.TestCase):

    def setUp(self):
        # Crea un DataFrame de ejemplo para usar en las pruebas
        data = {'columna_1': [1, 2, None, 4, 5],
                'columna_2': [None, 2, 3, None, 5],
                'columna_3': [1, 2, 3, 4, 5],
                'columna_4': ['A', 'B', 'C', 'D', 'E'],
                'columna_5': [1.1, 2.2, 3.3, 4.4, 5.5]}
        self.df = DataFrame(data)

    def test_check_nulls_field_not_in_DataFrame(self):
        with self.assertRaises(ValueError):
            check_nulls(self.df, 'Score')

    def test_check_nulls_non_string_field_name(self):
        with self.assertRaises(TypeError):
            check_nulls(self.df, 123)

    def test_check_nulls_field_with_nulls(self):
        result = check_nulls(self.df, 'columna_1')
        self.assertEqual(result, 'KO')

    def test_check_nulls_field_without_nulls(self):
        result = check_nulls(self.df, 'columna_3')
        self.assertEqual(result, 'OK')
        
    #test is empty
    def test_df_is_empty_empty_df(self):
        # Crea un DataFrame vacío
        data = {'columna_1': [], 'columna_2': []}
        df = DataFrame(data)
        result = df_is_empty(df)
        self.assertTrue(result)  # Debería ser True

    def test_df_is_empty_non_empty_df(self):
        # Crea un DataFrame con datos
        data = {'columna_1': [1, 2, 3], 'columna_2': ['A', 'B', 'C']}
        df = DataFrame(data)
        result = df_is_empty(df)
        self.assertFalse(result)  # Debería ser False

    #test check type
    def test_check_type_column_not_in_DataFrame(self):
        result = check_type(self.df, 'columna_inexistente', int)
        self.assertEqual(result, 'Error: La columna "columna_inexistente" no se encuentra en el DataFrame')

    def test_check_type_type_mismatch(self):
        result = check_type(self.df, 'columna_4', int)
        self.assertEqual(result, 'KO: Al menos un registro no es del tipo especificado')

    def test_check_type_all_records_match_type(self):
        result = check_type(self.df, 'columna_3', int)
        self.assertEqual(result, 'OK: Todos los registros son del tipo especificado')

if __name__ == '__main__':
    unittest.main()

