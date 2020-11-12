import os
import random

import pygame
from pygame.locals import *
import pygame_gui

from core.player import Player
from core.room import Room, room
from core.functions import travel, use, drop, investigate

# from core.functions import show_inventory, try_scene_change, examine_object
# from core.functions import take_object, activate_object, combine_objects
# from core.core_strings import get_instructions
# from core.setup import setup_starting_inventory
# from core.snow import Snow
# import scenes.scene_one as s1
# import scenes.scene_two as s2
# import scenes.scene_three as s3
# import scenes.scene_four as s4

# Put items in rooms
room['outside'].add_item('pebble')
room['living'].add_item('dog collar')
room['piano'].add_item('knife')
room['dining'].add_item('broken chair leg')
room['kitchen'].add_item('moldy bread')
room['nursery'].add_item('teddy bear')
room['vacant'].add_item('chunk of concrete')
room['laundry'].add_item('key')
room['bedroom'].add_item('journal')
room['bath'].add_item('crystal goblet')
room['pbath'].add_item('dead bird')
room['primary'].add_item('brooch')
room['closet'].add_item('hanger')
room['secret'].add_item('crumpled photo')
room['linen'].add_item('damp towel')

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['stairs']
room['foyer'].e_to = room['dining']
room['foyer'].w_to = room['living']
room['living'].n_to = room['piano']
room['living'].e_to = room['foyer']
room['piano'].s_to = room['living']
room['dining'].n_to = room['kitchen']
room['dining'].w_to = room['foyer']
room['kitchen'].s_to = room['dining']
room['stairs'].w_to = room['whall']
room['stairs'].e_to = room['ehall']
room['stairs'].n_to = room['primary']
room['stairs'].s_to = room['foyer']
room['whall'].s_to = room['nursery']
room['whall'].w_to = room['whall2']
room['whall'].n_to = room['linen']
room['whall'].e_to = room['stairs']
room['nursery'].n_to = room['whall']
room['whall2'].s_to = room['vacant']
room['whall2'].n_to = room['laundry']
room['whall2'].e_to = room['whall']
room['vacant'].n_to = room['whall2']
room['laundry'].s_to = room['whall2']
room['linen'].s_to = room['whall']
room['primary'].w_to = room['closet']
room['primary'].e_to = room['pbath']
room['primary'].s_to = room['stairs']
room['closet'].e_to = room['primary']
room['closet'].w_to = room['secret']
room['secret'].e_to = room['closet']
room['pbath'].w_to = room['primary']
room['ehall'].e_to = room['ehall2']
room['ehall'].s_to = room['bedroom']
room['ehall'].w_to = room['stairs']
room['ehall2'].s_to = room['bath']
room['ehall2'].w_to = room['ehall']
room['bath'].n_to = room['ehall2']
room['bedroom'].n_to = room['ehall']

ghost_rooms = ['living', 'piano', 'dining', 'kitchen', 'nursery', 'laundry',
               'bedroom', 'bath', 'pbath', 'primary', 'closet', 'vacant',
               'linen']

pygame.init()
pygame.mixer.music.load('./data/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
pygame.mixer.music.play()

# What does this do?
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('Audiophile')
# Make sure b/g images match this
screen = pygame.display.set_mode((640, 480))

# Adjust to something more appropriate
background_colour = pygame.Color("#F0F0F0")

ui_manager = pygame_gui.UIManager((640, 480), "data/ui_theme.json")
ui_manager.add_font_paths('agency', "data/AGENCYB.TTF")
ui_manager.preload_fonts([{'name': 'agency', 'point_size': 18, 'style': 'regular'},
                          {'name': 'gabriola', 'point_size': 18, 'style': 'bold'},
                          {'name': 'gabriola', 'point_size': 18, 'style': 'italic'}])

# Will we need this?
have_started = False

# Not sure how these work yet
# scenes = []
# scene_1 = s1.SceneOne()
# scenes.append(scene_1)
# scenes.append(s2.SceneTwo())
# scenes.append(s3.SceneThree())
# scenes.append(s4.SceneFour())
# active_scene = scene_1

# Instantiate player and ghost
player = Player(room['outside'])
ghost = Player(room[random.choice(ghost_rooms)])

def process_command(command):
    global have_started
    global player
    global ghost

    command = command.lower()

    if command == "":
        output = player.room_info()
    elif command == "n" or command == "s" or command == "e" or command == "w":
        message, player, ghost = travel(player, ghost, command)
        output = message
    elif command == "h":
        hint = "HINT: Find the key, the hidden room, the photograph, and the ghost - in that order. Do not get caught by the ghost until you have found all three things."
        output = hint
    elif command == "i":
        output = investigate(player)
    elif command == "in":
        if player.inventory != []:
            output = f'You currently have {player.inventory} in your inventory.'
        else:
            output = 'You have nothing in your inventory.'
    elif "use" in command:
        action, thing = command.split(' ')[0], ' '.join(command.split(' ')[1:])
        output = use(player, action, thing)
    elif "drop" in command:
        action, thing = command.split(' ')[0], ' '.join(command.split(' ')[1:])
        output = drop(player, action, thing)
    elif command == "q":
        running = False
        return "Farewell!"
    else:
        output = "There seems to have been an error. Please try again."

    return output

adventure_output = ("<font face='agency' size=5>Audiophile: A Ghost-Hunting Adventure</font>"
                    "<br><br>"
                    """You stand outside a simple, two-story house."""
                    "<br><br>"
                     """Will you open the door?"""
                    "<br><br>"
                    "Press N to begin")
entered_keys = ""

ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                              pygame.Rect((10, 10), (620, 300)),
                                              manager=ui_manager,
                                              object_id="#scene_text")
ui_scene_text.set_active_effect("typing_appear")
player_text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((20, 320), (600, 19)),
                                                        manager=ui_manager,
                                                        object_id="#player_input")
pygame_gui.elements.UILabel(pygame.Rect((10, 320), (10, 19)),
                            ">",
                            manager=ui_manager,
                            object_id="#carat")

running = True
clock = pygame.time.Clock()

while running:
    frameTime = clock.tick(60)
    time_delta = frameTime / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        ui_manager.process_events(event)

        if event.type == USEREVENT:
            if event.user_type == "ui_text_entry_finished":
                direction = event.text
                ####################
                adventure_output = process_command(direction)
                ####################
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
    #             if active_scene.is_first_visit and entered_keys != 'help' and entered_keys != 'inventory':
    #                 ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")

    # active_scene.update(time_delta)
    ui_manager.update(time_delta)
    # screen.blit(active_scene.background, (0, 0))  # draw the background

    # active_scene.render_back(screen)
    ui_manager.draw_ui(screen)
    # active_scene.render_front(screen)

    pygame.display.flip()  # flip all our drawn stuff onto the screen

pygame.quit()  # exited game loop so quit pygame
