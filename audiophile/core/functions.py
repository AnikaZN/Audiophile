import pygame

from core.player import Player
from core.room import room


'''
TO DO
- Terminate game when you hit the ghostie
- Allow player/ghost collision
- Implement replay option
- Fix closet <--> secret room navigation
- Clean up aesthetics
'''

def ghost_checks(player, ghost, direction):
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
        pygame.mixer.music.load('./data/2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        print('A')
        message = "You feel a strange chill... Be cautious. Something is near."
        return message
    elif ghost_room == player.current_room and "crumpled photo" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        print('B')
        message = "You feel an intense cold, and your muscles lock into place. You hear a scream, feel a pain deep in your body as if you have been stabbed, and the world goes dark as you collapse to the floor. GAME OVER -- Would you like to try again? Please type 'yes' or 'no'"
        return message
    elif ghost_room == player.current_room and "crumpled photo" in player.inventory:
        pygame.mixer.music.load('./data/2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        message = "You feel an intense cold, and your muscles lock into place. The sound of a scream shreds through your ears, and then the room grows impossibly silent. You are still frozen in place, but feel the crumpled photo in your pocket shift. Before your eyes, it unfolds in midair, and suddenly the foggy silhouette of a man stands before you. His eyes are sad, but he is smiling just a bit. 'Thank you' - the words echo through your head. The ghost disappears. You crumple to the floor, and watch in awe as the room around you grows brighter, as though the sun has come up. The cold leaves your body, and you know, with absolute certainty, that all is well. CONGRATULATIONS. YOU FREED THE GHOST, AND WON THE GAME -- Would you like to try again? Please type 'yes' or 'no'"
        print('C')
        return message

    if player.current_room.name == "Closet" and "hanger" not in player.inventory and direction == "w":
        message = "The closet wall seems to be hollow in areas... Perhaps a tool would help."
        print('D')
        return message
    if player.current_room.name == "Hidden Room" and "key" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        # pygame.mixer.music.play()
        message = "You search and search, but there is nothing in this room to save you. The light, once bright, gradually goes dim, and after some amount of time you cannot comprehend, you sit opposite the skeleton, close your eyes, and succumb to sleep. GAME OVER -- Would you like to try again? Please type 'yes' or 'no'"
        print('E')
        return message

    return "Nothing to report"

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

def investigate(player):
    invest = player.investigate()
    object = invest[10:-1]

    if invest == "There is nothing here.":
        return invest
    else:
        return take_item(player, object)

def take_item(player, object):
    player.inventory.append(object)
    message = f'You now have {player.inventory} in your inventory.'
    player.current_room.item_taken(object)
    return message

def use(player, action, thing):
    if thing == "hanger":
        if player.current_room.name == "Closet":
            player.inventory.remove(thing)
            player.current_room.add_item(thing)
            player.current_room = room['secret']
            return 'Unsure what is prompting you to do so, you run your hanger along the back wall of the closet. You have almost finished this odd scrape when it gets stuck - lodged into something. You wedge, twist, and tug, then with a sudden whoosh of machinery, a panel opens up in the wall. A bright light leaks through the hole that is now there.'
        else:
            return f'The {thing} does not do anything here.'
    elif thing == "key":
        if player.current_room.name == "Hidden Room":
            player.inventory.remove(thing)
            player.current_room.add_item(thing)
            player.current_room = room['closet']
            return 'Through the fog of panic, you remember the key in your pocket. You pull it out, hands trembling, and shove it into a hole on the center of the panel. The door slides open again, and you scramble out, your chest tight.'
        else:
            return f'The {thing} does not do anything here.'
    else:
        return f'The {thing} does not do anything here.'

def drop(player, action, thing):
    if thing in player.inventory:
        player.inventory.remove(thing)
        player.current_room.add_item(thing)
        return f'You currently have {player.inventory} in your inventory.'
    else:
        return 'There seems to have been an error. Please try again.'

def restart():
    player = Player(room['outside'])
    ghost = Player(room[random.choice(ghost_rooms)])
    pygame.mixer.music.load('../sound_effects/MysteriousSuspensefulMusic2018-11-03_-_Dark_Fog_-_David_Fesliyan.mp3')
    # pygame.mixer.music.play()
    return player, ghost
