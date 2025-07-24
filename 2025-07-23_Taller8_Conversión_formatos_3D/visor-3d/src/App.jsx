import React, { useState, Suspense } from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Stage } from '@react-three/drei';
import { StlModel, ObjModel, GltfModel } from './modelos';
import './App.css'; // Para estilos básicos

// Información de los modelos para el bonus
const modelInfo = {
  gltf: { name: 'GLTF', vertices: 8, faces: 12 },
  obj: { name: 'OBJ', vertices: 8, faces: 12 },
  stl: { name: 'STL', vertices: 36, faces: 12 },
};

export default function App() {
  const [currentModel, setCurrentModel] = useState('gltf');

  const renderCurrentModel = () => {
    switch (currentModel) {
      case 'stl':
        return <StlModel url="/cubo.stl" />;
      case 'obj':
        return <ObjModel url="/cubo.obj" />;
      case 'gltf':
      default:
        // El componente GLTF no necesita URL porque ya está autocontenido
        return <GltfModel />;
    }
  };

  return (
    <>
      {/* Interfaz de usuario (botones y bonus) */}
      <div className="ui-container">
        <h1>Visor de Modelos 3D</h1>
        <div className="button-group">
          <button onClick={() => setCurrentModel('gltf')}>Ver GLTF</button>
          <button onClick={() => setCurrentModel('obj')}>Ver OBJ</button>
          <button onClick={() => setCurrentModel('stl')}>Ver STL</button>
        </div>
        <div className="info-box">
          <h3>Formato Actual: {modelInfo[currentModel].name}</h3>
          <p>Vértices: {modelInfo[currentModel].vertices}</p>
          <p>Caras: {modelInfo[currentModel].faces}</p>
        </div>
      </div>

      {/* Escena 3D */}
      <Canvas dpr={[1, 2]} camera={{ fov: 45 }}>
        {/* Suspense es necesario para esperar a que los modelos carguen */}
        <Suspense fallback={null}>
          {/* Stage nos da un suelo e iluminación profesional de forma sencilla */}
          <Stage environment="city" intensity={0.6}>
            {renderCurrentModel()}
          </Stage>
        </Suspense>
        {/* OrbitControls nos permite mover la cámara */}
        <OrbitControls makeDefault />
      </Canvas>
    </>
  );
}