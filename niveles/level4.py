import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pygame import (display, transform, image, Rect, time, key, event, QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN,
                    MOUSEBUTTONUP, K_e, K_w)
from variables import config
from personajes import Player, Npc
from animaciones import dead_path, teclado
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
    map_data, tile_w, tile_h = files_and_var(1)
    map_data2, tile_w2, tile_h2 = files_and_var(2)
    map_data3, tile_w3, tile_h3 = files_and_var(3)
    castle_door_hitbox_map2 = Rect(430, 250, 148, 110)
    castle_door_hitbox = Rect(800, 562, 40, 140)
    teclas = teclado()
    img_e = teclas['tecla_e']
    img_e_pressed = teclas['tecla_e_pressed']
    img_w = teclas['tecla_w']
    img_w_pressed = teclas['tecla_w_pressed']
    PROXIMITY = 100
    castle_open = False
    request_open = False
    hidden = {"puerta_abierta"}
    suelo_rect = Rect(0, config.HEIGHT - 50, config.WIDHT, 50)
    collision_rects = [suelo_rect]

    level_complete = False
    while not level_complete:
        hero = Player(5, config.y_player, config.healt_player, 10)
        king = Npc(x=821, y=216, width=20.5, height=37.5, name="king", to_x=474, to_y=216, speed=1)
        config.prj_width = 60
        config.prj_height = 60

        player_won = False
        mostrar_cine = True
        internal_game = True
        can_move = False
        font_countdown = config.text_level_font
        last_key = 0
        new_map = False
        map = 1
        castle_map_initialized = False
        new_x = False
        initialized_map_3 = False
        door_dist = False

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
                    hero.y = 290
                    if not new_x:
                        hero.x = 5
                    elif new_x:
                        hero.x = 990
                    hero.set_size(20.5, 37.5)
                    collision_rects.clear()
                    if map == 1:
                        build_collisions(collision_rects, map_data)
                    elif map == 2:
                        build_collisions(collision_rects, map_data2)
                    elif map == 3:
                        build_collisions(collision_rects, map_data3)
                    castle_map_initialized = True
                    new_x = False

                if map == 2:
                    if castle_open:
                        hidden.discard("puerta_abierta")
                    else:
                        hidden.add("puerta_abierta")

                if map == 1:
                    draw_map(wn, map_data, tile_w, tile_h)
                elif map == 2:
                    draw_map(wn, map_data2, tile_w2, tile_h2, hidden)
                elif map == 3:
                    draw_map(wn, map_data3, tile_w3, tile_h3)

            if hero.hitbox_player.x >= 995 and map == 1:
                map = 2
                castle_map_initialized = False
            elif hero.hitbox_player.x <= 3 and map == 2:
                map = 1
                castle_map_initialized = False
                new_x = True
            elif initialized_map_3:
                map = 3
                castle_map_initialized = False
                new_x = False
                initialized_map_3 = False

            hero.update(keys_pressed, config.mouse_pressed, can_move, last_key, collision_rects)
            hero.draw(wn)
            hero.barra_healt(wn, 3, 4)

            if map == 3:
                king.update(hero)
                king.draw(wn, "level4", "charla_rey")

                if king.finish_npc_work:
                    internal_game = False
                    player_won = True
                    king.finish_npc_work = False

            if not new_map:
                door_hitbox = castle_door_hitbox
                door_dist = True
            elif map == 2:
                door_hitbox = castle_door_hitbox_map2
                door_dist = True
            else:
                door_dist = False

            if door_dist:
                dist = math.hypot(hero.hitbox_player.centerx - door_hitbox.centerx,
                                hero.hitbox_player.centery - door_hitbox.centery)

                if dist <= PROXIMITY:
                    if not castle_open:
                        if keys_pressed[K_e]:
                            prompt = img_e_pressed
                        else:
                            prompt = img_e
                    else:
                        if keys_pressed[K_w]:
                            castle_open = False
                            prompt = img_w_pressed
                            if not new_map:
                                new_map = True
                            if map == 2:
                                initialized_map_3 = True
                        else:
                            prompt = img_w

                    px = door_hitbox.centerx - prompt.get_width() // 2
                    py = door_hitbox.centery - prompt.get_height() - 8
                    wn.blit(prompt, (px, py))

                if request_open and dist <= PROXIMITY:
                    castle_open = True
                request_open = False

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

        if not config.game:
            break

        if mostrar_cine:
            if player_won:
                reproducir_cinematica(wn, "level4", "ending")

        if player_won:
            level_complete = True

level4()
