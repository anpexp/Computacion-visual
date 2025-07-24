# -*- coding: utf-8 -*-
"""
Solución al Taller - Rasterización desde Cero (Versión Multi-Imagen)
"""

# Importar librerías necesarias
from PIL import Image
import matplotlib.pyplot as plt

# ✅ 1. Preparar el entorno de dibujo
width, height = 200, 200

# --- Definición de los Algoritmos Modificados ---

def bresenham(pixels, x0, y0, x1, y1):
    """
    Dibuja una línea roja en el objeto 'pixels' proporcionado.
    """
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        if 0 <= x0 < width and 0 <= y0 < height:
            pixels[x0, y0] = (255, 0, 0)  # Rojo
        
        if x0 == x1 and y0 == y1:
            break
            
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

def midpoint_circle(pixels, x0, y0, radius):
    """
    Dibuja un círculo azul en el objeto 'pixels' proporcionado.
    """
    x = radius
    y = 0
    p = 1 - radius
    
    while x >= y:
        for dx, dy in [(x, y), (y, x), (-x, y), (-y, x), (-x, -y), (-y, -x), (x, -y), (y, -x)]:
            if 0 <= x0 + dx < width and 0 <= y0 + dy < height:
                pixels[x0 + dx, y0 + dy] = (0, 0, 255)  # Azul
        
        y += 1
        if p <= 0:
            p = p + 2*y + 1
        else:
            x -= 1
            p = p + 2*y - 2*x + 1

def fill_triangle(pixels, p1, p2, p3):
    """
    Rellena un triángulo verde en el objeto 'pixels' proporcionado.
    """
    pts = sorted([p1, p2, p3], key=lambda p: p[1])
    (x1, y1), (x2, y2), (x3, y3) = pts

    def interpolate(y_start, y_end, x_start, x_end):
        if y_end == y_start: return []
        slope = (x_end - x_start) / (y_end - y_start)
        return [int(x_start + slope * (y - y_start)) for y in range(y_start, y_end)]

    if y1 == y3: return # Evitar división por cero en triángulos horizontales
    
    x12 = interpolate(y1, y2, x1, x2)
    x23 = interpolate(y2, y3, x2, x3)
    x13 = interpolate(y1, y3, x1, x3)
    
    x_left = x12 + x23
    x_right = x13

    for y in range(y1, y3):
        idx = y - y1
        if idx < len(x_left) and idx < len(x_right):
            xl = x_left[idx]
            xr = x_right[idx]
            for x in range(min(xl, xr), max(xl, xr) + 1):
                if 0 <= x < width and 0 <= y < height:
                    pixels[x, y] = (0, 255, 0)  # Verde

# --- Creación y Dibujo en Imágenes Separadas ---

# 🖼️ Imagen 1: Línea
image_line = Image.new('RGB', (width, height), 'white')
pixels_line = image_line.load()
bresenham(pixels_line, 20, 20, 180, 120)

# 🖼️ Imagen 2: Círculo
image_circle = Image.new('RGB', (width, height), 'white')
pixels_circle = image_circle.load()
midpoint_circle(pixels_circle, 100, 100, 40)

# 🖼️ Imagen 3: Triángulo
image_triangle = Image.new('RGB', (width, height), 'white')
pixels_triangle = image_triangle.load()
fill_triangle(pixels_triangle, (30, 50), (100, 150), (160, 60))

print("✅ ¡Tres imágenes generadas con éxito!")

# ✅ 5. Mostrar los resultados en una sola figura
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Mostrar la línea
axs[0].imshow(image_line)
axs[0].set_title('1. Línea (Bresenham)', fontsize=14)
axs[0].axis('off')

# Mostrar el círculo
axs[1].imshow(image_circle)
axs[1].set_title('2. Círculo (Punto Medio)', fontsize=14)
axs[1].axis('off')

# Mostrar el triángulo
axs[2].imshow(image_triangle)
axs[2].set_title('3. Triángulo (Scanline)', fontsize=14)
axs[2].axis('off')

plt.tight_layout()
plt.show()