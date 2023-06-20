import pandas as pd

class Exportartxt:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    def exportar(self, archivo_salida):
        # Explotar el dataframe a un archivo .txt
        self.dataframe.to_csv(archivo_salida, sep='\t', index=False)