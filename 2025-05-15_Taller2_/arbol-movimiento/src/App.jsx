// src/App.jsx
import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { useControls } from 'leva';

/**
 * Componente que representa nuestro sistema solar jerárquico.
 */
function SolarSystem() {
  // Referencias para animar los grupos de objetos
  const planetRef = useRef();
  const moonRef = useRef();

  // Controles en tiempo real con Leva para el nodo padre (Sol)
  const { position, rotation } = useControls('Sol (Padre)', {
    position: { x: 0, y: 0, z: 0 },
    rotation: { x: 0, y: 0, z: 0 },
  });

  // useFrame es un hook que ejecuta una función en cada fotograma renderizado
  useFrame((state, delta) => {
    // Animación relativa: el planeta orbita alrededor del sol
    if (planetRef.current) {
      planetRef.current.rotation.y += delta * 0.5; // Velocidad de rotación del planeta
    }
    // Animación relativa: la luna orbita alrededor del planeta
    if (moonRef.current) {
      moonRef.current.rotation.y += delta * 1.5; // Velocidad de rotación de la luna
    }
  });

  return (
    // NIVEL 1: El grupo del Sol (Padre de todo el sistema)
    // Las transformaciones aplicadas aquí afectan a todos los hijos.
    <group position={[position.x, position.y, position.z]} rotation={[rotation.x, rotation.y, rotation.z]}>
      {/* Malla del Sol */}
      <mesh>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial color="orange" emissive="orange" emissiveIntensity={2} />
      </mesh>

      {/* NIVEL 2: El grupo del Planeta (hijo del Sol) */}
      {/* Su posición es relativa a la del Sol. */}
      <group ref={planetRef} position={[4, 0, 0]}>
        {/* Malla del Planeta */}
        <mesh>
          <sphereGeometry args={[0.5, 32, 32]} />
          <meshStandardMaterial color="royalblue" />
        </mesh>

        {/* NIVEL 3 (Bonus): El grupo de la Luna (hijo del Planeta) */}
        {/* Su posición es relativa a la del Planeta. */}
        <group ref={moonRef} position={[1.5, 0, 0]}>
          {/* Malla de la Luna */}
          <mesh scale={0.5}> {/* Hacemos la luna más pequeña */}
            <sphereGeometry args={[0.3, 32, 32]} />
            <meshStandardMaterial color="grey" />
          </mesh>
        </group>
      </group>
    </group>
  );
}

/**
 * Componente principal de la aplicación.
 */
export default function App() {
  return (
    <Canvas camera={{ position: [0, 5, 12], fov: 75 }}>
      {/* Luces para iluminar la escena */}
      <ambientLight intensity={0.3} />
      <pointLight position={[10, 10, 10]} intensity={1.5} />
      
      {/* Componente del sistema solar */}
      <SolarSystem />
      
      {/* Controles para mover la cámara */}
      <OrbitControls />
      
      {/* Un grid para tener una referencia visual del suelo */}
      <gridHelper args={[50, 50]} />
    </Canvas>
  );
}