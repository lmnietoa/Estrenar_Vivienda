import pandas as pd

class NombreSinNumeros:
    def __init__(self, campo, dataframe):
        self.dataframe = dataframe.copy()
        self.campo = campo
        
    def nombrelimpio(self):
        # Eliminar los dígitos que se encuentren en los registros de un campo
        self.dataframe.loc[:,self.campo] = self.dataframe[self.campo].str.replace('\d+', '', regex=True)
        return self.dataframe