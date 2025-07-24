Taller: Escenas Paramétricas - Creación de Objetos desde Datos

Este repositorio documenta las soluciones desarrolladas para el taller "Escenas Paramétricas", cuyo objetivo es generar objetos 3D de manera programada a partir de datos estructurados. Se exploraron dos entornos radicalmente diferentes para lograr el mismo fin: un script de Python con la biblioteca vedo y una aplicación web interactiva con React Three Fiber.
🔹 Solución 1: Python con vedo y numpy

Esta implementación se enfoca en la generación de una escena 3D estática a partir de un script, ideal para pipelines de procesamiento de datos, automatización y exportación para su uso en otro software.
Generación de Objetos desde Datos

La lógica principal reside en un script de Python que sigue estos pasos:

    Definición de Datos: Se crea una lista de diccionarios en Python. Cada diccionario representa un objeto en la escena y contiene sus propiedades clave: coordenadas, forma, color y tamaño.

    Procesamiento Iterativo: Se recorre esta lista con un bucle for.

    Lógica Condicional: Dentro del bucle, una estructura if/elif/else evalúa la propiedad forma de cada objeto.

    Instanciación de Primitivas: Según la forma, se instancia el objeto 3D correspondiente de la biblioteca vedo (Sphere, Cube, Cylinder), aplicando las propiedades de posición, color y tamaño definidas en los datos.

    Agrupación: Todos los objetos generados se almacenan en una lista de "actores" para ser visualizados o exportados conjuntamente.

Demostración de la Escena


![alt text](<resultado py.gif>)
[Animación de la escena generada con Python y Vedo]
Código Relevante

El núcleo de la generación paramétrica se encuentra en este bloque de código:

# Lista para almacenar nuestros objetos 3D
actores_escena = []

# Bucle para recorrer cada definición de objeto en los datos
for definicion_objeto in datos_escena:
    
    # Extracción de propiedades
    coords = definicion_objeto["coordenadas"]
    forma = definicion_objeto["forma"]
    # ... (otras propiedades)
    
    objeto_3d = None

    # Condicionales para decidir qué primitiva 3D crear
    if forma == "esfera":
        objeto_3d = vedo.Sphere(r=tamaño).pos(coords).color(color)
    elif forma == "cubo":
        objeto_3d = vedo.Cube(side=tamaño).pos(coords).color(color)
    elif forma == "cilindro":
        objeto_3d = vedo.Cylinder(r=tamaño["radio"], height=tamaño["altura"]).pos(coords).color(color)
    else:
        # Fallback para formas no reconocidas
        objeto_3d = vedo.Sphere(r=0.1).pos(coords).color(color)

    if objeto_3d:
        actores_escena.append(objeto_3d)

# Visualización de todos los actores juntos
vedo.show(actores_escena, axes=1)

    Enlace al script completo: [link a tu script .py o notebook]

Evidencia de Exportación

El script combina todos los objetos en una sola malla y la exporta a formatos estándar, generando la siguiente estructura de archivos:

python/escena_exportada/
├── escena_parametrica.gltf
├── escena_parametrica.obj
└── escena_parametrica.stl

🔹 Solución 2: React Three Fiber y leva

Esta implementación lleva el concepto a un entorno web interactivo. La escena no es estática, sino que puede ser manipulada en tiempo real por el usuario a través de una interfaz gráfica.
Generación de Objetos desde Datos

El enfoque aquí es declarativo y se basa en los principios de React:

    Estado Dinámico: Se utiliza el hook useControls de la biblioteca leva para crear un panel de control en la UI. Este panel maneja el estado de la aplicación, como la cantidad de objetos a mostrar.

    Generación de Datos Memorizada: Una función genera un array de objetos con propiedades aleatorias (posición, color, etc.). Este array se recalcula únicamente cuando el estado de leva cambia, gracias al hook useMemo de React, lo que optimiza el rendimiento.

    Renderizado Declarativo: En lugar de un bucle for, se utiliza el método .map() de JavaScript directamente en el código JSX. Este método itera sobre el array de datos y renderiza un componente <ObjetoParametrico> por cada elemento.

    Componente Adaptativo: El componente <ObjetoParametrico> recibe las propiedades del objeto (forma, color, etc.) como props y utiliza una estructura switch para renderizar la geometría (<boxGeometry>, <sphereGeometry>, etc.) correspondiente.

Demostración de la Escena

![alt text](<resultado three.gif>)

[Animación de la escena interactiva con React y Leva]
Código Relevante

La magia de esta solución reside en la combinación del control de estado y el renderizado declarativo:

// 1. Hook de 'leva' para crear el control en la UI
const { cantidad } = useControls({
  cantidad: { value: 10, min: 1, max: 100, step: 1 }
});

// 2. Generación de datos que se actualiza solo cuando 'cantidad' cambia
const datosEscena = useMemo(() => generarDatosDeEscena(cantidad), [cantidad]);

// 3. Mapeo del array de datos para renderizar los componentes
return (
  <Canvas>
    {/* ... luces y controles ... */}
    {datosEscena.map((objeto) => (
      <ObjetoParametrico
        key={objeto.id}
        forma={objeto.forma}
        position={objeto.position}
        {/* ... otras props ... */}
      />
    ))}
  </Canvas>
);

    Enlace al repositorio o componente: [link a tu repositorio de React]

✅ Reflexiones del Proceso
Lógica Aplicada

El taller permitió contrastar dos paradigmas de programación:

    Imperativo (Python): Se dan instrucciones paso a paso (for, if, append) para construir la escena. Es un enfoque directo y muy claro para tareas de scripting y automatización.

    Declarativo (React): Se describe el resultado final deseado basado en el estado actual (datosEscena). React se encarga de averiguar cómo llegar a ese resultado de la manera más eficiente. Es un modelo mental más poderoso para interfaces de usuario complejas e interactivas.

Dificultades y Soluciones

La mayor dificultad surgió en la implementación de Python dentro de Google Colab.

    Error de X server connection: Ocurrió porque Colab es un entorno sin pantalla y vedo intentaba abrir una ventana. Se solucionó configurando un backend compatible con notebooks (vedo.settings.default_backend = 'k3d').

    Error TraitError con k3d: Un error de compatibilidad de tipos de datos entre vedo.Point y el backend. La solución final fue reemplazar el Point por una Sphere muy pequeña, evitando así el componente problemático y garantizando la estabilidad.

Posibles Mejoras

    Para Python: Se podría extender para leer datos desde archivos externos (CSV, JSON), permitiendo la visualización de datasets reales. También se podría implementar lógica procedural más compleja para la distribución de objetos (ej. usando ruido Perlin).

    Para React: La escena podría enriquecerse añadiendo interactividad a los objetos (clic, hover), incorporando físicas con @react-three/cannon, o cargando modelos 3D en formato .gltf en lugar de solo primitivas.

Descripción de los Prompts

El desarrollo se realizó de forma conversacional. Los prompts iniciales consistieron en la descripción completa del taller para cada entorno. Los prompts posteriores fueron de depuración, incluyendo los errores de traceback exactos encontrados en Colab, lo que permitió iterar sobre las soluciones hasta encontrar una funcional.