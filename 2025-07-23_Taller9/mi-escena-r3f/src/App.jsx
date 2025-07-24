// src/App.jsx

import React, { useMemo } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { useControls } from 'leva';
import * as THREE from 'three';

// ==============================================================================
// PASO 1: CREACIÓN DE DATOS PARAMÉTRICOS
// ==============================================================================
// En lugar de una lista estática, creamos una función que genera datos
// aleatorios. Esto nos permitirá controlar la cantidad de objetos con Leva.
// Cada objeto tendrá las propiedades que necesitamos: id, forma, posición, etc.

function generarDatosDeEscena(cantidad) {
  const formasDisponibles = ['caja', 'esfera', 'cilindro'];
  const datos = [];

  for (let i = 0; i < cantidad; i++) {
    datos.push({
      id: `obj_${i}`,
      forma: formasDisponibles[i % formasDisponibles.length], // Alterna entre las formas
      position: [(Math.random() - 0.5) * 10, (Math.random() - 0.5) * 10, (Math.random() - 0.5) * 10],
      rotation: [Math.random() * Math.PI, Math.random() * Math.PI, Math.random() * Math.PI],
      scale: 0.5 + Math.random() * 0.5,
      color: new THREE.Color().setHSL(Math.random(), 0.7, 0.5), // Color aleatorio
    });
  }
  return datos;
}

// ==============================================================================
// PASO 2: COMPONENTE PARA RENDERIZAR UN ÚNICO OBJETO
// ==============================================================================
// Este componente recibe las propiedades de un objeto y decide qué geometría
// renderizar usando un condicional (en este caso, un 'switch').
// Esta es la clave para tener estructuras adaptativas.

function ObjetoParametrico({ forma, position, rotation, scale, color }) {
  return (
    <mesh position={position} rotation={rotation} scale={scale}>
      {/* Condicional para elegir la geometría basada en la propiedad 'forma' */}
      {(() => {
        switch (forma) {
          case 'caja':
            return <boxGeometry />;
          case 'esfera':
            return <sphereGeometry args={[0.8, 32, 32]} />; // radio, segmentos...
          case 'cilindro':
            return <cylinderGeometry args={[0.5, 0.5, 1.5, 32]} />; // radioSup, radioInf, altura, segmentos
          default:
            return <boxGeometry />;
        }
      })()}
      <meshStandardMaterial color={color} />
    </mesh>
  );
}


// ==============================================================================
// PASO 3: COMPONENTE PRINCIPAL DE LA APLICACIÓN
// ==============================================================================
// Aquí orquestamos todo:
// 1. Usamos 'leva' para crear un control que modifica la cantidad de objetos.
// 2. Usamos 'useMemo' para regenerar los datos solo cuando la cantidad cambia.
// 3. Mapeamos los datos para renderizar cada objeto usando nuestro componente.

export default function App() {
  
  // 1. Control dinámico con Leva
  // Este hook crea un panel de UI para controlar el valor 'cantidad'.
  const { cantidad } = useControls({
    cantidad: {
      value: 10, // Valor inicial
      min: 1,      // Valor mínimo
      max: 100,    // Valor máximo
      step: 1,     // Incremento
      label: 'Nº de Objetos'
    }
  });

  // 2. Generación de datos memorizada
  // useMemo es un hook de React que evita recalcular los datos en cada render.
  // Solo se ejecutará de nuevo si el valor de 'cantidad' (en el array de dependencias) cambia.
  const datosEscena = useMemo(() => generarDatosDeEscena(cantidad), [cantidad]);

  return (
    // El Canvas es el portal a nuestra escena 3D
    <Canvas camera={{ position: [0, 0, 15], fov: 60 }}>
      {/* --- Iluminación y Ayudantes --- */}
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 10, 5]} intensity={1.5} />
      <axesHelper args={[5]} /> {/* Muestra los ejes X, Y, Z */}
      <OrbitControls /> {/* Permite mover la cámara con el ratón */}

      {/* 3. Mapeo del array de datos para crear los objetos 3D
        Aquí usamos .map() para iterar sobre nuestros datos y renderizar
        un componente <ObjetoParametrico> por cada elemento del array.
        Pasamos las propiedades de cada objeto como props de React.
      */}
      {datosEscena.map((objeto) => (
        <ObjetoParametrico
          key={objeto.id} // La 'key' es crucial en React para listas dinámicas
          forma={objeto.forma}
          position={objeto.position}
          rotation={objeto.rotation}
          scale={objeto.scale}
          color={objeto.color}
        />
      ))}
    </Canvas>
  );
}