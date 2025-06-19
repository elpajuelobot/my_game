import pygame
import sys
import json
from variables import config

pygame.font.init()
font = pygame.font.Font(None, 35)

def render_multiline_text(text, font, color, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    surfaces = [font.render(line, True, color) for line in lines]
    return surfaces

def cargar_cinematica(nivel, tipo):
    with open("assets/data/cinematicas.json", "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    escenas = data.get(nivel, {}).get(tipo, [])
    return escenas

def spritesImages(rutaJson):
    with open(rutaJson, "r", encoding="utf-8") as images:
        rutas = json.load(images)

    imagenes = {}
    for nombre, ruta in rutas.items():
        imagenes[nombre] = pygame.image.load(ruta).convert_alpha()
    return imagenes

def run_cinematic(screen, escenas):
    background = pygame.transform.scale(pygame.image.load("assets/img/background/area juego/background.png").convert(), (config.WIDHT, config.HEIGHT))

    imagenes_personajes = spritesImages("assets/data/sprites.json")

    index = 0
    start_time = pygame.time.get_ticks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key in [pygame.K_SPACE, pygame.K_RETURN]:
                index += 1
                start_time = pygame.time.get_ticks()
                if index >= len(escenas):
                    running = False

        if index >= len(escenas):
            running = False
            break

        escena = escenas[index]
        mensaje = escena["texto"]
        personaje = escena.get("personaje", "caballero")
        duracion = escena.get("duracion", 5)

        if pygame.time.get_ticks() - start_time > duracion * 1000:
            index += 1
            start_time = pygame.time.get_ticks()
            if index >= len(escenas):
                running = False
                break

        screen.blit(background, (0, 0))

        if personaje in imagenes_personajes:
            personaje_img = imagenes_personajes.get(personaje)
            personaje_img = pygame.transform.scale(personaje_img, (800, 800))
            crop_height = int(personaje_img.get_height() * 0.7)
            personaje_crop = personaje_img.subsurface(0, 0, personaje_img.get_width(), crop_height)
            screen.blit(personaje_crop, (-200, config.HEIGHT - personaje_crop.get_height()))

        text_x = 400
        text_y = config.HEIGHT // 4
        max_width = config.WIDHT - text_x - 60

        nombre_surface = font.render(personaje.capitalize(), True, (255, 255, 0))
        screen.blit(nombre_surface, (text_x, text_y - 50))
        surfaces = render_multiline_text(mensaje, font, (255, 255, 255), max_width)
        bg_height = sum(s.get_height() + 10 for s in surfaces) + 20
        bg_surface = pygame.Surface((max_width + 40, bg_height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 180))
        screen.blit(bg_surface, (text_x - 20, text_y - 20))

        offset_y = text_y
        for s in surfaces:
            screen.blit(s, (text_x, offset_y))
            offset_y += s.get_height() + 10

        pygame.display.flip()
        config.clock.tick(config.FPS)

def reproducir_cinematica(screen, nivel, tipo):
    escenas = cargar_cinematica(nivel, tipo)
    if escenas:
        run_cinematic(screen, escenas)
