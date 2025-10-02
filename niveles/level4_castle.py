from pygame import Rect
import pytmx

def files_and_var(map):
    # Archivo del mapa
    if map == 1:
        tmx_data = pytmx.load_pygame(r"C:\Users\elpaj\Documents\my_game\assets\img\background\mapas en creacion\map_castle_interior_final_version.tmx")
    elif map == 2:
        tmx_data = pytmx.load_pygame(r"C:\Users\elpaj\Documents\my_game\assets\img\background\mapas en creacion\map_castle_interior_2.tmx")
    elif map == 3:
        tmx_data = pytmx.load_pygame(r"C:\Users\elpaj\Documents\my_game\assets\img\background\mapas en creacion\map_king_trone.tmx")
    else:
        print("Error")

    # Variables necesarias
    ANCHO_TILE = tmx_data.tilewidth
    ALTO_TILE = tmx_data.tileheight

    return tmx_data, ALTO_TILE, ANCHO_TILE

def build_collisions(collision_rects, map_data):
    print("Capas encontradas en el mapa:") # Línea DEBUG 
    for layer in map_data.layers:
        print(f"- {layer.name}") # Línea DEBUG 
        if layer.name == "colisiones":
            for obj in layer:
                collision_rects.append(Rect(obj.x, obj.y, obj.width, obj.height))

    print(f"\nNúmero de rectángulos de colisión cargados: {len(collision_rects)}") # Línea DEBUG 

def draw_map(wn, map_data, tile_w, tile_h, hidden_layers=None):
    if hidden_layers is None:
        hidden_layers = set()

    for layer in map_data.layers:
        name = getattr(layer, "name", None)
        if name in hidden_layers:
            continue

        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                if gid == 0:
                    continue
                tile_image = map_data.get_tile_image_by_gid(gid)
                if tile_image:
                    wn.blit(tile_image, (x * tile_w, y * tile_h))
