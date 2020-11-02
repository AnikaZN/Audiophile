"""
Sources:
https://www.fesliyanstudios.com/
"""

from room import Room
from player import Player
from item import Item
import random
import os
import pygame

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

# # Main
# pygame.init()
# pygame.mixer.music.load('../sound_effects/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
# pygame.mixer.music.play()
# name = input('What is your name? ')
#
# player = Player(name, room['outside'])
# ghost = Player('Ghost', room[random.choice(ghost_rooms)])
#
# print(f'Welcome, {player.name}! Your current location is: {player.room_info()}')

def clear():
    os.system( 'cls' )

def item(player, item):
    interact = input('What would you like to do? (HINT: You may "take" or "ignore" an item.) ')
    interact = interact.lower()

    if interact == 'take':
        player.inventory.append(item)
        print(f'You now have {player.inventory} in your inventory.')
        player.current_room.item_taken(item)
        return gameplay(player, ghost)
    elif interact == 'ignore':
        print('You leave it there.')
        return gameplay(player, ghost)
    else:
        print('There seems to have been an error. Please try again.')
        return gameplay(player, ghost)

# def gameplay(player, ghost, direction):
#     if direction == 'n':
#         print('Something is happening!')
#         return "It's gotta be a return statement."
#     else:
#         print("You are ending up here for some reason.")
#         return "Still a return statement, though."

def gameplay(player, ghost, direction=None):
    clear()
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
        pygame.mixer.music.load('../sound_effects/2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        return "You feel a strange chill... Be cautious. Something is near."
    elif ghost_room == player.current_room and "crumpled photo" not in player.inventory:
        pygame.mixer.music.load('../sound_effects/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        return "You feel an intense cold, and your muscles lock into place. You hear a scream, feel a pain deep in your body as if you have been stabbed, and the world goes dark as you collapse to the floor. GAME OVER"
        replay = input('Would you like to start over? Y or N ')
        if replay.lower() == "y":
            player = Player(name, room['outside'])
            ghost = Player(room[random.choice(ghost_rooms)])
            pygame.mixer.music.load('../sound_effects/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
            pygame.mixer.music.play()
            welcome = (f'Welcome! Your current location is: {player.room_info()}')
            return welcome, gameplay(player, ghost)
        elif replay.lower() == "n":
            exit()
    elif ghost_room == player.current_room and "crumpled photo" in player.inventory:
        pygame.mixer.music.load('../sound_effects/2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        return "You feel an intense cold, and your muscles lock into place. The sound of a scream shreds through your ears, and then the room grows impossibly silent. You are still frozen in place, but feel the crumpled photo in your pocket shift. Before your eyes, it unfolds in midair, and suddenly the foggy silhouette of a man stands before you. His eyes are sad, but he is smiling just a bit. 'Thank you' - the words echo through your head. The ghost disappears. You crumple to the floor, and watch in awe as the room around you grows brighter, as though the sun has come up. The cold leaves your body, and you know, with absolute certainty, that all is well. CONGRATULATIONS. YOU FREED THE GHOST, AND WON THE GAME."
        replay = input('Would you like to start over? Y or N ')
        if replay.lower() == "y":
            player = Player(room['outside'])
            ghost = Player(room[random.choice(ghost_rooms)])
            welcome = (f'Welcome! Your current location is: {player.room_info()}')
            return welcome, gameplay(player, ghost)
        elif replay.lower() == "n":
            exit()
    if player.current_room.name == "Hidden Room" and "key" not in player.inventory:
        pygame.mixer.music.load('../sound_effects/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        return 'You search and search, but there is nothing in this room to save you. The light, once bright, gradually goes dim, and after some amount of time you cannot comprehend, you sit opposite the skeleton, close your eyes, and succumb to sleep. GAME OVER'
        replay = input('Would you like to start over? Y or N ')
        if replay.lower() == "y":
            player = Player(room['outside'], [])
            ghost = Player(room[random.choice(ghost_rooms)])
            welcome = (f'Welcome! Your current location is: {player.room_info()}')
            return welcome, gameplay(player, ghost)
        elif replay.lower() == "n":
            exit()

    # direction = input('What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, H for a hint, Q to quit) ')
    # direction = direction.lower()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, gameplay(player, ghost)
        else:
            message = 'There is nothing to the north. Please choose a different direction.'
            return message, gameplay(player, ghost)
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, gameplay(player, ghost)
        else:
            message = 'There is nothing to the south. Please choose a different direction.'
            return message, gameplay(player, ghost)
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, gameplay(player, ghost)
        else:
            message = 'There is nothing to the east. Please choose a different direction.'
            return message, gameplay(player, ghost)
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(location)
            info = player.room_info()
            return info, gameplay(player, ghost)
        else:
            message = 'There is nothing to the west. Please choose a different direction.'
            return message, gameplay(player, ghost)

    elif direction == 'i':
        invest = player.investigate()
        object = invest[14:-1]

        if invest != "There is nothing here.":
            item(player, object)
            return invest
        else:
            return invest, gameplay(player, ghost)

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
    #                 return gameplay(player, ghost)
    #             else:
    #                 print('There seems to have been an error. Please try again.')
    #                 return gameplay(player, ghost)
    #         elif action == 'use':
    #             if thing == "hanger":
    #                 if player.current_room.name == "Closet":
    #                     print('Unsure what is prompting you to do so, you run your hanger along the back wall of the closet. You have almost finished this odd scrape when it gets stuck - lodged into something. You wedge, twist, and tug, then with a sudden whoosh of machinery, a panel opens up in the wall. A bright light leaks through the hole that is now there.')
    #                     player.inventory.remove(thing)
    #                     player.current_room.add_item(thing)
    #                     player.current_room = room['secret']
    #                     print(player.room_info())
    #                     return gameplay(player, ghost)
    #                 else:
    #                     print(f'The {thing} does not do anything here.')
    #                     return gameplay(player, ghost)
    #             elif thing == "key":
    #                 if player.current_room.name == "Hidden Room":
    #                     print('Through the fog of panic, you remember the key in your pocket. You pull it out, hands trembling, and shove it into a hole on the center of the panel. The door slides open again, and you scramble out, your chest tight.')
    #                     player.inventory.remove(thing)
    #                     player.current_room.add_item(thing)
    #                     player.current_room = room['closet']
    #                     print(player.room_info())
    #                     return gameplay(player, ghost)
    #                 else:
    #                     print(f'The {thing} does not do anything here.')
    #                     return gameplay(player, ghost)
    #             else:
    #                 print(f'The {thing} does not do anything here.')
    #                 return gameplay(player, ghost)
    #         else:
    #             print('There seems to have been an error. Please try again.')
    #             return gameplay(player, ghost)
    #     else:
    #         print('You have nothing in your inventory.')
    #         return gameplay(player, ghost)

    elif direction == 'h':
        hint = "HINT: Find the key, the hidden room, the photograph, and the ghost - in that order. Do not get caught by the ghost until you have found all three things."
        return hint, gameplay(player, ghost)

    elif direction == 'q':
        return 'Farewell!'

    else:
        error = 'There seems to have been an error. Please try again.'
        return error, gameplay(player, ghost)

if __name__ == '__main__':
    gameplay(player, ghost)
