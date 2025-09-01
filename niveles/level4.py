import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pygame import *
from variables import config
from personajes import Player
from random import randint
from animaciones import healt_potion, coin, dead_path, teclado
from cinematicas.cinematicas import reproducir_cinematica
from menu_pausa import menu_pausa
import math
from niveles.level4_castle import build_collisions, draw_map, files_and_var

def level4():
    wn = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero - Nivel 3")
    background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))
    castle_1 = transform.scale(image.load("assets/img/background/castle_01.png").convert_alpha(), (500, 500))
    castle_2 = transform.scale(image.load("assets/img/background/castle_02.png").convert_alpha(), (500, 500))
    grass_superior = transform.scale(image.load("assets/img/background/area juego/background descompuesto/Layer_0000_9.png").convert_alpha(), (1024, 768))
    castle_door_hitbox = Rect(800, 562, 40, 140)
    map_data, tile_w, tile_h = files_and_var()
    teclas = teclado()
    img_e = teclas['tecla_e']
    img_e_pressed = teclas['tecla_e_pressed']
    img_w = teclas['tecla_w']
    img_w_pressed = teclas['tecla_w_pressed']
    PROXIMITY = 100
    castle_open = False
    request_open = False

    #reproducir_cinematica(wn, "level3", "intro")

    suelo_rect = Rect(0, config.HEIGHT - 50, config.WIDHT, 50)
    collision_rects = [suelo_rect]

    level_complete = False
    while not level_complete:
        hero = Player(5, config.y_player, config.healt_player, 10)
        config.prj_width = 60
        config.prj_height = 60

        player_won = False
        mostrar_cine = True
        internal_game = True
        can_move = False
        font_countdown = config.text_level_font
        last_key = 0
        new_map = False
        castle_map_initialized = False

        # Tiempo de espera
        start_time = time.get_ticks()

        while internal_game:
            keys_pressed = key.get_pressed()
            config.clock.tick(config.FPS)

            # Tiempo de espera
            current_time = time.get_ticks()
            if current_time - start_time >= config.delay_inicial:
                can_move = True

            for e in event.get():
                if e.type == QUIT:
                    config.game = False
                    internal_game = False
                    level_complete = True
                    mostrar_cine = False

                elif e.type == KEYDOWN:
                    last_key = e.key

                elif e.type == KEYDOWN and e.key == K_ESCAPE:
                    resultado = menu_pausa(wn)
                    if resultado == "menu_principal":
                        config.menu_principal = True
                        config.game = False
                        internal_game = False
                        level_complete = True

                elif e.type == MOUSEBUTTONDOWN:
                    if e.button == 1:
                        config.mouse_pressed = True
                elif e.type == MOUSEBUTTONUP:
                    if e.button == 1:
                        config.mouse_pressed = False

                if hero.health > 0:
                    if e.type == KEYDOWN and e.key == K_e and hero.health > 0:
                        request_open = True

            if not new_map:
                wn.blit(background, (config.bg_x, config.bg_y))
                if castle_open:
                    wn.blit(castle_2, (570, 220))
                else:
                    wn.blit(castle_1, (570, 220))
                wn.blit(grass_superior, (config.bg_x, config.bg_y - 5))
            else:
                if not castle_map_initialized:
                    hero.y = 10
                    hero.x = 5
                    hero.set_size(20.5, 37.5)
                    collision_rects.clear()
                    build_collisions(collision_rects, map_data)
                    castle_map_initialized = True

                draw_map(wn, map_data, tile_w, tile_h)

            hero.update(keys_pressed, config.mouse_pressed, can_move, last_key, collision_rects)
            hero.draw(wn)
            hero.barra_healt(wn, 3, 4)

            dist = math.hypot(hero.hitbox_player.centerx - castle_door_hitbox.centerx,
                            hero.hitbox_player.centery - castle_door_hitbox.centery)

            if dist <= PROXIMITY:
                if not castle_open:
                    if keys_pressed[K_e]:
                        prompt = img_e_pressed
                    else:
                        prompt = img_e
                else:
                    if keys_pressed[K_w]:
                        prompt = img_w_pressed
                        new_map = True
                    else:
                        prompt = img_w

                px = castle_door_hitbox.centerx - prompt.get_width() // 2
                py = castle_door_hitbox.centery - prompt.get_height() - 8
                wn.blit(prompt, (px, py))

            if request_open and dist <= PROXIMITY:
                castle_open = True
            request_open = False

            if hero.health <= 0:
                hero.is_death = True
                if hero.death_count >= len(dead_path) * 5 and hero.death_timer != 0 and time.get_ticks() - hero.death_timer > 3000:
                    player_won = False
                    internal_game = False

            # Cuenta atrás inicial
            elapsed = time.get_ticks() - start_time
            remaining = max(0, (config.delay_inicial - elapsed) // 1000 + 1)

            if remaining > 0:
                countdown_text = font_countdown.render(str(remaining), True, config.text_color)
                rect = countdown_text.get_rect(center=(config.WIDHT // 2, config.HEIGHT // 2))
                wn.blit(countdown_text, rect)
            else:
                can_move = True

            display.update()

        end_time = time.get_ticks()
        while time.get_ticks() - end_time < config.delay_final:
            config.clock.tick(config.FPS)
            for e in event.get():
                if e.type == QUIT:
                    config.game = False
                    break

            wn.blit(background, (config.bg_x, config.bg_y))
            hero.draw(wn)
            hero.barra_healt(wn, 3, 4)

            display.update()

        if not config.game:
            break

        if mostrar_cine:
            if player_won:
                reproducir_cinematica(wn, "level3", "ending_win")
            else:
                reproducir_cinematica(wn, "level3", "ending_lose")

        if player_won:
            level_complete = True

level4()
