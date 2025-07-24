
import trimesh
import numpy as np

# Crear una malla de un cubo (caja)
# trimesh.primitives.Box() genera una geometría de caja centrada en el origen.
mesh = trimesh.primitives.Box()

# Añadir colores a los vértices para probar la capacidad de cada formato
# Generamos un color RGB aleatorio para cada uno de los 8 vértices del cubo.
# La información de color es crucial para diferenciar GLTF/OBJ de STL.
vertex_colors = np.random.rand(len(mesh.vertices), 3) * 255
mesh.visual.vertex_colors = vertex_colors

# Exportar la malla a los diferentes formatos
try:
    mesh.export('cubo.stl')
    mesh.export('cubo.obj')
    mesh.export('cubo.gltf')
    print("✅ Modelos base (cubo.stl, cubo.obj, cubo.gltf) creados exitosamente.")
except Exception as e:
    print(f"❌ Ocurrió un error al exportar: {e}")

def analizar_malla(ruta_archivo):
    """
    Carga una malla desde un archivo, imprime sus propiedades y la devuelve.
    """
    print(f"\n--- Analizando: {ruta_archivo} ---")
    try:
        # Cargar la malla usando trimesh.load
        # trimesh se encarga de detectar el formato y usar el cargador adecuado.
        malla = trimesh.load(ruta_archivo, force='mesh')

        print(f"Tipo de objeto cargado: {type(malla)}")
        print(f"Vértices: {len(malla.vertices)}")
        print(f"Caras (triángulos): {len(malla.faces)}")

        # .is_watertight verifica si la malla es un sólido cerrado sin agujeros.
        print(f"¿Es hermética (watertight)?: {malla.is_watertight}")

        # Comprobar si la malla tiene información de color
        # .visual.kind devuelve el tipo de información visual (ej: 'vertex', 'face', 'texture')
        if hasattr(malla.visual, 'kind') and malla.visual.kind:
             print(f"Información de color: Sí (tipo: {malla.visual.kind})")
        else:
             print("Información de color: No")

        return malla
    except Exception as e:
        print(f"No se pudo cargar o analizar la malla: {e}")
        return None

# Lista de archivos a analizar
archivos = ['cubo.stl', 'cubo.obj', 'cubo.gltf']
mallas = {}

for archivo in archivos:
    mallas[archivo] = analizar_malla(archivo)

# Para visualizar en un notebook, a veces es necesario configurar el backend.
# Si la visualización no aparece, puedes probar a ejecutar esto:
# trimesh.viewer.notebook.set_viewer('pyglet')

print("Visualizando cubo.stl (sin colores)...")
if mallas.get('cubo.stl'):
    mallas['cubo.stl'].show()

print("Visualizando cubo.obj (con colores, si el viewer lo soporta)...")
if mallas.get('cubo.obj'):
    mallas['cubo.obj'].show()

print("Visualizando cubo.gltf (con colores de vértice)...")
if mallas.get('cubo.gltf'):
    mallas['cubo.gltf'].show()

# Cargar el modelo original con toda la información
malla_gltf = trimesh.load('cubo.gltf', force='mesh')

print("Convirtiendo de GLTF a STL...")

# Exportar a STL. Trimesh automáticamente descartará la información no soportada (colores).
try:
    malla_gltf.export('cubo_convertido_a.stl')
    print("✅ Conversión a STL exitosa.")

    # Analicemos y visualicemos el resultado para confirmar la pérdida de datos
    malla_stl_convertida = analizar_malla('cubo_convertido_a.stl')
    if malla_stl_convertida:
        malla_stl_convertida.show()

except Exception as e:
    print(f"❌ Error durante la conversión: {e}")

import pandas as pd

def generar_informe_comparativo(lista_archivos):
    """
    Toma una lista de rutas de archivos 3D y devuelve un DataFrame de Pandas
    con una comparación de sus propiedades.
    """
    datos = []
    for archivo in lista_archivos:
        try:
            malla = trimesh.load(archivo, force='mesh')
            info = {
                "Archivo": archivo,
                "Vértices": len(malla.vertices),
                "Caras": len(malla.faces),
                "Es Hermética": malla.is_watertight,
                "Tiene Color": hasattr(malla.visual, 'kind') and malla.visual.kind is not None
            }
            datos.append(info)
        except Exception as e:
            print(f"No se pudo procesar {archivo}: {e}")

    # Para usar pd.DataFrame, necesitas tener pandas instalado (!pip install pandas)
    df = pd.DataFrame(datos)
    return df

# Lista de todos nuestros modelos (originales y convertidos)
todos_los_modelos = ['cubo.stl', 'cubo.obj', 'cubo.gltf', 'cubo_convertido_a.stl']

# Generar y mostrar el informe
informe = generar_informe_comparativo(todos_los_modelos)
print("\n--- ✨ Informe Comparativo Automatizado ✨ ---")
print(informe)