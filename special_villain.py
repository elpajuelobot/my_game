from personajes import Villain, Projectile
from time import sleep
from random import randint
from pygame import *
from variables import config

class VillainLevel3(Villain):
    def __init__(self, health, max_health, speed, animation_paths, can_shoot=False, movement_mode=..., levitate_height=50, fly_speed_y=2):
        super().__init__(health, max_health, speed, animation_paths, can_shoot, movement_mode, levitate_height, fly_speed_y)
        self.state = "idle"
        self.dodge_drtn = 300
        self.dodge_start_time = 0
        self.can_dodge = True
        self.dodge_cooldown = 2000
        self.last_dodge_time = 0
        self.dodge_direction = 1

        self.double_attck_ready = True
        self.last_attck_time = 0
        self.attack_cooldown = 2000

    def move_towards_player(self, player):
        current_time = time.get_ticks()

        if self.state == "dodging":
            self.x += 10 * self.dodge_direction
            if current_time - self.dodge_start_time > self.dodge_drtn:
                self.state = "idle"

        if not self.can_dodge and current_time - self.last_dodge_time > self.dodge_cooldown:
            self.can_dodge = True

        if (
            player.state.name == "ATTACKING"
            and self.can_dodge
            and abs(player.x - self.x) < 150
            and randint(1, 100) <= 30
        ):
            self.state = "dodging"
            self.dodge_start_time = current_time
            self.last_dodge_time = current_time
            self.can_dodge = False
            self.dodge_direction = 1 if randint(0, 1) == 0 else -1
            return

        super().move_towards_player(player)

    def draw(self, wn, player, enemy):
        if not self.visible:
            return

        self.hitbox_enemy = Rect(self.x, self.y, config.width_enemy, config.height_enemy)

        def aplicar_sombra(sprite):
            copia = sprite.copy()
            filtro = Surface(copia.get_size(), SRCALPHA)
            filtro.fill((0, 0, 0, 150))  # filtro oscuro
            copia.blit(filtro, (0, 0), special_flags=BLEND_RGBA_MULT)
            return copia

        if self.is_dead:
            current_animation = self.animations.get('dead') if self.direction == 1 else self.animations.get('dead_left')
            sprite = aplicar_sombra(current_animation[self.dead_count // config.ANIMATION_SPEED % len(current_animation)])
            wn.blit(sprite, (self.x, self.y))
            self.dead_count += 1
            if self.dead_count >= len(current_animation) * config.ANIMATION_SPEED:
                self.visible = False
            return

        elif self.is_shooting:
            current_animation = self.animations.get('shoot_right') if self.direction == 1 else self.animations.get('shoot_left')
            if current_animation:
                sprite = aplicar_sombra(current_animation[self.attack_count // config.ANIMATION_SPEED % len(current_animation)])
                wn.blit(sprite, (self.x, self.y))
                self.attack_count += 1
                if self.attack_count // config.ANIMATION_SPEED == (len(current_animation) - 1) and self.can_create_prj:
                    self.projectiles.append(Projectile(
                        self.x + config.width_enemy // 2,
                        self.y + config.height_enemy // 2,
                        player.x + config.widht_player // 2,
                        player.y + config.height_player // 2,
                        self.prj_speed,
                        self.prj_damage,
                        self.animations.get('prj_right') if self.direction == 1 else self.animations.get('prj_left')
                    ))
                    self.can_create_prj = False
                if self.attack_count >= len(current_animation) * config.ANIMATION_SPEED:
                    self.is_shooting = False
                    self.attack_count = 0
            else:
                self.is_shooting = False
                self.attack_count = 0

        elif self.is_attack:
            current_animation = self.animations['attack_right'] if self.moving_right or not self.moving_left else self.animations['attack_left']
            sprite = aplicar_sombra(current_animation[self.attack_count // config.ANIMATION_SPEED % len(current_animation)])
            wn.blit(sprite, (self.x, self.y))
            self.attack_count += 1
            if self.attack_count >= len(current_animation) * 6:
                self.attack_count = 0
                self.check_collision_hero(player)

        elif self.moving_right or self.moving_left:
            if self.mv_mode == self.MOVE_GROUND:
                current_animation = self.animations['run_right'] if self.direction == 1 else self.animations['run_left']
            else:
                current_animation = self.animations.get('fly_right', self.animations['idle_right']) if self.direction == 1 else self.animations.get('fly_left', self.animations['idle_left'])
            sprite = aplicar_sombra(current_animation[self.walk_count // config.ANIMATION_SPEED % len(current_animation)])
            wn.blit(sprite, (self.x, self.y))

        else:
            if self.mv_mode == self.MOVE_GROUND:
                current_animation = self.standing
            else:
                current_animation = self.animations.get('idle_right', self.standing) if self.direction == 1 else self.animations.get('idle_left', self.standing)
            sprite = aplicar_sombra(current_animation[self.walk_count // config.ANIMATION_SPEED % len(current_animation)])
            wn.blit(sprite, (self.x, self.y))

        self.walk_count += 1

        for projectile in list(self.projectiles):
            projectile.update(player, enemy)
            projectile.draw(wn)
            projectile.can_damage_player(player)
            if not projectile.visible:
                self.projectiles.remove(projectile)

    def check_collision_hero(self, player):
        current_time = time.get_ticks()

        if self.hitbox_enemy.colliderect(player.hitbox_player):
            if self.double_attck_ready:
                player.health -= self.num_hurt
                sleep(0.1)
                player.health -= self.num_hurt
                self.double_attck_ready = False
                self.last_attck_time = current_time

        if not self.double_attck_ready and current_time - self.last_attck_time > self.attack_cooldown:
            self.double_attck_ready = True
