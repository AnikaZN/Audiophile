import os
import random

import pygame
from pygame.locals import *
import pygame_gui

from core.room import Room

# from core.functions import show_inventory, try_scene_change, examine_object
# from core.functions import take_object, activate_object, combine_objects
# from core.core_strings import get_instructions
# from core.setup import setup_starting_inventory
# from core.snow import Snow
# import scenes.scene_one as s1
# import scenes.scene_two as s2
# import scenes.scene_three as s3
# import scenes.scene_four as s4

class Player():
    def __init__(self, current_room, inventory = []):
        # self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def room_info(self):
        name = self.current_room.name
        description = self.current_room.description
        return f'{name} - {description}'

    def investigate(self):
        item = self.current_room.items
        if items != None:
            return f'--- You see a {item}.'
        else:
            return "--- There is nothing here."

# Declare all the rooms
room = {
    'outside':  Room("Outside the House",
                     """You stand outside a simple, two-story house. Will you open the door?"""),

    'foyer':    Room("Foyer",
                     """Softly illuminated ahead of you is a staircase, and there are rooms to either side."""),

    'living':   Room("Living Room",
                     """You enter what appears to be the living room. Couches covered in plastic are pushed up against the walls and a fireplace sits under the stairs. Moonlight filters in through the window, enough to reveal a shadow to the north, but you can't tell what it is."""),

    'piano':    Room("Piano Room",
                     """You continue north and the floor beneath you shifts from worn-down carpet to cracked tiles. A grand piano, covered in dust, takes up the entire space."""),

    'dining':   Room("Dining Room",
                     """This room smells of rotting wood - an ancient table sits in the center, with six chairs around it, in various states of destruction. A glint of metal shines to the north."""),

    'kitchen':  Room("Kitchen",
                     """This must have been the kitchen once. All the large items have been stripped, leaving gaping holes in their place, but the sink, which was what caught your light, is still here. The cabinets smell worse of rot than the dining room table did."""),

    'stairs':   Room("Stairs",
                     """You reach the top of the stairs. Dark hallways extend to either side, and directly in front of you is a cracked-open door."""),

    'whall':    Room("Hallway",
                     """There are sliding doors to the north and a regular door to the south. The hallway continues to the west and the east."""),

    'ehall':    Room("Hallway",
                     """Nothing but an open door to the south and more hallway to the east."""),

    'whall2':   Room("Hallway",
                     """You have gone as far west as you seem to be able to. There are doors to the north and the south."""),

    'ehall2':   Room("Hallway",
                     """You have gone as far east as you seem to be able to. There is only a door to the south."""),

    'nursery':  Room("Nursery",
                     """This room once held joy, and perhaps that makes it harder to stand in. An empty bassinet sits by the window."""),

    'vacant':   Room("Vacant Room",
                     """There is nothing here. The walls feel and look like concrete."""),

    'laundry':  Room("Laundry Room",
                     """There is barely enough room for the door to open - you squeeze inside to find a rusted washer and dryer. Something clatters behind them."""),

    'linen':    Room("Linen Closet",
                     """You slide the doors open to the smell of musty, damp cloth. There is enough room for a person to fit between the doors and the shelves, but only just."""),

    'primary':  Room("Primary Bedroom",
                     """This room carries an aura of strange grandeur; the four-poster bed looks as though it was made just this morning. On the west wall, there seems to be a closet, and to the east, there is another door. A horrid smell leaks out from behind it."""),

    'closet':   Room("Closet",
                     """Empty hangers and a single pair of red heels sit neatly in the closet. It is smaller than you would have expected."""),

    'secret':   Room("Hidden Room",
                     """You squeeze through the small opening and find yourself in a room, several times larger than the closet. This room is bright, and it takes your eyes a moment to adjust. When they do, you realize what you are looking at - a full skeleton, slumped against the wall. Its hand is wrapped around something, but you only just have time to notice this before there is a noise from behind you. The panel whirs and clicks back into place. The surface is smooth except for a keyhole in the center."""),

    'pbath':    Room("Primary Bathroom",
                     """You push the door open and the smell intensifies. If not for that, though, this is a perfectly normal bathroom, also pristine."""),

    'bedroom':  Room("Bedroom",
                     """This room is bare, except for an empty bed frame and a nightstand."""),

    'bath':     Room("Bathroom",
                     """Here, the smell of mold. The porcelain tub is halfway full of brown water."""),
}

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
# pygame.mixer.music.load('../data/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
# pygame.mixer.music.play()

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

# Skipped two functione here: process_command and parse

adventure_output = ("<font face='agency' size=5>A Ghost-Hunting Adventure</font>"
                    "<br><br>"
                    "Type 'help' for instructions"
                    "<br><br>"
                    "Press Enter to begin")
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
                entered_keys = event.text
                # THESE TWO LINES MUST BE ADDRESSED
                #####################################
                parsed_command = parse(entered_keys)
                adventure_output = process_command(parsed_command[0], parsed_command[1], parsed_command[2])
                #####################################
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
    #             if active_scene.is_first_visit and entered_keys != 'help' and entered_keys != 'inventory':
    #                 ui_scene_text.set_active_effect("typing_appear")
    #             player_text_entry.set_text("")
    #
    # active_scene.update(time_delta)
    ui_manager.update(time_delta)
    # screen.blit(active_scene.background, (0, 0))  # draw the background

    # active_scene.render_back(screen)
    ui_manager.draw_ui(screen)
    # active_scene.render_front(screen)

    pygame.display.flip()  # flip all our drawn stuff onto the screen

pygame.quit()  # exited game loop so quit pygame
