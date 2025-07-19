from pygame import *
import math
from variables import config

def handle_mouse_down_event(event):
    if event.type == MOUSEBUTTONDOWN:
        current_time = time.get_ticks()
        current_pos = event.pos

        distance = math.hypot(current_pos[0] - config.last_click_pos[0], current_pos[1] - config.last_click_pos[1])

        config.double_click = False
        config.single_click_detected_this_frame = False 

        if (current_time - config.last_click_time < config.DOUBLE_CLICK_THRESHOLD_MS and 
            distance < config.DOUBLE_CLICK_DISTANCE_THRESHOLD and event.button == 1):

            config.double_click = True
            config.last_click_time = 0
            config.waiting_for_single_click_confirm = False
            
        else:
            config.last_click_time = current_time
            config.last_click_pos = current_pos
            config.potential_single_click_pos = current_pos

            config.waiting_for_single_click_confirm = True


def update_click_state():
    config.single_click_detected_this_frame = False 

    if config.waiting_for_single_click_confirm:
        if time.get_ticks() - config.last_click_time >= config.DOUBLE_CLICK_THRESHOLD_MS:
            config.single_click_detected_this_frame = True
            config.waiting_for_single_click_confirm = False