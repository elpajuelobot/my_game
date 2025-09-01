from pygame import *
from buttons import RectButton, CircleButton
from menu_opciones import menu_opciones
from variables import config
from niveles.level1 import level1
from niveles.level2 import level2
from niveles.level3 import level3

def levels():
    wn_menu_levels = display.set_mode((config.WIDHT, config.HEIGHT))
    display.set_caption("El caballero")
    background_image = transform.scale(image.load("assets/img/background/area juego/background.png").convert(), (1024, 768))

    # Botones
    bttnLevel1 = CircleButton(100, config.HEIGHT//2, 50, config.colorButton)
    bttnLevel2 = CircleButton(275, config.HEIGHT//3, 50, config.colorButton)
    bttnLevel3 = CircleButton(350, config.HEIGHT//8, 50, config.colorButton)
    bttnBack = RectButton(0, 0, 100, 50, config.colorButton)

    while config.menu_niveles:
        # FPS
        config.clock.tick(config.FPS)

        # Imagen de fondo
        wn_menu_levels.blit(background_image, (config.bg_x, config.bg_y))

        for e in event.get():
            if e.type == QUIT:
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = False

            elif bttnLevel1.click(e):
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = True
                level1()

            elif bttnLevel2.click(e):
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = True
                level2()

            elif bttnLevel3.click(e):
                config.menu_niveles = False
                config.menu_opciones = False
                config.menu_principal = False
                config.game = True
                level3()

            elif bttnBack.click(e):
                config.menu_niveles = False
                config.menu_principal = True
                config.menu_opciones = False
                config.game = False

        draw.line(wn_menu_levels, (255, 255, 255),
                (bttnLevel1.x + bttnLevel1.radio, bttnLevel1.y + bttnLevel1.radio),
                (bttnLevel2.x + bttnLevel2.radio, bttnLevel2.y + bttnLevel2.radio), 7)
        draw.line(wn_menu_levels, (255, 255, 255),
                (bttnLevel2.x + bttnLevel2.radio, bttnLevel2.y + bttnLevel2.radio),
                (bttnLevel3.x + bttnLevel3.radio, bttnLevel3.y + bttnLevel3.radio), 7)
        bttnLevel1.draw(wn_menu_levels, "Nivel1")
        bttnLevel2.draw(wn_menu_levels, "Nivel2")
        bttnLevel3.draw(wn_menu_levels, "Nivel3")
        bttnBack.draw_button(wn_menu_levels, "<--")

        display.update()

