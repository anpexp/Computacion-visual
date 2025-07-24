Taller - Segmentando el Mundo: Binarización y Reconocimiento de Formas 🔬

Este repositorio contiene la solución al taller práctico de visión por computador, enfocado en técnicas de segmentación de imágenes y análisis morfológico utilizando Python y OpenCV.

📝 Proceso de Segmentación y Análisis

El objetivo es identificar y analizar formas geométricas dentro de una imagen. El proceso se puede resumir en los siguientes pasos:

    Carga y Preprocesamiento: La imagen original se carga y se convierte a escala de grises. Este paso es fundamental porque las operaciones de umbralización requieren una imagen de un solo canal para funcionar.

    Binarización (Umbralización): La imagen en escala de grises se segmenta para crear una imagen binaria (blanco y negro). Se utilizó un umbral fijo, donde cada píxel se compara con un valor predefinido (en este caso, 127). Los píxeles más oscuros que el umbral se convierten en negro y los más claros en blanco, aislando así las formas de interés.

    Detección de Contornos: Sobre la imagen binarizada, se aplica el algoritmo cv2.findContours de OpenCV. Este algoritmo escanea la imagen y localiza los límites que separan las formas (objetos blancos) del fondo (negro).

    Análisis de Formas: Una vez detectados los contornos, se itera sobre cada uno para extraer métricas clave:

        Momentos de imagen (cv2.moments): Se utilizan para calcular el centro de masa o centroide de cada forma, que nos da su punto central.

        Caja Delimitadora (cv2.boundingRect): Se calcula el rectángulo más pequeño que encierra completamente cada contorno.

        Métricas: Se calcula el número total de formas, el área y el perímetro promedio.

🚀 Resultados Visuales

En el colab se muestra el resultado del proceso en tres etapas clave.
El resultado final muestra los contornos detectados en verde, los centroides como círculos azules y las cajas delimitadoras en rojo.

💻 Código Destacado

El proyecto fue desarrollado en un notebook de Google Colab.

[Solucion Colab](Taller_4.ipynb)

A continuación, los fragmentos de código más importantes:

1. Umbralización Fija

Python

# Cargar la imagen y convertir a escala de grises
image = cv2.imread('formas.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbral fijo para binarizar la imagen
# THRESH_BINARY_INV convierte los objetos de interés a blanco y el fondo a negro.
ret, thresh_fixed = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

2. Detección y Dibujo de Contornos

Python

# Encontrar los contornos externos de las formas
contours, hierarchy = cv2.findContours(thresh_fixed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos sobre una copia de la imagen original
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

3. Cálculo de Centroides y Bounding Boxes

Python

analysis_image = image.copy()

# Iterar sobre cada contorno para analizarlo
for contour in contours:
    # Calcular momentos para encontrar el centroide
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        # Dibujar el centroide
        cv2.circle(analysis_image, (cx, cy), 5, (255, 0, 0), -1)

    # Calcular y dibujar la caja delimitadora (bounding box)
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(analysis_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

🧠 Comentarios Personales

Aprendizaje: Este taller fue una excelente introducción práctica a los fundamentos de la visión por computador. Me pareció sorprendente lo fácil que es implementar un pipeline completo de detección y análisis con una biblioteca tan potente como OpenCV. Las funciones cv2.findContours y cv2.moments abstraen una gran complejidad matemática, permitiendo enfocarse en la lógica del problema.

Dificultades: La principal dificultad, aunque menor en este caso por la simplicidad de la imagen, suele ser la elección del método y valor de umbralización. Una mala elección puede llevar a que los objetos se fusionen o no se detecten correctamente. En imágenes con iluminaciones no uniformes, el umbral fijo no sería suficiente y el umbral adaptativo (cv2.adaptiveThreshold) se vuelve indispensable. Entender la diferencia y cuándo usar cada uno fue un punto clave del aprendizaje.Claro, aquí tienes el archivo README.md documentando el taller, sin incluir la sección de "Bonus" y cumpliendo con todos los requisitos.
