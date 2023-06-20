import pandas as pd

class ClasificacionVivienda:
    def __init__(self, dataframe):
        self.dataframe = dataframe.copy()
    
    def tipovivienda(self):
        # Definir una función para asignar los valores a la columna 'Tipo_Vivienda'
        def asignar_tipo(row):
            if 0 <= row['Precio desde'] <= 200000000:
                return 'VIS'
            elif 200000000 < row['Precio desde'] <= 500000000:
                return 'MEDIA'
            elif 500000000 < row['Precio desde'] <= 800000000:
                return 'ALTA'
            elif row['Precio desde'] > 800000000:
                return 'SUPER ALTA'
            else:
                return None
        
        # Aplicar la función a cada fila y asignar los valores a la columna 'Tipo_Vivienda'
        self.dataframe['Tipo_Vivienda'] = self.dataframe.apply(asignar_tipo, axis=1)
        return self.dataframe
        