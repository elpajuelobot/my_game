from pygame import transform, image
from variables import config

# Cargar imágenes de animación del jugador
walk_right_path = [transform.scale(image.load(f'assets/img/players/hero/RunR_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
walk_left_path = [transform.scale(image.load(f'assets/img/players/hero/RunL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
stand_right = [transform.scale(image.load(f'assets/img/players/hero/_idle_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
stand_left = [transform.scale(image.load(f'assets/img/players/hero/_idleL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
jump_right_path = [transform.scale(image.load(f'assets/img/players/hero/_Jump_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 2)]
jump_left_path = [transform.scale(image.load(f'assets/img/players/hero/_JumpL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 2)]
attack_right_combo_path = [transform.scale(image.load(f'assets/img/players/hero/_Attack_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
attack_left_combo_path = [transform.scale(image.load(f'assets/img/players/hero/_AttackL_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 9)]
attack_right_1_path = [transform.scale(image.load(f'assets/img/players/hero/_Attack1_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 3)]
attack_left_1_path = [transform.scale(image.load(f'assets/img/players/hero/_AttackL1_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 3)]
attack_right_2_path = [transform.scale(image.load(f'assets/img/players/hero/_Attack2_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 5)]
attack_left_2_path = [transform.scale(image.load(f'assets/img/players/hero/_AttackL2_{i}.png'), (config.widht_player, config.height_player)) for i in range(0, 5)]
dead_path = [transform.scale(image.load(f'assets/img/players/hero/_Death_{i}.png'), (65, 35)) for i in range(0, 9)]
dead_left_path = [transform.scale(image.load(f'assets/img/players/hero/_DeathL_{i}.png'), (65, 35)) for i in range(0, 9)]
crouchWalk_right = [transform.scale(image.load(f'assets/img/players/hero/_CrouchWalk_{i}.png'), (35, 35)) for i in range(1, 8)]
crouchWalk_left = [transform.scale(image.load(f'assets/img/players/hero/left__CrouchWalk_{i}.png'), (35, 35)) for i in range(1, 8)]
crouchWalk_r_transition = transform.scale(image.load('assets/img/players/hero/_CrouchTransition.png'), (35, 47))
crouchWalk_l_transition = transform.scale(image.load('assets/img/players/hero/_CrouchTransitionL.png'), (35, 47))
crouch_right = transform.scale(image.load('assets/img/players/hero/_Crouch.png'), (35, 35))
crouch_left = transform.scale(image.load('assets/img/players/hero/_CrouchL.png'), (35, 35))


def villain(name, width, height):

    animations = {}

    if name == "NightBorne":
        # Cargar imágenes del villano
        animations['idle_right'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Idle_{i}.png'), (width, height)) for i in range(0, 8)]
        animations['idle_left'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Idle_left_{i}.png'), (width, height)) for i in range(0, 8)]
        animations['dead'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Death_{i}.png'), (width, height)) for i in range(0, 22)]
        animations['dead_left'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/left_NightBorne_Death_{i}.png'), (width, height)) for i in range(0, 22)]
        animations['run_right'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Run_{i}.png'), (width, height)) for i in range(0, 5)]
        animations['run_left'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_RunL_{i}.png'), (width, height)) for i in range(0, 5)]
        animations['attack_right'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Attack_{i}.png') ,(width, height)) for i in range(0, 11)]
        animations['attack_left'] = [transform.scale(image.load(f'assets/img/players/villian/NightBorne/NightBorne_Attack_Left_{i}.png'), (width, height)) for i in range(0, 11)]

    elif name == 'Boss':
        animations['idle_right'] = [transform.scale(image.load(f'assets/img/players/villian/boss/Necromancer_idle_left_{i}.png'), (width, height)) for i in range(0, 7)]
        animations['idle_left'] = [transform.scale(image.load(f'assets/img/players/villian/boss/Necromancer_idle_left_{i}.png'), (width, height)) for i in range(0, 7)]
        animations['dead'] = [transform.scale(image.load(f'assets/img/players/villian/boss/Necromancer_death_{i}.png'), (width, height)) for i in range(0, 9)]
        animations['dead_left'] = [transform.scale(image.load(f'assets/img/players/villian/boss/left_Necromancer_death_{i}.png'), (width, height)) for i in range(0, 9)]
        animations['fly_right'] = [transform.scale(image.load(f'assets/img/players/villian/boss/Necromancer_run_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['fly_left'] = [transform.scale(image.load(f'assets/img/players/villian/boss/left_Necromancer_run_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['shoot_right'] = [transform.scale(image.load(f'assets/img/players/villian/boss/Necromancer_attack3_{i}.png') ,(width, height)) for i in range(1, 17)]
        animations['shoot_left'] = [transform.scale(image.load(f'assets/img/players/villian/boss/left_Necromancer_attack3_{i}.png'), (width, height)) for i in range(1, 17)]
        # Disparos
        animations['prj_right'] = [transform.scale(image.load(f'assets/img/players/villian/boss/proyectil_right_{i}.png'), (config.prj_width, config.prj_height)) for i in range(0, 2)]
        animations['prj_left'] = [transform.scale(image.load(f'assets/img/players/villian/boss/proyectil_left_{i}.png'), (config.prj_width, config.prj_height)) for i in range(0, 2)]

    elif name == 'Dead':
        animations['idle_right'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_idle_right_{i}.png'), (width, height)) for i in range(1, 7)]
        animations['idle_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_idle_{i}.png'), (width, height)) for i in range(1, 7)]
        animations['dead'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_death_{i}.png'), (width, height)) for i in range(1, 18)]
        animations['dead_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_death_{i}.png'), (width, height)) for i in range(1, 18)]
        animations['fly_right'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_run_{i}.png'), (width, height)) for i in range(0, 3)]
        animations['fly_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_run_{i}.png'), (width, height)) for i in range(0, 3)]
        animations['attack_right'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_attack{i}.png') ,(width, height)) for i in range(1, 7)]
        animations['attack_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_attack{i}.png'), (width, height)) for i in range(1, 7)]
        animations['summon'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_summon_{i}.png'), (width, height)) for i in range(1, 5)]
        animations['summon_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_summon_{i}.png'), (width, height)) for i in range(1, 5)]

    elif name == 'Dead_summon':
        animations['idle'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]
        animations['idle_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]
        animations['dead'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_summon_Death_{i}.png'), (width, height)) for i in range(1, 5)]
        animations['dead_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_summon_Death_{i}.png'), (width, height)) for i in range(1, 5)]
        animations['fly_right'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]
        animations['fly_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]
        animations['attack_right'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]
        animations['attack_left'] = [transform.scale(image.load(f'C:/Users/elpaj/Documents/my_game/assets/img/players/villian/The_Dead/left_The_Dead_summon_Idle_{i}.png'), (width, height)) for i in range(1, 4)]

    elif name == 'Wizard':
        animations['idle_right'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_idle_{i}.png'), (width, height)) for i in range(1, 6)]
        animations['idle_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_idle_{i}.png'), (width, height)) for i in range(1, 6)]
        animations['dead'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_death_{i}.png'), (width, height)) for i in range(1, 7)]
        animations['dead_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_death_{i}.png'), (width, height)) for i in range(1, 7)]
        animations['run_right'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_run_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['run_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_run_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['shoot_right'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_attack1_{i}.png') ,(width, height)) for i in range(1, 8)]
        animations['shoot_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_attack1_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['attack_right'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_attack2_{i}.png') ,(width, height)) for i in range(1, 8)]
        animations['attack_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_attack2_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['jump'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_jump_{i}.png'), (width, height)) for i in range(1, 2)]
        animations['jump_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_jump_{i}.png'), (width, height)) for i in range(1, 2)]
        animations['fall'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_fall_{i}.png'), (width, height)) for i in range(1, 2)]
        animations['fall_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_fall_{i}.png'), (width, height)) for i in range(1, 2)]
        # Disparos
        animations['prj_right'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/Wizard_prj_{i}.png'), (config.prj_width, config.prj_height)) for i in range(0, 1)]
        animations['prj_left'] = [transform.scale(image.load(f'assets/img/players/villian/Wizard/left_Wizard_prj_{i}.png'), (config.prj_width, config.prj_height)) for i in range(0, 1)]

    elif name == "Knight":
        animations['idle_right'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/KnightIdle_{i}.png'), (width, height)) for i in range(1, 15)]
        animations['idle_left'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/left_KnightIdle_{i}.png'), (width, height)) for i in range(1, 15)]
        animations['dead'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/KnightDeath_{i}.png'), (width, height)) for i in range(1, 15)]
        animations['dead_left'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/left_KnightDeath_{i}.png'), (width, height)) for i in range(1, 15)]
        animations['run_right'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/KnightRun_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['run_left'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/left_KnightRun_{i}.png'), (width, height)) for i in range(1, 8)]
        animations['attack_right'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/KnightAttack_{i}.png') ,(width, height)) for i in range(1, 22)]
        animations['attack_left'] = [transform.scale(image.load(f'assets/img/players/villian/Knight/left_KnightAttack_{i}.png'), (width, height)) for i in range(1, 22)]

    return animations

# Cargar imágenes de los objetos
healt_potion = transform.scale(image.load("assets/img/objetos/Kyrise's 16x16 RPG Icon Pack - V1.3/icons/32x32/potion_02g.png"), (30, 32))
coin = transform.scale(image.load("assets/img/objetos/Kyrise's 16x16 RPG Icon Pack - V1.3/icons/32x32/shard_01a.png"), (30, 32))

# efectos
red_portal = [transform.scale(image.load(f'C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\effects\\portal_rojo_{i}.png'), (config.width_portal, config.height_portal)) for i in range(1, 61)]

def teclado():
    teclas_image = {}

    teclas_image['tecla_e'] = transform.scale(image.load("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\objetos\\teclado_image\\cortados\\Key_e.png"), (config.widht_key_image, config.height_key_image))
    teclas_image['tecla_e_pressed'] = transform.scale(image.load("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\objetos\\teclado_image\\cortados\\Key_pressed_e.png"), (config.widht_key_image, config.height_key_image))

    teclas_image['tecla_w'] = transform.scale(image.load("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\objetos\\teclado_image\\cortados\\Key_w.png"), (config.widht_key_image, config.height_key_image))
    teclas_image['tecla_w_pressed'] = transform.scale(image.load("C:\\Users\\elpaj\\Documents\\my_game\\assets\\img\\objetos\\teclado_image\\cortados\\Key_pressed_w.png"), (config.widht_key_image, config.height_key_image))

    return teclas_image
