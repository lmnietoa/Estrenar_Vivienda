import pandas as pd

class FormatoTel:
    def __init__(self, campo, dataframe):
        self.dataframe = dataframe.copy()
        self.campo = campo
        
    def tellimpio(self):
        # Convertir los registros del campo "Teléfono" en string
        self.dataframe.loc[:,self.campo] = self.dataframe[self.campo].str.replace(',', '', regex=True).astype(float).astype('int64').astype(str)
        # Buscar "57" en el string y borrarlo
        self.dataframe.loc[:,self.campo] = self.dataframe[self.campo].apply(lambda x: x[2:] if x.startswith('57') else x)
        return self.dataframe