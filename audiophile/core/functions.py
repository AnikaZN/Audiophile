import pygame
import random

from core.player import Player
from core.room import room, ghost_rooms


'''
TO DO
- Clear inventory on restart
- Implement a map (backup: breadcrumbs "this is what you've typed")
'''

# See if there is a ghost collision
def ghost_checks(player, ghost, direction):
    # Where is the ghost?
    ghost_room = ghost.current_room

    # Ghost goes north if they can
    new_ghost_location = ghost_room.n_to
    if new_ghost_location != None:
        ghost = Player(new_ghost_location)
    else:
        # Ghost goes east if they can't go north
        new_ghost_location = ghost_room.e_to
        if new_ghost_location != None:
            ghost = Player(new_ghost_location)
        else:
            # Ghost goes south if the can't go east
            new_ghost_location = ghost_room.s_to
            if new_ghost_location != None:
                ghost = Player(new_ghost_location)
            else:
                # Ghost goes west if they can't go south
                new_ghost_location = ghost_room.w_to
                ghost = Player(new_ghost_location)

    # If the ghost is one room away
    if ghost_room.n_to == player.current_room or ghost_room.s_to == player.current_room or ghost_room.w_to == player.current_room or ghost_room.e_to == player.current_room:
        pygame.mixer.music.load('./data/2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3')
        pygame.mixer.music.play(loops=-1)
        message = "You feel a strange chill... Be cautious. Something is near."
        return message
    # If there is a ghost collision and player does not have photo
    elif ghost_room == player.current_room and "crumpled photo" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play(loops=-1)
        message = "You feel an intense cold, and your muscles lock into place. You hear a scream, feel a pain deep in your body as if you have been stabbed, and the world goes dark as you collapse to the floor. GAME OVER -- Would you like to try again? Please type 'yes' or 'no'"
        return message
    # If player has photo and re-enters bedroom
    elif player.current_room.name == "Primary Bedroom" and "crumpled photo" in player.inventory:
        pygame.mixer.music.load('./data/2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3')
        pygame.mixer.music.play(loops=-1)
        message = "You feel an intense cold, and your muscles lock into place. The sound of a scream shreds through your ears, and then the room grows impossibly silent. You are still frozen in place, but feel the crumpled photo in your pocket shift. Before your eyes, it unfolds in midair, and suddenly the foggy silhouette of a man stands before you. His eyes are sad, but he is smiling just a bit. 'Thank you' - the words echo through your head. The ghost disappears. You crumple to the floor, and watch in awe as the room around you grows brighter, as though the sun has come up. The cold leaves your body, and you know, with absolute certainty, that all is well. CONGRATULATIONS. YOU FREED THE GHOST, AND WON THE GAME"
        return message

    # Secret room hint in closet
    if player.current_room.name == "Closet" and direction == "w":
        message = "The closet wall seems to be hollow in areas... Perhaps a tool would help."
        return message
    # Player death if they enter secret room without key
    if player.current_room.name == "Hidden Room" and "key" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play(loops=-1)
        message = "You search and search, but there is nothing in this room to save you. The light, once bright, gradually goes dim, and after some amount of time you cannot comprehend, you sit opposite the skeleton, close your eyes, and succumb to sleep. GAME OVER -- Would you like to try again? Please type 'yes' or 'no'"
        return message

    # No ghost interaction
    return "Nothing to report"

# Actual movement
def travel(player, ghost, direction):
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

# Check for items in current room
def investigate(player):
    invest = player.investigate()
    object = invest[10:-1]

    if invest == "There is nothing here.":
        return invest
    else:
        return take_item(player, object)

# Collect items in current room
def take_item(player, object):
    player.inventory.append(object)
    message = f'You now have {player.inventory} in your inventory.'
    player.current_room.item_taken(object)
    return message

# Use an item
def use(player, action, thing):
    if thing in player.inventory:
        # Use hanger
        if thing == "hanger":
            # Hanger can only be used in closet
            if player.current_room.name == "Closet":
                player.inventory.remove(thing)
                player.current_room.add_item(thing)
                player.current_room = room['secret']
                return 'Unsure what is prompting you to do so, you run your hanger along the back wall of the closet. You have almost finished this odd scrape when it gets stuck - lodged into something. You wedge, twist, and tug, then with a sudden whoosh of machinery, a panel opens up in the wall. A bright light leaks through the hole that is now there.'
            else:
                return f'The {thing} does not do anything here.'
        # Use key
        elif thing == "key":
            # Key can only be used in hidden room
            if player.current_room.name == "Hidden Room":
                player.inventory.remove(thing)
                player.current_room.add_item(thing)
                player.current_room = room['closet']
                return 'Through the fog of panic, you remember the key in your pocket. You pull it out, hands trembling, and shove it into a hole on the center of the panel. The door slides open again, and you scramble out, your chest tight.'
            else:
                return f'The {thing} does not do anything here.'
        # Item has no use
        else:
            return f'The {thing} does not do anything here.'
    # Item not in inventory
    else:
        return 'There seems to have been an error. Please try again.'

# Discard item - must be in inventory
def drop(player, action, thing):
    if thing in player.inventory:
        player.inventory.remove(thing)
        player.current_room.add_item(thing)
        return f'You currently have {player.inventory} in your inventory.'
    else:
        return 'There seems to have been an error. Please try again.'

# Start over outside the house
def restart(player):
    player.current_room = room['outside']
    ghost = Player(room[random.choice(ghost_rooms)])
    pygame.mixer.music.load('./data/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
    pygame.mixer.music.play(loops=-1)
    message = "You stand outside a simple, two-story house. Will you open the door?"
    return message, player, ghost
