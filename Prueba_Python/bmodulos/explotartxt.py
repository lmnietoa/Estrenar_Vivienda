import pandas as pd
import os

class Exportartxt:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
    def exportar(self, archivo_salida):
        # Explotar el dataframe a un archivo .txt
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
        ruta_salida = os.path.join(parent_dir, archivo_salida)
        self.dataframe.to_csv(ruta_salida, sep='\t', index=False)