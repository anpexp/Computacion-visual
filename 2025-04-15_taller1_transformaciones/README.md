# Taller de Transformaciones Geométricas - README

![Ejemplo de transformación](transformacion.gif)

## Descripción
Implementación de transformaciones geométricas (traslación, rotación y escala) en diferentes entornos de programación. Este repositorio contiene ejemplos en Python, Unity, Three.js y Processing.

---

## Implementación en Python (2D)

### Características principales
- Animación de un cuadrado con transformaciones combinadas
- Generación de GIF como resultado
- Uso de coordenadas homogéneas para transformaciones
- Combinación de matrices de transformación

### Código relevante
```python
# Transformaciones aplicadas en cada frame
T = T_translate @ T_rotate @ T_scale  # Orden: Escala → Rotación → Traslación
transformed_points = (T @ points.T).T

# Parámetros animados
tx = 5 * t      # Desplazamiento lineal en X
ty = 3 * t      # Desplazamiento lineal en Y
theta = 2 * np.pi * t  # Rotación completa (360°)
sx = 1 + 2 * t  # Escala de 1 a 3