import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generación de una imagen binarizada de ejemplo ---
# Creamos una imagen en negro de 500x500 píxeles
height, width = 500, 500
# El tipo de dato np.uint8 es crucial para que OpenCV la procese correctamente
binary_image = np.zeros((height, width), dtype=np.uint8)

# Dibujamos formas geométricas en blanco (valor 255)
# Un círculo
cv2.circle(binary_image, (100, 100), 50, 255, -1)
# Un cuadrado
cv2.rectangle(binary_image, (200, 200), (300, 300), 255, -1)
# Un triángulo
# Definimos los vértices del triángulo
triangle_vertices = np.array([[400, 400], [480, 250], [320, 250]], np.int32)
# Reorganizamos los vértices en un formato compatible con polylines
triangle_vertices = triangle_vertices.reshape((-1, 1, 2))
cv2.fillPoly(binary_image, [triangle_vertices], 255)


# --- 2. Detección de Contornos ---
# Usamos cv2.findContours para encontrar los contornos en la imagen binarizada
# cv2.RETR_EXTERNAL: recupera solo los contornos más externos.
# cv2.CHAIN_APPROX_SIMPLE: comprime los segmentos horizontales, verticales y diagonales, dejando solo sus puntos finales.
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Creamos una copia de la imagen original para dibujar sobre ella.
# La convertimos a BGR para poder dibujar contornos y texto en color.
output_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)


# --- 3. Cálculo de Propiedades y Etiquetado ---
print(f"Se encontraron {len(contours)} figuras en la imagen.")

# Iteramos sobre cada contorno detectado
for i, c in enumerate(contours):
    # Omitimos contornos muy pequeños que podrían ser ruido
    if cv2.contourArea(c) < 20:
        continue

    # a. Calcular Área
    area = cv2.contourArea(c)

    # b. Calcular Perímetro
    # El segundo argumento (True) indica que la forma es cerrada.
    perimeter = cv2.arcLength(c, True)

    # c. Calcular Centroide a partir de los momentos
    M = cv2.moments(c)
    # Evitamos la división por cero si el momento m00 es 0
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
    else:
        # Si el área es cero, usamos el primer punto del contorno como referencia
        cx, cy = c[0][0]

    # d. Dibujar el contorno sobre la imagen de salida
    # El -1 en el cuarto argumento dibuja todos los contornos encontrados.
    # Aquí usamos [c] para dibujar uno por uno.
    cv2.drawContours(output_image, [c], -1, (0, 255, 0), 2) # Contorno en verde

    # e. Etiquetar cada figura con sus métricas
    # Colocamos un punto en el centroide para visualizarlo
    cv2.circle(output_image, (cx, cy), 5, (255, 0, 0), -1) # Centroide en azul

    # Preparamos las etiquetas de texto
    label_area = f"Area: {int(area)}"
    label_perimeter = f"Perimetro: {perimeter:.2f}"
    label_centroid = f"Centroide: ({cx}, {cy})"

    # Posicionamos y dibujamos las etiquetas cerca del centroide
    cv2.putText(output_image, label_area, (cx - 60, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(output_image, label_perimeter, (cx - 60, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(output_image, label_centroid, (cx - 60, cy + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)


# --- 4. Visualización de Resultados ---
plt.figure(figsize=(10, 10))
# Convertimos de BGR (formato de OpenCV) a RGB (formato de Matplotlib) para una correcta visualización
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title('Resultados del Análisis de Figuras Geométricas')
plt.axis('off') # Ocultamos los ejes para una mejor visualización
plt.show()