import pandas as pd

class CargueArchivo:
    def __init__(self, archivo_entrada):
        # Recepción de variables
        self.archivo_entrada = archivo_entrada
        self.dataframe = None

    def cargararchivo(self):
        # Leer el archivo CSV utilizando Pandas
        self.dataframe = pd.read_csv(self.archivo_entrada, delimiter=';')
        return self.dataframe