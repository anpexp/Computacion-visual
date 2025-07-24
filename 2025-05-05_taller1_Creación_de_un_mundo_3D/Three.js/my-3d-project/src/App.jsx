import { useState, useEffect } from 'react'
import { Canvas, useLoader } from '@react-three/fiber'
import { OrbitControls, Edges, Points } from '@react-three/drei'
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader'

function Model({ mode, setVertexCount }) {
  const obj = useLoader(OBJLoader, '/model.obj')
  const geometry = obj.children[0].geometry

  // Actualizar conteo de vértices
  useEffect(() => {
    if (geometry) {
      setVertexCount(geometry.attributes.position.count)
    }
  }, [geometry, setVertexCount])

  return (
    <>
      {mode === 'vertices' && (
        <points geometry={geometry}>
          <pointsMaterial size={0.05} color="red" />
        </points>
      )}
      
      {mode === 'edges' && (
        <mesh geometry={geometry}>
          <meshStandardMaterial color="#fff" wireframe={false} />
          <Edges color="yellow" />
        </mesh>
      )}
      
      {mode === 'faces' && (
        <mesh geometry={geometry}>
          <meshStandardMaterial color="#666" wireframe={false} />
        </mesh>
      )}
    </>
  )
}

function Controls() {
  return (
    <OrbitControls
      enablePan={true}
      enableZoom={true}
      enableRotate={true}
    />
  )
}

function UI({ mode, setMode, vertexCount }) {
  return (
    <div style={{ position: 'absolute', top: 20, left: 20, color: 'white' }}>
      <button onClick={() => setMode('faces')}>Caras</button>
      <button onClick={() => setMode('edges')}>Aristas</button>
      <button onClick={() => setMode('vertices')}>Vértices</button>
      <p>Vértices: {vertexCount}</p>
    </div>
  )
}

export default function App() {
  const [mode, setMode] = useState('faces')
  const [vertexCount, setVertexCount] = useState(0)

  return (
    <>
      <UI mode={mode} setMode={setMode} vertexCount={vertexCount} />
      <Canvas camera={{ position: [2, 2, 2] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        <Model mode={mode} setVertexCount={setVertexCount} />
        <Controls />
      </Canvas>
    </>
  )
}