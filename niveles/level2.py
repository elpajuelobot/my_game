import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pygame import *
from variables import config
from personajes import Player, Villain
from random import randint
from objetos import Item, get_cell_from_mouse, draw_inventory, add_to_inventory, inventory
from animaciones import healt_potion, coin, dead_path
from cinematicas.cinematicas import reproducir_cinematica
from menu_pausa import menu_pausa

def level2():
    wn = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero - Nivel 2")
    background = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    reproducir_cinematica(wn, "level2", "intro")

    level_complete = False
    while not level_complete:
        hero = Player()
        enemy = Villain(randint(4, 6))  # Enemigo más fuerte

        player_won = False
        mostrar_cine = True
        internal_game = True
        paused = False

        while internal_game:
            keys_pressed = key.get_pressed()
            config.clock.tick(config.FPS)

            for e in event.get():
                if e.type == QUIT:
                    config.game = False
                    internal_game = False
                    level_complete = True
                    mostrar_cine = False

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
                    if e.type == KEYDOWN and e.key == K_e:
                        config.show_inventory = not config.show_inventory
                        config.dragging = False
                        config.dragged_item = None

                if config.show_inventory:
                    if e.type == MOUSEBUTTONDOWN:
                        cell = get_cell_from_mouse(e.pos)
                        if cell:
                            row, col = cell
                            if inventory[row][col]:
                                config.dragging = True
                                config.dragged_item = inventory[row][col].copy()
                                inventory[row][col] = None

                    elif e.type == MOUSEBUTTONUP:
                        if config.dragging:
                            cell = get_cell_from_mouse(e.pos)
                            if cell:
                                row, col = cell
                                if inventory[row][col] is None:
                                    inventory[row][col] = config.dragged_item
                                else:
                                    if inventory[row][col]["name"] == config.dragged_item["name"]:
                                        inventory[row][col]["quantity"] += config.dragged_item["quantity"]
                                    else:
                                        if inventory[row][col] != config.dragged_item:
                                            inventory[row][col], config.dragged_item = config.dragged_item, inventory[row][col]
                            config.dragging = False
                            config.dragged_item = None

            config.x_relativa = config.bg_x % config.WIDHT
            wn.blit(background, (config.x_relativa - config.WIDHT, config.bg_y))
            wn.blit(background, (config.x_relativa, config.bg_y))

            hero.move_player(keys_pressed, config.mouse_pressed)
            hero.draw(wn, enemy)
            hero.barra_healt(wn, 3, 4)

            enemy.draw(wn, hero)
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
