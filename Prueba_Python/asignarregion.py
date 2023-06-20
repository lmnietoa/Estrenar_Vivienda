import pandas as pd

class AsignarRegion:
    def __init__(self, dataframe, archivo_regiones):
        self.dataframe = dataframe.copy()
        self.archivo_regiones = archivo_regiones

    def combinarregion(self):
        # Cargar el archivo CSV de regiones
        self.df_regiones = pd.read_csv(self.archivo_regiones, delimiter=';')
        # Realizar un merge entre los dataframes utilizando la columna 'Ciudad'
        self.df_final = pd.merge(self.dataframe, self.df_regiones, on='Ciudad', how='left')
        # Renombrar la columna resultante como 'Region'
        self.df_final.rename(columns={'Región': 'Region'}, inplace=True)
        return self.df_final