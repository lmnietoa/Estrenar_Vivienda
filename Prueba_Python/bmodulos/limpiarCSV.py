import pandas as pd

class LimpiarCSV:
    def __init__(self, campo, dataframe):
        self.df = dataframe
        self.campo = campo
        
    def limpiardatos(self):
        # Eliminar registros vacíos en un campo dado
        df_limpiado = self.df.dropna(subset=[self.campo])
        return df_limpiado
    
class LimpiarCSVConPrueba(LimpiarCSV):
    def limpiardatos(self):
        # Eliminar registros vacíos en un campo dado
        df = self.df.dropna(subset=[self.campo])
        # Eliminar la palabra "prueba" al inicio de los registros en un campo dado
        df_limpiado = df[~df[self.campo].str.startswith('prueba')]
        return df_limpiado