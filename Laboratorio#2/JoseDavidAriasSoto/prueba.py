import os

def crear_inventario(ruta_directorio):
    inventario = []
    
    for ruta_actual, directorios, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            ruta_completa = os.path.join(ruta_actual, archivo)
            tamaño = os.path.getsize(ruta_completa)
            inventario.append((archivo, ruta_completa, tamaño))
    
    return inventario

# Ruta del directorio que deseas analizar
ruta_directorio = "C:\Users\larzz\OneDrive\Escritorio\Universidad\Tercer Cuatri\Conta y Costos"

# Crear el inventario de documentos
inventario_documentos = crear_inventario(ruta_directorio)

# Mostrar el inventario
for documento in inventario_documentos:
    nombre_documento, ruta_documento, tamaño_documento = documento
    print(f"Nombre: {nombre_documento} | Ruta: {ruta_documento} | Tamaño: {tamaño_documento} bytes")
