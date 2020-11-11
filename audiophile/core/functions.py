import pygame

from core.player import Player


'''
TO DO
- Figure out "investigate room" and take items
- Figure out inventory interaction
- Display warning message along with new room information
- "Enter" key to close additional messages? (Hint/ghostie warning)
- Terminate game when you hit the ghostie
- Implement replay option
- Clean up aesthetics
'''
# def item(player, ghost, item):
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False
#
#         ui_manager.process_events(event)
#
#         if event.type == USEREVENT:
#             if event.user_type == "ui_text_entry_finished":
#                 direction = event.text
#
#                 if direction == 'take':
#                     player.inventory.append(item)
#                     message = f'You now have {player.inventory} in your inventory.'
#                     player.current_room.item_taken(item)
#                     return message, player, ghost
#                 elif direction == 'ignore':
#                     message = 'You leave it there.'
#                     return message, player, ghost
#                 else:
#                     message = 'There seems to have been an error. Please try again.'
#                     return message, player, ghost

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
        pygame.mixer.music.load('./data/2020-06-25_-_Dark_Shadows_-_www.FesliyanStudios.com_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        message = "You feel a strange chill... Be cautious. Something is near."
        return message, player, ghost
    elif ghost_room == player.current_room and "crumpled photo" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        message = "You feel an intense cold, and your muscles lock into place. You hear a scream, feel a pain deep in your body as if you have been stabbed, and the world goes dark as you collapse to the floor. GAME OVER"
        running = False
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
        pygame.mixer.music.load('./data/2018-07-02_-_Tears_of_Joy_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        message = "You feel an intense cold, and your muscles lock into place. The sound of a scream shreds through your ears, and then the room grows impossibly silent. You are still frozen in place, but feel the crumpled photo in your pocket shift. Before your eyes, it unfolds in midair, and suddenly the foggy silhouette of a man stands before you. His eyes are sad, but he is smiling just a bit. 'Thank you' - the words echo through your head. The ghost disappears. You crumple to the floor, and watch in awe as the room around you grows brighter, as though the sun has come up. The cold leaves your body, and you know, with absolute certainty, that all is well. CONGRATULATIONS. YOU FREED THE GHOST, AND WON THE GAME."
        running = False
        # replay = input('Would you like to start over? Y or N ')
        # if replay.lower() == "y":
        #     player = Player(room['outside'])
        #     ghost = Player(room[random.choice(ghost_rooms)])
        #     welcome = (f'Welcome! Your current location is: {player.room_info()}')
        #     print(welcome)
        # elif replay.lower() == "n":
        #     exit()
    if player.current_room.name == "Hidden Room" and "key" not in player.inventory:
        pygame.mixer.music.load('./data/2020-02-16_-_Anxiety_-_David_Fesliyan.mp3')
        pygame.mixer.music.play()
        message = "You search and search, but there is nothing in this room to save you. The light, once bright, gradually goes dim, and after some amount of time you cannot comprehend, you sit opposite the skeleton, close your eyes, and succumb to sleep. <br><br> GAME OVER"
        running = False
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

    # elif direction == 'i':
    #     invest = player.investigate()
    #     object = invest[14:-1]
    #
    #     if invest != "There is nothing here.":
    #         return invest, item(player, ghost, object)
    #     else:
    #         return invest, player, ghost

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
