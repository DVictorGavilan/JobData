import unittest
import pandas as pd
from pandas import DataFrame
from job_data import quality

class TestQuality(unittest.TestCase):

    def setUp(self):
        # Crea un DataFrame de ejemplo para usar en las pruebas
        data = {'columna_1': [1, 2, None, 4, 5],
                'columna_2': [None, 2, 3, None, 5],
                'columna_3': [1, 2, 3, 4, 5],
                'columna_enteros': [1, 2, 3, 4, 5],
                'columna_mezclada': [1, 2, '3', 4, 5],}
        self.df = DataFrame(data)

    def test_check_nulls_field_not_in_DataFrame(self):
        with self.assertRaises(ValueError):
            quality.check_nulls(self.df, 'Score')

    def test_check_nulls_non_string_field_name(self):
        with self.assertRaises(TypeError):
            quality.check_nulls(self.df, 123)

    def test_check_nulls_field_with_nulls(self):
        result = quality.check_nulls(self.df, 'columna_1')
        self.assertEqual(result, 'KO')

    def test_check_nulls_field_without_nulls(self):
        result = quality.check_nulls(self.df, 'columna_3')
        self.assertEqual(result, 'OK')
        
    #test is empty
    def test_df_is_empty_empty_df(self):
        # Crea un DataFrame vacío
        data = {'columna_1': [], 'columna_2': []}
        df = DataFrame(data)
        result = quality.df_is_empty(df)
        self.assertTrue(result)  # Debería ser True

    def test_df_is_empty_non_empty_df(self):
        # Crea un DataFrame con datos
        data = {'columna_1': [1, 2, 3], 'columna_2': ['A', 'B', 'C']}
        df = DataFrame(data)
        result = quality.df_is_empty(df)
        self.assertFalse(result)  # Debería ser False

    #test check type
    def test_column_not_in_DataFrame(self):
        with self.assertRaises(ValueError) as cm:
            quality.check_type(self.df, 'columna_inexistente', int)
        self.assertEqual(str(cm.exception), 'Error: La columna "columna_inexistente" no se encuentra en el DataFrame')

    def test_column_with_all_matching_data_type(self):
        result = quality.check_type(self.df, 'columna_enteros', int)
        self.assertEqual(result, 'OK: Todos los registros son del tipo especificado')

    def test_column_with_non_matching_data_type(self):
        with self.assertRaises(ValueError) as cm:
            quality.check_type(self.df, 'columna_mezclada', int)
        self.assertEqual(str(cm.exception), 'KO: Al menos un registro no es del tipo especificado')

if __name__ == '__main__':
    unittest.main()

