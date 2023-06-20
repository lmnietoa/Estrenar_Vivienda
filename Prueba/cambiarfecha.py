import pandas as pd

class CambiarFecha:
    def __init__(self, campo, dataframe):
        self.dataframe = dataframe.copy()
        self.campo = campo

    def formatofecha(self):
        # Cambiar el formato de la fecha
        self.dataframe.loc[:,self.campo] = pd.to_datetime(self.dataframe[self.campo], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
        return self.dataframe