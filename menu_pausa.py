from pygame import *
from variables import config
from buttons import RectButton

def menu_pausa(wn):
    wn_menu = Surface((config.WIDHT, config.HEIGHT))
    wn_menu.set_alpha(180)
    wn_menu.fill((0, 0, 0))
    wn.blit(wn_menu, (0, 0))

    # Texto del título
    font_titulo = font.Font(None, 80)
    text = font_titulo.render("Pausa", True, config.text_color)
    wn.blit(text, (config.WIDHT // 2 - text.get_width() // 2, 150))

    # Botones
    bttn_renaudar = RectButton(config.WIDHT // 2 - 100, 300, 200, 60, config.colorButton)
    bttn_exit = RectButton(config.WIDHT // 2 - 100, 400, 200, 60, (200, 0, 0))

    bttn_renaudar.draw_button(wn, "Renaudar")
    bttn_exit.draw_button(wn, "Salir")

    display.update()

    while True:
        for e in event.get():
            if e.type == QUIT:
                return "salir"
            elif bttn_renaudar.click(e):
                return "renaudar"
            elif bttn_exit.click(e):
                return "menu_principal"

        config.clock.tick(config.FPS)


