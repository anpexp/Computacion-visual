import React, { useRef } from 'react';
import { useLoader } from '@react-three/fiber';
import { STLLoader } from 'three/examples/jsm/loaders/STLLoader';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';

// 1. Componente para el modelo STL
export function StlModel({ url }) {
  // useLoader es un "hook" que carga assets de forma declarativa
  // STL no tiene material, por eso debemos definir uno.
  const geom = useLoader(STLLoader, url);
  return (
    <mesh geometry={geom} scale={0.05}>
      <meshStandardMaterial color="hotpink" />
    </mesh>
  );
}

// 2. Componente para el modelo OBJ
export function ObjModel({ url }) {
  // OBJ sí puede tener material, pero para este taller lo asignamos manualmente
  const obj = useLoader(OBJLoader, url);
  return (
    <primitive object={obj} scale={0.05}>
      <meshStandardMaterial color="skyblue" />
    </primitive>
  );
}

// 3. Re-exportamos el modelo GLTF generado para tener todo en un lugar
// Asegúrate que la ruta al componente `Cubo.jsx` es correcta.
export { Cubo as GltfModel } from './Cubo';