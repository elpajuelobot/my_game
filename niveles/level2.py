import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pygame import (display, transform, image, Rect, time, key, event, QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN,
                    MOUSEBUTTONUP, mouse)
from variables import config
from personajes import Player, Villain
from random import randint
from objetos import Item, get_cell_from_mouse, draw_inventory, add_to_inventory, inventory
from animaciones import healt_potion, coin, dead_path, villain
from cinematicas.cinematicas import reproducir_cinematica
from menu_pausa import menu_pausa
from niveles.level3 import level3

def level2():
    wn = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero - Nivel 2")
    background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    reproducir_cinematica(wn, "level2", "intro")

    suelo_rect = Rect(0, config.HEIGHT - 50, config.WIDHT, 50)
    collision_rects = [suelo_rect]

    level_complete = False
    while not level_complete:
        hero = Player(5, config.y_player, config.healt_player, 10)
        config.prj_width = 60
        config.prj_height = 60
        enemy = Villain(config.health_enemy, 10, 4, villain("Wizard", config.width_enemy, config.height_enemy), True, Villain.MOVE_GROUND, 100)  # Enemigo más fuerte

        player_won = False
        mostrar_cine = True
        internal_game = True
        can_move = False
        font_countdown = config.text_level_font
        last_key = 0

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

            wn.blit(background, (config.bg_x, config.bg_y))

            hero.update(keys_pressed, config.mouse_pressed, can_move, last_key, collision_rects, enemy)
            hero.draw(wn)
            hero.barra_healt(wn, 3, 4)

            enemy.draw(wn, hero, enemy)
            if can_move:
                enemy.move_towards_player(hero)
            enemy.draw_health_bar(wn)

            if config.show_inventory:
                draw_inventory(wn)
                if config.dragging and config.dragged_item:
                    wn.blit(healt_potion, mouse.get_pos())

            if enemy.health <= 0:
                enemy.is_dead = True

            if enemy.is_dead and not enemy.visible:
                player_won = True
                internal_game = False

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
                    return

            wn.blit(background, (config.bg_x, config.bg_y))
            hero.draw(wn)
            hero.barra_healt(wn, 3, 4)
            enemy.draw(wn, hero, enemy)
            enemy.draw_health_bar(wn)

            display.update()

        if not config.game:
            break

        if mostrar_cine:
            if player_won:
                reproducir_cinematica(wn, "level2", "ending_win")
            else:
                reproducir_cinematica(wn, "level2", "ending_lose")

        if player_won:
            level_complete = True
            level3()
