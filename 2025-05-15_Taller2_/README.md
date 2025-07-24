Taller: Jerarquías y Transformaciones con React Three Fiber

Este proyecto demuestra el concepto de jerarquías de transformación en 3D utilizando React Three Fiber. La escena consiste en un sistema solar simple con un Sol, un Planeta y una Luna para ilustrar cómo las transformaciones de un objeto padre afectan a sus hijos.

🚀 Cómo Ejecutar

    Clona el repositorio: git clone <URL_DEL_REPOSITORIO>

    Instala las dependencias: npm install

    Inicia el servidor de desarrollo: npm run dev

🔬 Implementación y Visualización

A continuación se detalla la implementación clave y los resultados visuales del taller.

1. Creación de la Jerarquía

La estructura de la escena se organiza en tres niveles anidando componentes <group>. Cada <group> actúa como un contenedor que aplica sus transformaciones (posición, rotación, escala) a todos sus hijos.
JavaScript

// La estructura jerárquica en JSX
<group position={...} rotation={...}> {/* Nivel 1: Sol */}
  <mesh> {/* Malla del Sol */}
    <sphereGeometry />
    <meshStandardMaterial color="orange" />
  </mesh>

  <group ref={planetRef} position={[4, 0, 0]}> {/* Nivel 2: Planeta */}
    <mesh> {/* Malla del Planeta */}
      <sphereGeometry />
      <meshStandardMaterial color="royalblue" />
    </mesh>

    <group ref={moonRef} position={[1.5, 0, 0]}> {/* Nivel 3: Luna */}
      <mesh scale={0.5}> {/* Malla de la Luna */}
        <sphereGeometry />
        <meshStandardMaterial color="grey" />
      </mesh>
    </group>
  </group>
</group>

2. Controles en Tiempo Real con Leva

Para manipular el nodo padre (el Sol) en tiempo real, utilizamos el hook useControls de la librería Leva. Esto crea un panel de control con sliders que modifican directamente las propiedades de position y rotation del grupo principal.
JavaScript

import { useControls } from 'leva';

// ... dentro del componente
const { position, rotation } = useControls('Sol (Padre)', {
  position: { x: 0, y: 0, z: 0 },
  rotation: { x: 0, y: 0, z: 0 },
});

3. Animación de Órbita Relativa

La animación de las órbitas se implementa con el hook useFrame, que se ejecuta en cada fotograma. Al rotar los grupos del planeta y de la luna sobre su propio eje Y, logramos que orbiten alrededor de sus respectivos padres.

    GIF 1: Movimiento Relativo Compuesto
    Este GIF muestra el sistema en movimiento. Se observa a la Luna orbitando al Planeta, mientras que el sistema Planeta-Luna orbita al Sol.

4. Efecto de las Transformaciones del Padre

Manipular al padre (Sol) con los controles de Leva demuestra visualmente la herencia de transformaciones.

    GIF 2: Traslación del Padre
    Aquí se muestra cómo al mover la posición del Sol, todo el sistema (planeta y luna) se desplaza junto a él, manteniendo sus órbitas y distancias relativas intactas.

    GIF 3: Rotación del Padre
    Este GIF ilustra que al rotar el Sol, el plano orbital de todo el sistema se inclina, demostrando que las transformaciones se encadenan desde el padre hacia los hijos.

✅ Descripción de Prompts Usados

Para la generación de la estructura base de este taller, se utilizó un asistente de IA (Gemini) con un prompt inicial similar a este:

    "Desarrolla un taller en React Three Fiber sobre jerarquías y transformaciones. El objetivo es crear una escena con una estructura padre-hijo de al menos tres niveles (ej. Sol, Planeta, Luna). Aplica transformaciones de rotación y traslación al nodo padre y permite controlarlas en tiempo real con sliders de Leva. La animación debe mostrar el movimiento relativo de los hijos orbitando a sus padres."

A partir de la base generada, se refinó el código, se ajustaron los parámetros y se redactó la documentación para alinearla con los objetivos específicos del taller.

🗣️ Comentarios Personales y Aprendizaje

Aprendizaje:
Este taller fue increíblemente revelador. La lección más importante fue comprender de manera práctica que el orden de las transformaciones y la anidación son fundamentales. Antes, pensaba en la posición de cada objeto de forma global, pero ahora entiendo que todo se resuelve en cascada desde el padre. Ver cómo al rotar el Sol se inclinaba toda la órbita del planeta fue el momento "eureka" 💡. La abstracción que ofrece <group> en React Three Fiber simplifica enormemente la gestión de sistemas complejos, como un brazo robótico o, en este caso, un sistema solar.

Dificultades Encontradas:
Al principio, fue un poco confuso entender por qué la luna se movía "correctamente" sin tener que calcular su posición global en cada fotograma. La dificultad estaba en cambiar el chip de pensar en coordenadas del mundo (world space) a pensar en coordenadas locales (local space). Una vez superado ese obstáculo conceptual, la lógica de la animación con useFrame se volvió mucho más intuitiva. También, posicionar la cámara (<Canvas camera={...}>) inicialmente para que se viera bien la escena requirió un poco de prueba y error.