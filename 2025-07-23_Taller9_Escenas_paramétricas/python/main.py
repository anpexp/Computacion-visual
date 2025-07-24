# Taller - Escenas Paramétricas: Creación de Objetos desde Datos
# Solución con Python, NumPy y Vedo (Versión para Escritorio)

# ==============================================================================
# PASO 0: INSTALACIÓN DE BIBLIOTECAS (Entorno de Escritorio)
# ==============================================================================
# En un entorno de escritorio, abre tu terminal o consola y ejecuta el
# siguiente comando para instalar las bibliotecas necesarias.
# No es necesario instalar 'k3d'.
#
# pip install vedo numpy
#
# =------------------------------------------------------------------------------

# ==============================================================================
# PASO 1: IMPORTACIÓN DE BIBLIOTECAS
# ==============================================================================
# Importamos las herramientas necesarias.
import vedo
import numpy as np
import os

# ==============================================================================
# PASO 1.5: CONFIGURACIÓN DE ENTORNO
# ==============================================================================
# Para un entorno de escritorio, NO necesitamos configurar un backend especial.
# Comentamos o eliminamos la siguiente línea para que vedo use su
# backend por defecto, que abrirá una ventana interactiva.
# vedo.settings.default_backend = 'k3d'
# ------------------------------------------------------------------------------


# ==============================================================================
# PASO 2: DEFINICIÓN DE DATOS ESTRUCTURADOS
# ==============================================================================
# Esta parte del código no cambia. La estructura de datos es la misma.
# ------------------------------------------------------------------------------
datos_escena = [
    {
        "coordenadas": [0, 0, 0],
        "forma": "esfera",
        "color": "red",
        "tamaño": 0.5
    },
    {
        "coordenadas": [2, 0, 0],
        "forma": "cubo",
        "color": "blue",
        "tamaño": 0.8
    },
    {
        "coordenadas": [-2, 0, 0],
        "forma": "cilindro",
        "color": "green",
        "tamaño": {"radio": 0.3, "altura": 1.5}
    },
    {
        "coordenadas": [0, 2, 0],
        "forma": "esfera",
        "color": "yellow",
        "tamaño": 0.4
    },
    {
        "coordenadas": [0, -2, 0],
        "forma": "cubo",
        "color": "purple",
        "tamaño": 0.6
    },
    {
        "coordenadas": [2, 2, 0],
        "forma": "desconocida",
        "color": "grey",
        "tamaño": 0.2
    }
]

# ==============================================================================
# PASO 3: GENERACIÓN DE LA ESCENA CON BUCLES Y CONDICIONALES
# ==============================================================================
# El proceso de generación de objetos es idéntico.
# ------------------------------------------------------------------------------

print("Iniciando la generación de la escena...")

actores_escena = []

for definicion_objeto in datos_escena:
    
    coords = definicion_objeto["coordenadas"]
    forma = definicion_objeto["forma"]
    color = definicion_objeto["color"]
    tamaño = definicion_objeto["tamaño"]
    
    objeto_3d = None

    print(f"Procesando objeto: {forma} en {coords}")

    if forma == "esfera":
        objeto_3d = vedo.Sphere(r=tamaño).pos(coords).color(color)
        
    elif forma == "cubo":
        objeto_3d = vedo.Cube(side=tamaño).pos(coords).color(color)
        
    elif forma == "cilindro":
        objeto_3d = vedo.Cylinder(r=tamaño["radio"], height=tamaño["altura"]).pos(coords).color(color)
    
    else:
        print(f"  -> Forma '{forma}' no reconocida. Creando una esfera pequeña como marcador.")
        objeto_3d = vedo.Sphere(r=0.1).pos(coords).color(color)

    if objeto_3d:
        actores_escena.append(objeto_3d)

print("Generación de objetos completada.")

# ==============================================================================
# PASO 4: VISUALIZACIÓN Y EXPORTACIÓN DE LA ESCENA
# ==============================================================================
# La visualización y exportación funcionan de manera similar.
# ------------------------------------------------------------------------------

# 1. VISUALIZACIÓN EN VENTANA NATIVA
# -----------------
print("\nMostrando la escena 3D en una ventana interactiva...")
# Esta llamada ahora abrirá una ventana de escritorio.
# El script se pausará aquí hasta que cierres la ventana.
vedo.show(actores_escena, __doc__, axes=1, viewup='z').close()


# 2. EXPORTACIÓN
# -----------------
# El proceso de exportación es exactamente el mismo.
escena_combinada = vedo.merge(actores_escena)
escena_combinada.compute_normals().clean()

directorio_salida = "escena_exportada"
if not os.path.exists(directorio_salida):
    os.makedirs(directorio_salida)

print(f"\nExportando la escena combinada al directorio '{directorio_salida}'...")

ruta_obj = os.path.join(directorio_salida, "escena_parametrica.obj")
vedo.write(escena_combinada, ruta_obj)
print(f" - Escena guardada como: {ruta_obj}")

ruta_stl = os.path.join(directorio_salida, "escena_parametrica.stl")
vedo.write(escena_combinada, ruta_stl)
print(f" - Escena guardada como: {ruta_stl}")

ruta_gltf = os.path.join(directorio_salida, "escena_parametrica.gltf")
vedo.write(escena_combinada, ruta_gltf)
print(f" - Escena guardada como: {ruta_gltf}")

print("\n¡Proceso del taller completado exitosamente!")
