import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Cargar una imagen a color y convertirla a escala de grises ---

# Cargar la imagen desde un archivo. Asegúrate de tener una imagen en el directorio.
# Puedes usar cualquier imagen (ej. 'perro.jpg', 'paisaje.png')
try:
    img_color = cv2.imread('imagen.jpg')
    if img_color is None:
        raise FileNotFoundError("El archivo 'imagen.jpg' no se encontró. Asegúrate de que la imagen esté en la misma carpeta que el script.")
    
    # OpenCV carga las imágenes en formato BGR. Lo convertimos a RGB para visualizarlo correctamente con Matplotlib.
    img_color_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

    # Convertir la imagen a escala de grises
    img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

except FileNotFoundError as e:
    print(e)
    # Si no se encuentra la imagen, creamos una de reemplazo para que el script no falle.
    img_gris = np.zeros((400, 600), dtype=np.uint8)
    img_color_rgb = np.zeros((400, 600, 3), dtype=np.uint8)
    print("Se ha creado una imagen negra de respaldo para continuar con la ejecución.")


# --- 2. Aplicar filtros convolucionales simples ---

# a) Filtro de Suavizado (Blur) con un kernel de 5x5
# El filtro promedia los píxeles vecinos, lo que resulta en una imagen más suave.
img_blur = cv2.blur(img_gris, (5, 5))

# b) Filtro de Enfoque (Sharpening)
# Este kernel resta los píxeles circundantes del píxel central, realzando las diferencias.
kernel_sharpening = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
img_sharpened = cv2.filter2D(img_gris, -1, kernel_sharpening)


# --- 3. Implementar detección de bordes ---

# a) Filtro de Sobel en los ejes X y Y
# Detecta los bordes verticales (gradiente en X) y horizontales (gradiente en Y).
sobel_x = cv2.Sobel(img_gris, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img_gris, cv2.CV_64F, 0, 1, ksize=5)

# Convertimos de nuevo a 8-bit para poder visualizarlos
sobel_x_abs = cv2.convertScaleAbs(sobel_x)
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# Opcional: Combinar Sobel X y Y para obtener una detección de bordes más completa
sobel_combined = cv2.addWeighted(sobel_x_abs, 0.5, sobel_y_abs, 0.5, 0)

# b) Filtro Laplaciano
# Detecta bordes en todas las direcciones calculando la segunda derivada de la imagen.
laplaciano = cv2.Laplacian(img_gris, cv2.CV_64F)
laplaciano_abs = cv2.convertScaleAbs(laplaciano)


# --- 4. Comparación visual entre métodos ---

# Usaremos Matplotlib para mostrar todas las imágenes en una sola figura y compararlas fácilmente.
plt.style.use('seaborn-v0_8-dark') # Estilo para un mejor aspecto de los gráficos

# Creación de la figura y los subplots
fig, axs = plt.subplots(3, 3, figsize=(15, 12))
fig.suptitle('Taller - Ojos Digitales: Resultados de Visión Artificial', fontsize=20)

# Imagen Original a Color
axs[0, 0].imshow(img_color_rgb)
axs[0, 0].set_title('1. Imagen Original (Color)')
axs[0, 0].axis('off')

# Imagen en Escala de Grises
axs[0, 1].imshow(img_gris, cmap='gray')
axs[0, 1].set_title('2. Imagen en Escala de Grises')
axs[0, 1].axis('off')

# Imagen con Filtro de Suavizado (Blur)
axs[0, 2].imshow(img_blur, cmap='gray')
axs[0, 2].set_title('3. Filtro de Suavizado (Blur)')
axs[0, 2].axis('off')

# Imagen con Filtro de Enfoque (Sharpening)
axs[1, 0].imshow(img_sharpened, cmap='gray')
axs[1, 0].set_title('4. Filtro de Enfoque (Sharpening)')
axs[1, 0].axis('off')

# Detección de Bordes con Sobel en Eje X
axs[1, 1].imshow(sobel_x_abs, cmap='gray')
axs[1, 1].set_title('5. Bordes - Sobel X')
axs[1, 1].axis('off')

# Detección de Bordes con Sobel en Eje Y
axs[1, 2].imshow(sobel_y_abs, cmap='gray')
axs[1, 2].set_title('6. Bordes - Sobel Y')
axs[1, 2].axis('off')

# Detección de Bordes combinando Sobel X y Y
axs[2, 0].imshow(sobel_combined, cmap='gray')
axs[2, 0].set_title('7. Bordes - Sobel Combinado')
axs[2, 0].axis('off')

# Detección de Bordes con Filtro Laplaciano
axs[2, 1].imshow(laplaciano_abs, cmap='gray')
axs[2, 1].set_title('8. Bordes - Laplaciano')
axs[2, 1].axis('off')

# Espacio vacío para mejorar la distribución
axs[2, 2].axis('off')

# Ajustar el espaciado y mostrar la figura
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()