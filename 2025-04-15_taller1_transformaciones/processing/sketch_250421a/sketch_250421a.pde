void setup() {
  size(800, 600, P3D);
  smooth();
  noStroke();
}

void draw() {
  background(0);
  lights();
  directionalLight(255, 255, 255, 0, -1, -1);
  
  float time = millis() * 0.001;  // Tiempo en segundos
  
  // Centro de referencia
  translate(width/2, height/2, 0);
  
  pushMatrix();
  
  // 1. Traslación senoidal en X y Z + movimiento vertical en Y
  float moveX = sin(time) * 150;
  float moveZ = cos(time) * 150;
  float moveY = sin(time * 2) * 80;  // Doble frecuencia para movimiento más rápido
  translate(moveX, moveY, moveZ);
  
  // 2. Rotación en 3 ejes con diferentes velocidades
  rotateX(time);           // 1 rotación completa por segundo en X
  rotateY(time * 0.8);     // 80% de velocidad en Y
  rotateZ(time * 0.3);     // 30% de velocidad en Z
  
  // 3. Escalado pulsante usando función seno
  float scaleFactor = sin(time * 3) * 0.4 + 1;  // Entre 0.6 y 1.4
  scale(scaleFactor);
  
  // Dibujar cubo con material
  fill(30, 144, 255);  // Dodger Blue
  box(80);
  
  popMatrix();
}
