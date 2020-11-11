import os
import random

import pygame
from pygame.locals import *
import pygame_gui

from core.player import Player
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

# Declare all the rooms
room = {
    'outside':  Room("Outside the House",
                     """You stand outside a simple, two-story house. Will you open the door?"""),

    'foyer':    Room("Foyer",
                     """Softly illuminated ahead of you is a staircase, and there are rooms to either side.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'living':   Room("Living Room",
                     """You enter what appears to be the living room. Couches covered in plastic are pushed up against the walls and a fireplace sits under the stairs. Moonlight filters in through the window, enough to reveal a shadow to the north, but you can't tell what it is.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'piano':    Room("Piano Room",
                     """You continue north and the floor beneath you shifts from worn-down carpet to cracked tiles. A grand piano, covered in dust, takes up the entire space.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'dining':   Room("Dining Room",
                     """This room smells of rotting wood - an ancient table sits in the center, with six chairs around it, in various states of destruction. A glint of metal shines to the north.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'kitchen':  Room("Kitchen",
                     """This must have been the kitchen once. All the large items have been stripped, leaving gaping holes in their place, but the sink, which was what caught your light, is still here. The cabinets smell worse of rot than the dining room table did.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'stairs':   Room("Stairs",
                     """You reach the top of the stairs. Dark hallways extend to either side, and directly in front of you is a cracked-open door.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'whall':    Room("Hallway",
                     """There are sliding doors to the north and a regular door to the south. The hallway continues to the west and the east.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'ehall':    Room("Hallway",
                     """Nothing but an open door to the south and more hallway to the east.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'whall2':   Room("Hallway",
                     """You have gone as far west as you seem to be able to. There are doors to the north and the south.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'ehall2':   Room("Hallway",
                     """You have gone as far east as you seem to be able to. There is only a door to the south.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'nursery':  Room("Nursery",
                     """This room once held joy, and perhaps that makes it harder to stand in. An empty bassinet sits by the window.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'vacant':   Room("Vacant Room",
                     """There is nothing here. The walls feel and look like concrete.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'laundry':  Room("Laundry Room",
                     """There is barely enough room for the door to open - you squeeze inside to find a rusted washer and dryer. Something clatters behind them.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'linen':    Room("Linen Closet",
                     """You slide the doors open to the smell of musty, damp cloth. There is enough room for a person to fit between the doors and the shelves, but only just.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'primary':  Room("Primary Bedroom",
                     """This room carries an aura of strange grandeur; the four-poster bed looks as though it was made just this morning. On the west wall, there seems to be a closet, and to the east, there is another door. A horrid smell leaks out from behind it.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'closet':   Room("Closet",
                     """Empty hangers and a single pair of red heels sit neatly in the closet. It is smaller than you would have expected.
                    What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'secret':   Room("Hidden Room",
                     """You squeeze through the small opening and find yourself in a room, several times larger than the closet. This room is bright, and it takes your eyes a moment to adjust. When they do, you realize what you are looking at - a full skeleton, slumped against the wall. Its hand is wrapped around something, but you only just have time to notice this before there is a noise from behind you. The panel whirs and clicks back into place. The surface is smooth except for a keyhole in in the center.
                     What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'pbath':    Room("Primary Bathroom",
                     """You push the door open and the smell intensifies. If not for that, though, this is a perfectly normal bathroom, also pristine.
                     What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'bedroom':  Room("Bedroom",
                     """This room is bare, except for an empty bed frame and a nightstand.
                     What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),

    'bath':     Room("Bathroom",
                     """Here, the smell of mold. The porcelain tub is halfway full of brown water.
                     What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit)"""),
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

def gameplay(player, ghost, direction):
    ghost_room = ghost.current_room

    new_ghost_location = ghost_room.n_to
    if new_ghost_location != None:
        ghost = Player(new_ghost_location)
    else:
        new_ghost_location = ghost_room.e_to
        if new_ghost_location != None:
            ghost = Player(new_ghost_location)
        else:
            new_ghost_location = ghost_room.s_to
            if new_ghost_location != None:
                ghost = Player(new_ghost_location)
            else:
                new_ghost_location = ghost_room.w_to
                ghost = Player(new_ghost_location)

    if ghost_room.n_to == player.current_room or ghost_room.s_to == player.current_room or ghost_room.w_to == player.current_room or ghost_room.e_to == player.current_room:
        # pygame.mixer.music.load('../sound_effects/2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        return "You feel a strange chill... Be cautious. Something is near."
    elif ghost_room == player.current_room and "crumpled photo" not in player.inventory:
        # pygame.mixer.music.load('../sound_effects/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        return "You feel an intense cold, and your muscles lock into place. You hear a scream, feel a pain deep in your body as if you have been stabbed, and the world goes dark as you collapse to the floor. GAME OVER"
        # replay = input('Would you like to start over? Y or N ')
        # if replay.lower() == "y":
        #     player = Player(room['outside'])
        #     ghost = Player(room[random.choice(ghost_rooms)])
        #     # pygame.mixer.music.load('../sound_effects/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
        #     # pygame.mixer.music.play()
        #     welcome = (f'Welcome! Your current location is: {player.room_info()}')
        #     print(welcome)
        # elif replay.lower() == "n":
        #     exit()
    elif ghost_room == player.current_room and "crumpled photo" in player.inventory:
        # pygame.mixer.music.load('../sound_effects/2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        return "You feel an intense cold, and your muscles lock into place. The sound of a scream shreds through your ears, and then the room grows impossibly silent. You are still frozen in place, but feel the crumpled photo in your pocket shift. Before your eyes, it unfolds in midair, and suddenly the foggy silhouette of a man stands before you. His eyes are sad, but he is smiling just a bit. 'Thank you' - the words echo through your head. The ghost disappears. You crumple to the floor, and watch in awe as the room around you grows brighter, as though the sun has come up. The cold leaves your body, and you know, with absolute certainty, that all is well. CONGRATULATIONS. YOU FREED THE GHOST, AND WON THE GAME."
        # replay = input('Would you like to start over? Y or N ')
        # if replay.lower() == "y":
        #     player = Player(room['outside'])
        #     ghost = Player(room[random.choice(ghost_rooms)])
        #     welcome = (f'Welcome! Your current location is: {player.room_info()}')
        #     print(welcome)
        # elif replay.lower() == "n":
        #     exit()
    if player.current_room.name == "Hidden Room" and "key" not in player.inventory:
        # pygame.mixer.music.load('../sound_effects/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        return "You search and search, but there is nothing in this room to save you. The light, once bright, gradually goes dim, and after some amount of time you cannot comprehend, you sit opposite the skeleton, close your eyes, and succumb to sleep. <br><br> GAME OVER"
        # replay = input('Would you like to start over? Y or N ')
        # if replay.lower() == "y":
        #     player = Player(room['outside'], [])
        #     ghost = Player(room[random.choice(ghost_rooms)])
        #     welcome = (f'Welcome! Your current location is: {player.room_info()}')
        #     print(welcome)
        # elif replay.lower() == "n":
        #     exit()

    # direction = input('What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit) ')
    # direction = direction.lower()
    # direction = commandLineSetup()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, player, ghost
        else:
            message = 'There is nothing to the north. Please choose a different direction.'
            return message, player, ghost
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, player, ghost
        else:
            message = 'There is nothing to the south. Please choose a different direction.'
            return message, player, ghost
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, player, ghost
        else:
            message = 'There is nothing to the east. Please choose a different direction.'
            return message, player, ghost
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, player, ghost
        else:
            message = 'There is nothing to the west. Please choose a different direction.'
            return message, player, ghost

    elif direction == 'i':
        invest = player.investigate()
        object = invest[14:-1]

        if invest != "There is nothing here.":
            return invest, player, ghost
        else:
            return invest, player, ghost

    # elif direction == 'in':
    #     if player.inventory != []:
    #         print(f'You currently have {player.inventory} in your inventory.')
    #         command = input('You can "drop" an item or "use" an item. Please name the item. (Example: "use pebble") ')
    #         command = command.lower()
    #         action, thing = command.split(' ')[0], ' '.join(command.split(' ')[1:])
    #         if action == 'drop':
    #             if thing in player.inventory:
    #                 player.inventory.remove(thing)
    #                 player.current_room.add_item(thing)
    #                 print(f'You currently have {player.inventory} in your inventory.')
    #             else:
    #                 print('There seems to have been an error. Please try again.')
    #         elif action == 'use':
    #             if thing == "hanger":
    #                 if player.current_room.name == "Closet":
    #                     print('Unsure what is prompting you to do so, you run your hanger along the back wall of the closet. You have almost finished this odd scrape when it gets stuck - lodged into something. You wedge, twist, and tug, then with a sudden whoosh of machinery, a panel opens up in the wall. A bright light leaks through the hole that is now there.')
    #                     player.inventory.remove(thing)
    #                     player.current_room.add_item(thing)
    #                     player.current_room = room['secret']
    #                     print(player.room_info())
    #                 else:
    #                     print(f'The {thing} does not do anything here.')
    #             elif thing == "key":
    #                 if player.current_room.name == "Hidden Room":
    #                     print('Through the fog of panic, you remember the key in your pocket. You pull it out, hands trembling, and shove it into a hole on the center of the panel. The door slides open again, and you scramble out, your chest tight.')
    #                     player.inventory.remove(thing)
    #                     player.current_room.add_item(thing)
    #                     player.current_room = room['closet']
    #                     print(player.room_info())
    #                 else:
    #                     print(f'The {thing} does not do anything here.')
    #             else:
    #                 print(f'The {thing} does not do anything here.')
    #         else:
    #             print('There seems to have been an error. Please try again.')
    #     else:
    #         print('You have nothing in your inventory.')

    elif direction == 'h':
        hint = "HINT: Find the key, the hidden room, the photograph, and the ghost - in that order. Do not get caught by the ghost until you have found all three things."
        return hint, player, ghost

    elif direction == 'q':
        return 'Farewell!'
        running = False

    else:
        error = 'There seems to have been an error. Please try again.'
        return error, player, ghost

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
                adventure_output, player, ghost = gameplay(player, ghost, direction)
                ui_scene_text.kill()
                ui_scene_text = pygame_gui.elements.UITextBox(adventure_output,
                                                              pygame.Rect((10, 10), (620, 300)),
                                                              manager=ui_manager,
                                                              object_id="#scene_text")
    #             if active_scene.is_first_visit and entered_keys != 'help' and entered_keys != 'inventory':
    #                 ui_scene_text.set_active_effect("typing_appear")
                player_text_entry.set_text("")
    #
    # active_scene.update(time_delta)
    ui_manager.update(time_delta)
    # screen.blit(active_scene.background, (0, 0))  # draw the background

    # active_scene.render_back(screen)
    ui_manager.draw_ui(screen)
    # active_scene.render_front(screen)

    pygame.display.flip()  # flip all our drawn stuff onto the screen

pygame.quit()  # exited game loop so quit pygame
