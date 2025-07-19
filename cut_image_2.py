from PIL import Image
import os

def recortar_sprites(imagen_path, salida_dir, total_sprites, nombre_inicio=1):
    imagen = Image.open(imagen_path).convert("RGBA")
    width, height = imagen.size
    sprite_width = width // total_sprites

    if not os.path.exists(salida_dir):
        os.makedirs(salida_dir)

    for i in range(total_sprites):
        frame = imagen.crop((i * sprite_width, 0, (i + 1) * sprite_width, height))
        bbox = frame.getbbox()
        if bbox:
            sprite_recortado = frame.crop(bbox)
            nombre_archivo = f"The_Dead_death_{nombre_inicio + i}.png"
            sprite_recortado.save(os.path.join(salida_dir, nombre_archivo))
            print(f"Guardado: {nombre_archivo}")

# Para el primer archivo con 10 sprites, empieza en 1
recortar_sprites("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\villian\\The_Dead\\complete\\death_part_1.png", "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\villian\\The_Dead\\derecha", total_sprites=10, nombre_inicio=1)

# Para el segundo archivo con 8 sprites, empieza en 11
recortar_sprites("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\villian\\The_Dead\\complete\\death_part_2.png", "C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\players\\villian\\The_Dead\\derecha", total_sprites=8, nombre_inicio=11)
