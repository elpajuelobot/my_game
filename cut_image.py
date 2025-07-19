from PIL import Image
import os

def recortar_sprites(imagen_path, salida_dir, num_sprites):
    """
    Recorta automáticamente los sprites de un spritesheet eliminando los espacios transparentes.

    :param imagen_path: Ruta a la imagen del spritesheet.
    :param salida_dir: Carpeta donde se guardarán los sprites recortados.
    :param num_sprites: Número de sprites en la fila.
    """
    imagen = Image.open(imagen_path).convert("RGBA")
    width, height = imagen.size
    sprite_width = width // num_sprites

    if not os.path.exists(salida_dir):
        os.makedirs(salida_dir)

    for i in range(num_sprites):
        # Recortar sprite base
        frame = imagen.crop((i * sprite_width, 0, (i + 1) * sprite_width, height))

        # Recortar bordes transparentes
        bbox = frame.getbbox()
        if bbox:
            sprite_recortado = frame.crop(bbox)
            nombre_archivo = f"_CrouchWalk_{i + 1}.png"
            sprite_recortado.save(os.path.join(salida_dir, nombre_archivo))
            print(f"Guardado: {nombre_archivo}")

# Ejemplo de uso
ruta_imagen = "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\hero\\complete\\_CrouchWalk.png"
carpeta_salida = "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\hero\\derecha"
numero_de_sprites = 8

recortar_sprites(ruta_imagen, carpeta_salida, numero_de_sprites)
