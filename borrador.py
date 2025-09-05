import pygame
import pytmx
import os
from variables import config

# --- 1. Inicializar Pygame y configuración de la ventana ---
pygame.init()
ANCHO_PANTALLA = config.WIDHT
ALTO_PANTALLA = config.HEIGHT
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego con Colisiones y Salto")

# --- 2. Cargar el mapa y los rectángulos de colisión ---
# Asegúrate de que la ruta a tu archivo .tmx sea correcta
try:
    tmx_data = pytmx.load_pygame(r"C:\Users\elpaj\Documents\my_game\assets\img\background\mapas en creacion\map_castle_interior_2.tmx")
except FileNotFoundError:
    print("Error: No se encontró el archivo de mapa. Asegúrate de que la ruta sea correcta.")
    pygame.quit()
    exit()

# Información del mapa para dibujar
ANCHO_TILE = tmx_data.tilewidth
ALTO_TILE = tmx_data.tileheight

# Cargar los rectángulos de colisión de la capa de objetos
collision_rects = []
print("Capas encontradas en el mapa:")
for layer in tmx_data.layers:
    print(f"- {layer.name}")
    if layer.name == "colisiones":
        for obj in layer:
            obj_y_corregida = tmx_data.height * tmx_data.tileheight - obj.y - obj.height
            collision_rects.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

print(f"\nNúmero de rectángulos de colisión cargados: {len(collision_rects)}")

# --- 3. Personaje (ahora un cuadrado) ---
player_rect = pygame.Rect(100, 100, 32, 32)
player_color = (255, 0, 0) # Rojo

# Variables de movimiento
player_speed = 4
gravity = 0.5
jump_strength = -10
dy = 0 # Velocidad vertical
on_ground = False

# --- 4. Funciones de dibujo ---
def draw_map():
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile_image = tmx_data.get_tile_image_by_gid(gid)
                if tile_image:
                    screen.blit(tile_image, (x * ANCHO_TILE, y * ALTO_TILE))


# --- 5. Bucle principal del juego ---
clock = pygame.time.Clock()
running = True

while running:
    # --- Manejo de eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                dy = jump_strength
                on_ground = False

    # --- 6. Lógica de movimiento ---
    keys = pygame.key.get_pressed()
    dx = 0
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dx = -player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dx = player_speed

    # Aplicar gravedad
    dy += gravity

    # --- 7. Detección y respuesta a colisiones (horizontal y vertical) ---

    # Colisiones horizontales
    player_rect.x += dx
    for rect in collision_rects:
        if player_rect.colliderect(rect):
            if dx > 0:  # Moviéndose a la derecha
                player_rect.right = rect.left
            if dx < 0:  # Moviéndose a la izquierda
                player_rect.left = rect.right

            # Lógica de escalada: Si el jugador colisiona y está subiendo
            # Mueve al jugador hacia arriba para que "salte" al siguiente escalón
            # El valor 10 es un ajuste que puedes cambiar para que se sienta bien
            if on_ground:
                player_rect.y -= 10
                dy = 0 # No está cayendo si está escalando

    # Colisiones verticales
    on_ground = False
    player_rect.y += dy
    for rect in collision_rects:
        if player_rect.colliderect(rect):
            if dy > 0:
                player_rect.bottom = rect.top
                dy = 0
                on_ground = True
            if dy < 0:
                player_rect.top = rect.bottom
                dy = 0

    # --- 8. Actualizar pantalla y dibujar ---
    screen.fill((0, 0, 0))
    draw_map()
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.display.flip()
    clock.tick(60)

# --- 9. Salir del juego ---
pygame.quit()