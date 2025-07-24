import { useFrame } from '@react-three/fiber'
import { useRef } from 'react'
import { MathUtils } from 'three'

function MeshObject() {
  const meshRef = useRef()
  const scaleFactor = useRef(0)
  
  useFrame((state, delta) => {
    const { clock } = state
    const time = clock.elapsedTime
    
    // Animación de traslación senoidal
    meshRef.current.position.x = Math.sin(time) * 2
    meshRef.current.position.z = Math.cos(time) * 2
    
    // Rotación continua
    meshRef.current.rotation.y += delta * 1.5  // 1.5 radianes por segundo
    meshRef.current.rotation.x += delta * 0.8
    
    // Escalado pulsante
    scaleFactor.current = Math.sin(time) * 0.5 + 1
    meshRef.current.scale.setScalar(scaleFactor.current)
  })

  return (
    <mesh ref={meshRef}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial 
        color="#00ff00"
        emissive="#003300"
        metalness={0.5}
      />
    </mesh>
  )
}

export default MeshObject