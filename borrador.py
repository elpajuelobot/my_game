import pygame # Asegúrate de importar pygame
from pygame import *
from variables import config
from animaciones import * # Asumo que aquí están dead_right_villain, attack_right_villain, run_right_villain, etc.

class Villain:
    def __init__(self, speed):
        self.x = config.x_enemy
        self.y = config.y_enemy
        self.hitbox_enemy = Rect(self.x, self.y, config.width_enemy, config.height_enemy)
        self.standing = stand_right_villain  # Imagen de pie por defecto
        self.walk_count = 0
        self.moving_right = False
        self.moving_left = False
        self.is_attack = False
        self.attack_count = 0
        self.health = config.health_enemy
        self.is_dead = False # Se mantiene para la compatibilidad con level1.py, pero el estado principal es 'state'
        self.visible = True
        self.is_stand = False
        self.num_hurt = 4
        self.speed = speed

        # --- VARIABLES PARA EL SISTEMA DE ESTADOS Y ANIMACIÓN DE MUERTE ---
        self.STATE_ALIVE = 0
        self.STATE_DYING = 1
        self.STATE_DEAD = 2
        self.state = self.STATE_ALIVE # El estado inicial es vivo

        self.time_of_death_start = 0 # Para controlar cuándo empezó la animación de muerte
        self.death_animation_duration = len(dead_right_villain) * config.ANIMATION_SPEED # Duración en "ticks" del juego
        self.current_death_frame = 0 # Para el índice del frame de muerte actual
        self.last_frame_update = 0 # Para controlar la velocidad de la animación de muerte

        self.dead_x = 0  # Posición X en la que el enemigo muere
        self.dead_y = 0  # Posición Y en la que el enemigo muere (normalmente la misma que self.y)
        self.death_bg_x_offset = 0 # Offset del fondo (config.bg_x) cuando el enemigo muere

    # --- MÉTODO: take_damage (Maneja la lógica de recibir daño y morir) ---
    def take_damage(self, amount):
        if self.state == self.STATE_ALIVE: # Solo recibe daño si está vivo
            self.health -= amount
            if self.health <= 0:
                self.health = 0 # Asegurarse de que no sea negativo
                self.state = self.STATE_DYING # Cambiar a estado muriendo
                self.is_dead = True # Mantener por compatibilidad con level1.py si es que lo usa
                self.time_of_death_start = pygame.time.get_ticks() # Guardar el tiempo actual
                self.current_death_frame = 0 # Reiniciar el contador de frames de muerte
                
                # ¡Capturar la posición del enemigo y el offset del fondo en el momento de la muerte!
                self.dead_x = self.x
                self.dead_y = self.y
                self.death_bg_x_offset = config.bg_x # Guarda el scroll actual del fondo

    # --- MÉTODO: update (Actualiza la lógica del villano, incluyendo la animación de muerte) ---
    def update(self):
        # Lógica para la animación de muerte
        if self.state == self.STATE_DYING:
            current_time = pygame.time.get_ticks()

            # Lógica para actualizar el frame de la animación de muerte
            # Usa config.ANIMATION_SPEED para controlar la velocidad de frames
            if current_time - self.last_frame_update > config.ANIMATION_SPEED: 
                self.current_death_frame += 1
                self.last_frame_update = current_time

            # Comprobar si la animación de muerte ha terminado
            if self.current_death_frame >= len(dead_right_villain):
                self.state = self.STATE_DEAD # Cambiar a estado muerto
                self.visible = False # Hacerlo invisible para que el nivel pueda removerlo

        # Lógica para otras animaciones si fuera necesario (ej. animación de daño)
        # Asegúrate de que solo las animaciones de vida se actualicen si el estado es ALIVE
        # self.walk_count solo se incrementa si el villano está vivo
        if self.state == self.STATE_ALIVE:
             self.walk_count += 1 # O el contador de la animación que esté activa

    def move_towards_player(self, player):
        # El villano solo se mueve si está vivo y el inventario no está abierto
        if self.state == self.STATE_ALIVE and player.health > 0 and config.show_inventory == False:
            if player.x > self.x:
                self.moving_right = True
                self.moving_left = False
                self.is_attack = False
                self.x += min(self.speed, player.x - self.x)
            elif player.x < self.x:
                self.moving_right = False
                self.moving_left = True
                self.is_attack = False
                self.x -= min(self.speed, self.x - player.x)
            else:
                self.is_attack = True
        else:
            # Si no está vivo o hay inventario abierto, detiene su movimiento y ataque
            self.moving_left = False
            self.moving_right = False
            self.is_attack = False
            self.is_stand = True # Se queda quieto

    def draw(self, wn, player):
        if not self.visible:
            return

        # Calcular la posición de dibujado relativa al scroll del fondo para el villano vivo
        draw_x_alive = self.x + config.x_relativa 

        # Hitbox (se dibuja en la posición lógica del enemigo en el mundo para colisiones)
        self.hitbox_enemy = Rect(self.x, self.y, config.width_enemy, config.height_enemy)
        #draw.rect(wn, (255, 0, 0), self.hitbox_enemy, 2) # Descomenta para ver la hitbox

        if self.state == self.STATE_DEAD:
            # Si está muerto y no visible, no dibujamos nada
            return

        elif self.state == self.STATE_DYING:
            # Calcular la posición de dibujado compensando el scroll del fondo
            display_x_death = self.dead_x + (config.bg_x - self.death_bg_x_offset)
            
            # Asegurarse de que el frame actual sea válido
            if self.current_death_frame < len(dead_right_villain):
                wn.blit(dead_right_villain[self.current_death_frame], (display_x_death, self.dead_y))
            else:
                # Si por alguna razón el frame_index es mayor, dibujar el último frame
                wn.blit(dead_right_villain[-1], (display_x_death, self.dead_y))
            
        elif self.is_attack:
            wn.blit(attack_right_villain[self.attack_count // config.ANIMATION_SPEED % len(attack_right_villain)], (draw_x_alive, self.y))
            # El attack_count se incrementaría aquí si fuera la única forma de avanzar la animación
            # Pero es mejor que los contadores de animación se manejen en update o de forma independiente.
            # Si attack_count ya se incrementa en update, quita esta línea:
            # self.attack_count += 1 

            if self.attack_count >= len(attack_right_villain) * config.ANIMATION_SPEED: # Ajusta el divisor si es diferente
                self.attack_count = 0
                # self.check_collision_hero(player) # La colisión se chequea cuando el ataque golpea, no al finalizar la animación
                                                   # Esto debería estar en un chequeo de colisión de ataque, no aquí.

        elif self.moving_right:
            wn.blit(run_right_villain[self.walk_count // config.ANIMATION_SPEED % len(run_right_villain)], (draw_x_alive, self.y))

        elif self.moving_left:
            wn.blit(run_left_villain[self.walk_count // config.ANIMATION_SPEED % len(run_left_villain)], (draw_x_alive, self.y))

        else: # Quieto
            wn.blit(self.standing[self.walk_count // config.ANIMATION_SPEED % len(self.standing)], (draw_x_alive, self.y))
            
    def draw_health_bar(self, wn):
        # La barra de vida solo se dibuja si el villano está vivo
        if self.state == self.STATE_ALIVE:
            health_ratio = max(self.health / config.health_enemy, 0) # Usa config.health_enemy como max health
            health_width = int(health_ratio * config.width_health_enemy)
            
            # Dibujar la barra de vida también relativa al scroll del fondo
            bar_x = self.x + config.x_relativa + 15 # Ajusta este offset si es necesario
            health_bar = Rect(bar_x, self.y - 5, health_width, config.height_health_enemy)
            draw.rect(wn, (255, 0, 255), health_bar) # Color de la barra de vida

            # Dibuja el texto de vida también relativo al scroll del fondo
            health_text = config.fuente.render(f"Vida: {self.health}", True, config.text_color)
            text_x = self.x + config.x_relativa - 8 # Ajusta este offset si es necesario
            wn.blit(health_text, (text_x, self.y - 25))

    def check_collision_hero(self, player):
        # Este método asumo que se llama cuando el ataque del villano golpea al jugador
        # La lógica para aplicar daño debe ocurrir aquí.
        # Por ejemplo, si el villano está en estado de ataque y su hitbox colisiona con la del jugador
        if self.state == self.STATE_ALIVE and self.is_attack and self.hitbox_enemy.colliderect(player.hitbox_player):
            player.health -= self.num_hurt
            player.is_hurt = True # Asumiendo que el Player tiene un estado 'is_hurt'
            # Podrías añadir un cooldown para el daño del villano aquí si quieres que no dañe en cada frame de contacto