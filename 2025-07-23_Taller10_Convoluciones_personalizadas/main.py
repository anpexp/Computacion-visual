import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- Paso 1: Implementar la Convolución 2D Manualmente ---
def manual_convolution(image, kernel):
    """
    Aplica una convolución 2D a una imagen utilizando un kernel específico.

    Args:
        image (np.array): La imagen de entrada en escala de grises.
        kernel (np.array): El kernel (matriz de convolución).

    Returns:
        np.array: La imagen resultante después de la convolución.
    """
    # Obtener dimensiones de la imagen y el kernel
    img_height, img_width = image.shape
    kernel_height, kernel_width = kernel.shape

    # Calcular el padding necesario para manejar los bordes
    pad_h = kernel_height // 2
    pad_w = kernel_width // 2

    # Crear una imagen de salida inicializada a ceros
    output_image = np.zeros_like(image)

    # Añadir padding a la imagen original para que el kernel pueda operar en los bordes
    padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Iterar sobre cada píxel de la imagen (sin el padding)
    for y in range(img_height):
        for x in range(img_width):
            # Extraer la región de interés (ROI) que coincide con el tamaño del kernel
            # El +1 es para asegurar que se incluye el índice final en el slicing
            roi = padded_image[y:y + kernel_height, x:x + kernel_width]

            # Aplicar la convolución: multiplicación elemento a elemento y suma
            pixel_value = np.sum(roi * kernel)

            # Asignar el valor calculado al píxel correspondiente en la imagen de salida
            output_image[y, x] = pixel_value

    return output_image

# --- Paso 2: Cargar la Imagen ---
# Para este ejemplo, crearemos una imagen de prueba si no se encuentra una local.
try:
    # Intenta cargar una imagen llamada 'test_image.jpg'
    gray_image = cv2.imread('test_image.jpg', cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        raise FileNotFoundError
except FileNotFoundError:
    print("No se encontró 'test_image.jpg'. Creando una imagen de prueba.")
    # Crea una imagen sintética con un cuadrado blanco sobre fondo negro
    gray_image = np.zeros((256, 256), dtype=np.uint8)
    cv2.rectangle(gray_image, (50, 50), (200, 200), 255, -1)
    cv2.putText(gray_image, 'TEST', (75, 140), cv2.FONT_HERSHEY_SIMPLEX, 1.5, 0, 3)


# --- Paso 3: Diseñar los Kernels ---

# Kernel de Enfoque (Sharpening)
# Realza los bordes y detalles. La suma de sus elementos es 1.
sharpen_kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

# Kernel de Suavizado (Box Blur)
# Promedia los píxeles vecinos, resultando en un efecto de desenfoque.
# La suma de sus elementos es 1 para mantener el brillo.
blur_kernel = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

# Kernel de Detección de Bordes (Laplaciano)
# Detecta áreas con cambios rápidos de intensidad.
# La suma de sus elementos es 0.
edge_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# --- Paso 4: Aplicar los Filtros ---

# Aplicación de los filtros con la función manual
manual_sharpened = manual_convolution(gray_image, sharpen_kernel)
manual_blurred = manual_convolution(gray_image, blur_kernel)
manual_edges = manual_convolution(gray_image, edge_kernel)

# Aplicación de los mismos filtros con la función de OpenCV para comparación
opencv_sharpened = cv2.filter2D(src=gray_image, ddepth=-1, kernel=sharpen_kernel)
opencv_blurred = cv2.filter2D(src=gray_image, ddepth=-1, kernel=blur_kernel)
opencv_edges = cv2.filter2D(src=gray_image, ddepth=-1, kernel=edge_kernel)


# --- Paso 5: Comparar y Mostrar Resultados ---

# Configurar el lienzo para mostrar 7 imágenes: 1 original + 3 manuales + 3 de OpenCV
plt.style.use('seaborn-v0_8-dark')
fig, axes = plt.subplots(3, 3, figsize=(14, 14))
fig.suptitle('🧪 Taller: Comparación de Convoluciones Manuales vs. OpenCV', fontsize=20, y=0.95)

# Títulos para cada imagen
titles = [
    'Original', 'Enfoque (Manual)', 'Enfoque (OpenCV)',
    'Suavizado (Manual)', 'Suavizado (OpenCV)', 'Bordes (Manual)',
    'Bordes (OpenCV)'
]
images = [
    gray_image, manual_sharpened, opencv_sharpened,
    manual_blurred, opencv_blurred, manual_edges,
    opencv_edges
]

# Colocar la imagen original en el centro de la primera fila
axes[0, 0].set_visible(False)
axes[0, 1].imshow(gray_image, cmap='gray')
axes[0, 1].set_title('Imagen Original', fontsize=14)
axes[0, 1].axis('off')
axes[0, 2].set_visible(False)

# Mostrar los resultados de enfoque
axes[1, 0].imshow(manual_sharpened, cmap='gray')
axes[1, 0].set_title('Enfoque (Manual)', fontsize=12)
axes[1, 0].axis('off')

axes[1, 1].imshow(opencv_sharpened, cmap='gray')
axes[1, 1].set_title('Enfoque (OpenCV)', fontsize=12)
axes[1, 1].axis('off')

# Mostrar los resultados de suavizado
axes[1, 2].imshow(manual_blurred, cmap='gray')
axes[1, 2].set_title('Suavizado (OpenCV)', fontsize=12)
axes[1, 2].axis('off')

axes[2, 0].imshow(manual_blurred, cmap='gray')
axes[2, 0].set_title('Suavizado (Manual)', fontsize=12)
axes[2, 0].axis('off')


# Mostrar los resultados de detección de bordes
axes[2, 1].imshow(manual_edges, cmap='gray')
axes[2, 1].set_title('Bordes (Manual)', fontsize=12)
axes[2, 1].axis('off')

axes[2, 2].imshow(opencv_edges, cmap='gray')
axes[2, 2].set_title('Bordes (OpenCV)', fontsize=12)
axes[2, 2].axis('off')


plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()