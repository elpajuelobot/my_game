from PIL import Image
import os

def recortar_sprites(imagen_path, salida_dir, columnas, filas):
    """
    Recorta automáticamente los sprites de un spritesheet con múltiples filas y columnas,
    eliminando los espacios transparentes.

    :param imagen_path: Ruta a la imagen del spritesheet.
    :param salida_dir: Carpeta donde se guardarán los sprites recortados.
    :param columnas: Número de sprites por fila.
    :param filas: Número de filas de sprites.
    """
    imagen = Image.open(imagen_path).convert("RGBA")
    width, height = imagen.size
    sprite_width = width // columnas
    sprite_height = height // filas

    if not os.path.exists(salida_dir):
        os.makedirs(salida_dir)

    contador = 0
    for fila in range(filas):
        for columna in range(columnas):
            # Recortar sprite base
            left = columna * sprite_width
            upper = fila * sprite_height
            right = left + sprite_width
            lower = upper + sprite_height
            frame = imagen.crop((left, upper, right, lower))

            # Recortar bordes transparentes
            bbox = frame.getbbox()
            if bbox:
                sprite_recortado = frame.crop(bbox)
                nombre_archivo = f"portal_rojo_{contador + 1}.png"
                sprite_recortado.save(os.path.join(salida_dir, nombre_archivo))
                print(f"Guardado: {nombre_archivo}")
                contador += 1

# Ejemplo de uso
ruta_imagen = "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\effects\\complete\\13_vortex_spritesheet_adapted.png"
carpeta_salida = "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\effects"
columnas = 8  # número de sprites por fila
filas = 7    # número de filas

recortar_sprites(ruta_imagen, carpeta_salida, columnas, filas)
