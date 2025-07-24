📸 Taller - De Píxels a Coordenadas: Explorando la Imagen como Matriz

Este repositorio contiene la solución completa para el taller "De Píxels a Coordenadas", desarrollado en Python utilizando OpenCV, NumPy y Matplotlib. El objetivo es demostrar cómo una imagen digital es, en esencia, una matriz numérica que podemos manipular directamente para realizar análisis y modificaciones a nivel de píxel.

🖼️ Manipulación de Imagen Realizada

El script realiza un procesamiento secuencial sobre una imagen de entrada para ilustrar conceptos clave de la visión por computador:

    Carga y Conversión de Color: La imagen se carga utilizando OpenCV (en formato BGR) y se convierte a los espacios de color RGB (para una visualización estándar) y HSV (para separar la intensidad de la información de color). Se visualizan todos los canales por separado.

    Modificación por Regiones (Slicing): Se utiliza el slicing de matrices de NumPy para manipular áreas específicas:

        Se dibuja un rectángulo azul en una zona de la imagen, asignando directamente un valor de color [R, G, B] a un subconjunto de la matriz.

        Se copia y pega una región de la imagen en otra ubicación, demostrando cómo se pueden clonar porciones de la matriz.

    Análisis de Histograma: Se calcula y visualiza el histograma de la imagen. Primero, se muestra el histograma de intensidades de la imagen en escala de grises. Luego, se presenta el histograma de color, mostrando la distribución de los canales Rojo, Verde y Azul.

    Ajuste de Brillo y Contraste: Se aplican ajustes de brillo y contraste utilizando dos métodos:

        Manual: A través de la ecuación lineal g(x)=alphacdotf(x)+beta, donde alpha controla el contraste y beta el brillo.

        Función de OpenCV: Usando cv2.convertScaleAbs() para obtener el mismo resultado de forma optimizada.

✨ Resultados Visuales (GIFs)

A continuación se muestran los efectos visuales de las manipulaciones realizadas.


1. Modificación de Regiones con Slicing
Muestra cómo se añade un rectángulo azul y se clona una sección de la imagen.
![alt text](Figure_2.png)

2. Visualización del Histograma de Intensidad
Muestra la imagen en escala de grises y el histograma que representa la distribución de sus píxeles.
![alt text](Figure_3.png)

3. Ajuste de Brillo y Contraste
Compara la imagen original con la versión de brillo y contraste mejorados.
![alt text](Figure_5.png)
💻 Código de la Solución

El taller se resolvió en un único script de Python. Para ejecutarlo, solo necesitas tener las librerías opencv-python, numpy y matplotlib instaladas, y una imagen llamada imagen.jpg en el mismo directorio.
Python

import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Cargar una imagen en color ---
# Carga la imagen desde el archivo. cv2.imread la carga en formato BGR por defecto.
imagen_bgr = cv2.imread('imagen.jpg')

if imagen_bgr is None:
    print("Error: No se pudo cargar la imagen. Asegúrate de que 'imagen.jpg' esté en el mismo directorio.")
else:
    # Convertimos de BGR a RGB para una visualización correcta con Matplotlib
    imagen_rgb = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2RGB)

    # --- 2. Acceder y mostrar los canales RGB y HSV ---
    
    # Canales RGB
    R, G, B = cv2.split(imagen_rgb)

    # Convertir a HSV
    imagen_hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(imagen_hsv)

    # Visualización de canales
    fig, axs = plt.subplots(2, 4, figsize=(18, 8))
    fig.suptitle('Visualización de Canales de Color', fontsize=16)

    axs[0, 0].imshow(imagen_rgb)
    axs[0, 0].set_title('Original RGB')
    axs[0, 0].axis('off')

    axs[0, 1].imshow(R, cmap='gray')
    axs[0, 1].set_title('Canal Rojo (R)')
    axs[0, 1].axis('off')

    axs[0, 2].imshow(G, cmap='gray')
    axs[0, 2].set_title('Canal Verde (G)')
    axs[0, 2].axis('off')

    axs[0, 3].imshow(B, cmap='gray')
    axs[0, 3].set_title('Canal Azul (B)')
    axs[0, 3].axis('off')
    
    axs[1, 0].imshow(imagen_hsv)
    axs[1, 0].set_title('Original HSV')
    axs[1, 0].axis('off')

    axs[1, 1].imshow(H, cmap='gray')
    axs[1, 1].set_title('Canal Matiz (H)')
    axs[1, 1].axis('off')

    axs[1, 2].imshow(S, cmap='gray')
    axs[1, 2].set_title('Canal Saturación (S)')
    axs[1, 2].axis('off')

    axs[1, 3].imshow(V, cmap='gray')
    axs[1, 3].set_title('Canal Valor (V)')
    axs[1, 3].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()


    # --- 3. Utilizar slicing para modificar regiones ---
    imagen_modificada = imagen_rgb.copy()

    # a. Cambiar el color de un área rectangular
    imagen_modificada[100:300, 150:400] = [0, 0, 255]

    # b. Sustituir una región por otra parte de la imagen
    region_origen = imagen_rgb[50:150, 50:200]
    imagen_modificada[350:450, 300:450] = region_origen

    # Visualización de las modificaciones
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(imagen_rgb)
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(imagen_modificada)
    plt.title('Imagen con Regiones Modificadas')
    plt.axis('off')
    plt.show()

    # --- 4. Calcular y visualizar el histograma de intensidades ---
    imagen_gris = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2GRAY)

    # Histograma con Matplotlib
    plt.figure(figsize=(10, 5))
    plt.title("Histograma de Intensidades (Escala de Grises)")
    plt.hist(imagen_gris.ravel(), 256, [0, 256])
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Cantidad de Píxeles')
    plt.grid(True)
    plt.show()

    # --- 5. Aplicar ajustes de brillo y contraste ---
    alpha = 1.5  # Factor de contraste
    beta = 50    # Valor de brillo
    
    # Ajuste con cv2.convertScaleAbs()
    ajuste_opencv = cv2.convertScaleAbs(imagen_bgr, alpha=alpha, beta=beta)
    ajuste_opencv_rgb = cv2.cvtColor(ajuste_opencv, cv2.COLOR_BGR2RGB)

    # Visualización
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(imagen_rgb)
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(ajuste_opencv_rgb)
    plt.title('Ajuste de Brillo y Contraste')
    plt.axis('off')
    plt.show()

✅ Descripción de Prompts Usados

Para la generación de la solución, se utilizó un único prompt principal que detallaba todos los requisitos del taller.

Prompt inicial:

    "Desarrolla la solución del siguiente taller para un entorno de escritorio de python: Taller - De Pixels a Coordenadas: Explorando la Imagen como Matriz
    🔍 Objetivo del taller: Comprender cómo se representa una imagen digital como una matriz numérica y manipular sus componentes a nivel de píxel...
    🔹 Actividades: Cargar una imagen, acceder y mostrar canales RGB y HSV, utilizar slicing para modificar regiones, calcular histograma y aplicar ajustes de brillo y contraste."



💡 Comentarios Personales

Aprendizaje:
Este taller es una excelente introducción práctica a la manipulación de imágenes. El mayor aprendizaje fue interiorizar que cada imagen no es más que un gran array de NumPy. Entender esto desmitifica muchas operaciones de visión por computador. La técnica de slicing es increíblemente poderosa y eficiente para acceder y modificar regiones sin necesidad de bucles. Además, visualizar los canales de color por separado ayuda a comprender cómo se compone la información visual y la utilidad de diferentes espacios de color como HSV.

Dificultades:
La dificultad más común al empezar es la confusión entre los formatos BGR (usado por OpenCV) y RGB (usado por Matplotlib). Si no se realiza la conversión, los colores en las visualizaciones son incorrectos, lo cual puede ser confuso. Otra pequeña dificultad fue asegurar que los tipos de datos fueran los correctos (uint8, float32) al aplicar operaciones manuales de brillo para evitar errores de desbordamiento de datos (overflow), algo que la función cv2.convertScaleAbs maneja internamente.