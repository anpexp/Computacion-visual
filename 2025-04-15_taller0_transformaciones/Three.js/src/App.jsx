import { Canvas } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'

export default function App() {
  return (
    <div style={{ height: '100vh', width: '100vw' }}>
      <Canvas camera={{ position: [3, 3, 3] }}>
        <ambientLight intensity={0.5} />
        <pointLight position={[10, 10, 10]} />
        
        <MeshObject />
        
        <OrbitControls enableZoom={true} />
      </Canvas>
    </div>
  )
}

function MeshObject() {
  return (
    <mesh>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial 
        color="#00ff00" 
        emissive="#003300"
        metalness={0.5}
      />
    </mesh>
  )
}
