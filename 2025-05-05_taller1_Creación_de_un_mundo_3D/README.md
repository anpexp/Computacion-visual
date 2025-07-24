# Proyecto de Visualización de Modelos 3D

Este repositorio contiene dos implementaciones para la visualización de modelos 3D:

* **Python con trimesh y vedo**: Generación de vistas estáticas y animaciones por código.
* **React Three Fiber**: Aplicación web interactiva con controles para mostrar vértices, aristas o caras.

---

## 1. Implementación en Python

### Descripción

Se utiliza **trimesh** para cargar y procesar el modelo 3D (`.stl`, `.obj` o `.gltf`) y **vedo** para renderizar una visualización con componentes estructurales:

* Vértices en rojo
* Aristas en negro
* Caras semitransparentes en cian
* Información textual superpuesta

Además, se genera una animación rotativa que se exporta como video y se muestra como GIF.

### Visualización Final

![Rotación 360° del modelo 3D](assets/python_animation.gif)

### Código Relevante

```python
import trimesh
import vedo
from vedo import Plotter, Video
import numpy as np
# Cargar y convertir modelo
mesh = trimesh.load('modelo.stl')
vedo_mesh = vedo.Mesh([mesh.vertices, mesh.faces]).lighting('glossy')

# Configurar escena
plt = Plotter(axes=1, bg='white', size=(1000, 800))
vedo_mesh.c('cyan').alpha(0.5)
edges = vedo_mesh.edges().c('black').lw(1)
vertices = vedo_mesh.points().c('red').ps(8)

# Mostrar información
info = f"""
Información del modelo:
- Vértices: {len(mesh.vertices)}
- Caras:   {len(mesh.faces)}
- Aristas: {len(mesh.edges)}
- Volumen: {mesh.volume:.2f} unidades³
- Bounding box: {mesh.bounds}
"""

plt.show(vedo_mesh, edges, vertices,
         vedo.Text2D(info, pos='bottom-left', c='k'),
         "Visualización 3D con Componentes Estructurales")

# Generar animación
video = Video("animation.mp4", duration=10, fps=15)
for i in range(0, 360, 2):
    vedo_mesh.rotate_y(2)
    video.add_frame()
video.close()
```

> Enlace al repositorio: [Python-3D-Visualization](https://github.com/usuario/Python-3D-Visualization)

---

## 2. Implementación en React Three Fiber

### Descripción

Aplicación web creada con **React**, **@react-three/fiber** y **@react-three/drei**:

* Muestra el mismo modelo 3D (`model.obj`)
* Permite alternar entre modos de visualización:

  * Caras sólidas
  * Aristas resaltadas
  * Puntos (vértices)
* Controles de cámara mediante **OrbitControls**
* Indicador dinámico del conteo de vértices

### Visualización Final

![Interfaz React Three Fiber](assets/react_viewer.gif)

### Código Relevante

```jsx
import { useState, useEffect } from 'react'
import { Canvas, useLoader } from '@react-three/fiber'
import { OrbitControls, Edges, Points } from '@react-three/drei'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader'

function Model({ mode, setVertexCount }) {
  const obj = useLoader(OBJLoader, '/model.obj')
  const geometry = obj.children[0].geometry

  useEffect(() => {
    if (geometry) setVertexCount(geometry.attributes.position.count)
  }, [geometry, setVertexCount])

  return (
    <>  {mode === 'vertices' && <Points geometry={geometry} size={0.05} color="red" />}
       {mode === 'edges'    && <mesh geometry={geometry}><Edges color="yellow" /></mesh>}
       {mode === 'faces'    && <mesh geometry={geometry}><meshStandardMaterial color="#666" /></mesh>}
    </>
  )
}

export default function App() {
  const [mode, setMode] = useState('faces')
  const [vertexCount, setVertexCount] = useState(0)

  return (
    <>  <UI mode={mode} setMode={setMode} vertexCount={vertexCount} />
        <Canvas camera={{ position: [2,2,2] }}>
          <ambientLight intensity={0.5} />
          <pointLight position={[10,10,10]} />
          <Model mode={mode} setVertexCount={setVertexCount} />
          <OrbitControls />
        </Canvas>
    </>
  )
}
```

> Enlace al repositorio: [React-3D-Viewer](https://github.com/usuario/React-3D-Viewer)

---

## Prompts Utilizados

No se aplicaron modelos generativos ni prompts interactivos en este proyecto.

---

## Aprendizajes y Dificultades

* **Aprendizajes**:

  * Manejo de librerías 3D en Python y JavaScript
  * Flujo de trabajo para convertir modelos entre formatos
  * Optimización de escenas para render en tiempo real

* **Dificultades**:

  * Sincronización de conteo de vértices en React
  * Ajuste de materiales semitransparentes y sombras en vedo
  * Exportar animaciones fluidas sin pérdida de calidad

---

*README generado el 26 de mayo de 2025*
