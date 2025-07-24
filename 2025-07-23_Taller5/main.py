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
    # Seleccionamos un rectángulo desde la fila 100 a la 300 y la columna 150 a la 400.
    # Le asignamos un color azul puro (R=0, G=0, B=255).
    imagen_modificada[100:300, 150:400] = [0, 0, 255]

    # b. Sustituir una región por otra parte de la imagen
    # Definimos una región de origen (por ejemplo, un parche de 100x150 píxeles)
    region_origen = imagen_rgb[50:150, 50:200]
    
    # Copiamos esa región a una nueva ubicación
    # La región de destino debe tener las mismas dimensiones.
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
    # Convertimos la imagen a escala de grises para el histograma de intensidad
    imagen_gris = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2GRAY)

    # a. Calcular el histograma con Matplotlib (más directo)
    plt.figure(figsize=(10, 5))
    plt.title("Histograma de Intensidades (Escala de Grises)")
    plt.hist(imagen_gris.ravel(), 256, [0, 256])
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Cantidad de Píxeles')
    plt.grid(True)
    plt.show()

    # b. Histograma de color con OpenCV y Matplotlib
    colores = ('b', 'g', 'r') # OpenCV carga en BGR
    plt.figure(figsize=(10, 5))
    plt.title("Histograma de Color")
    for i, col in enumerate(colores):
        # cv2.calcHist([imagen], [canal], mask, [tamaño_hist], [rango])
        hist_color = cv2.calcHist([imagen_bgr], [i], None, [256], [0, 256])
        plt.plot(hist_color, color = col)
        plt.xlim([0, 256])
    plt.xlabel('Intensidad de Píxel')
    plt.ylabel('Cantidad de Píxeles')
    plt.legend(['Azul', 'Verde', 'Rojo'])
    plt.grid(True)
    plt.show()

    # --- 5. Aplicar ajustes de brillo y contraste ---
    
    # a. Ajuste manual por ecuación: g(x) = alpha * f(x) + beta
    # alpha: contraste (1.0-3.0), beta: brillo (0-100)
    alpha = 1.5  # Factor de contraste
    beta = 50    # Valor de brillo

    ajuste_manual = np.clip(alpha * imagen_rgb.astype(np.float32) + beta, 0, 255).astype(np.uint8)

    # b. Ajuste con cv2.convertScaleAbs()
    # Esta función hace esencialmente lo mismo de forma optimizada.
    ajuste_opencv = cv2.convertScaleAbs(imagen_bgr, alpha=alpha, beta=beta)
    ajuste_opencv_rgb = cv2.cvtColor(ajuste_opencv, cv2.COLOR_BGR2RGB) # Convertir para mostrar

    # Visualización de los ajustes
    plt.figure(figsize=(18, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(imagen_rgb)
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(ajuste_manual)
    plt.title('Ajuste Manual (Contraste y Brillo)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(ajuste_opencv_rgb)
    plt.title('Ajuste con OpenCV')
    plt.axis('off')
    plt.show()