from pygame import transform, image
from variables import config

# Cargar imágenes de animación del jugador
walk_right_path = [transform.scale(image.load(f'assets/img/players/hero/RunR_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
walk_left_path = [transform.scale(image.load(f'assets/img/players/hero/RunL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
stand_right = [transform.scale(image.load(f'assets/img/players/hero/_idle_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
stand_left = [transform.scale(image.load(f'assets/img/players/hero/_idleL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
jump_right_path = [transform.scale(image.load(f'assets/img/players/hero/_Jump_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 2)]
jump_left_path = [transform.scale(image.load(f'assets/img/players/hero/_JumpL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 2)]
attack_right_path = [transform.scale(image.load(f'assets/img/players/hero/_Attack_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
attack_left_path = [transform.scale(image.load(f'assets/img/players/hero/_AttackL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
dead_path = [transform.scale(image.load(f'assets/img/players/hero/_Death_{i}.png'), (65, 35)) for i in range(0, 9)]
dead_left_path = [transform.scale(image.load(f'assets/img/players/hero/_DeathL_{i}.png'), (65, 35)) for i in range(0, 9)]

# Cargar imágenes del villano
stand_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Idle_{i}.png'), (config.width_enemy, config.height_enemy)) for i in range(0, 8)]
dead_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Death_{i}.png'), (config.width_enemy, config.height_enemy)) for i in range(0, 22)]
run_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Run_{i}.png'), (config.width_enemy, config.height_enemy)) for i in range(0, 5)]
run_left_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_RunL_{i}.png'), (config.width_enemy, config.height_enemy)) for i in range(0, 5)]
attack_right_villain = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Attack_{i}.png') ,(config.width_enemy, config.height_enemy)) for i in range(0, 11)]

# Cargar imágenes de los objetos
healt_potion = transform.scale(image.load("assets/img/objetos/Kyrise's 16x16 RPG Icon Pack - V1.3/icons/32x32/potion_02g.png"), (30, 32))
coin = transform.scale(image.load("assets/img/objetos/Kyrise's 16x16 RPG Icon Pack - V1.3/icons/32x32/shard_01a.png"), (30, 32))
