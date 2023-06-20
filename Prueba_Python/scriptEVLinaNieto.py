from carguearchivo import CargueArchivo
from limpiarCSV import LimpiarCSV, LimpiarCSVConPrueba
from nombresinnumeros import NombreSinNumeros
from formatotel import FormatoTel
from cambiarfecha import CambiarFecha
from clasificacionvivienda import ClasificacionVivienda
from asignarregion import AsignarRegion
from explotartxt import Exportartxt

if __name__ == "__main__":
    
    # Cargar archivo .csv que se normalizará
    cargue_archivo = CargueArchivo('Prueba.csv')
    df_limpio = cargue_archivo.cargararchivo()
    
    # Crear una instancia de la clase LimpiadorCSV para operar la columna 'Nombre'
    limpiador = LimpiarCSV('Nombre', df_limpio)
    # Eliminar las filas que tengan el campo ‘Nombre’ vacío.
    df_limpio = limpiador.limpiardatos()
    
    # Crear una instancia de la clase NombreSinNumeros para operar la columna 'Nombre'
    sinnumeros = NombreSinNumeros('Nombre', df_limpio)
    # Retirar los números del campo ‘Nombre’
    df_limpio = sinnumeros.nombrelimpio()
    
    # Crear una instancia de la clase LimpiadorCSV para operar la columna 'Teléfono'
    limpiador = LimpiarCSV('Teléfono', df_limpio)
    # Eliminar las filas que tengan el campo ‘Telefono’ vacío.
    df_limpio = limpiador.limpiardatos()
    
    # Crear una instancia de la clase FormatoTel para operar la columna 'Teléfono'
    formatotel = FormatoTel('Teléfono', df_limpio)
    # Retirar el 57 al inicio de cada numero en el campo ‘Telefono’.
    df_limpio = formatotel.tellimpio()
    
    # Crear una instancia de la clase LimpiarCSVConPrueba para operar la columna 'Correo electrónico'
    limpiador = LimpiarCSVConPrueba('Correo electrónico', df_limpio)
    # Eliminar las filas que tengan el campo ‘Correo electrónico’ vacío o tengan pruebas.
    df_limpio = limpiador.limpiardatos()
    
    # Crear una instancia de la clase CambiarFecha para operar la columna 'Fecha'
    formatofecha = CambiarFecha('Fecha', df_limpio)
    # Cambiar el formato de fecha a ‘aaaa-mm-dd’
    df_limpio = formatofecha.formatofecha()
    
    # Crear una instancia de la clase ClasificacionVivienda para operar la columna 'Tipo_Vivienda'
    tipovivienda = ClasificacionVivienda(df_limpio)
    # Crear una columna llamada 'Tipo_Vivienda' y agrupar datos según requerimientos
    df_limpio = tipovivienda.tipovivienda()
    
    # Crear una instancia de la clase AsignarRegion para operar la columna 'Region'
    region = AsignarRegion(df_limpio, 'Regiones.csv')
    # Crear una columna llamada ‘Region’ que muestre la región correspondiente en cada ciudad
    df_limpio = region.combinarregion()
    
    # Crear una instancia de la clase Exportartxt para operar archivo CSV
    exportartxt= Exportartxt(df_limpio)
    # Exportar los datos de Python a un archivo .txt
    exportartxt.exportar('PruebaResultadoFinal.txt')