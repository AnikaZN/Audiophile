from room import Room
from player import Player
from item import Item


# Declare all the rooms
room = {
    'outside':  Room("Outside the House",
                     "You stand outside a simple, two-story house. Will you open the door?"),

    'foyer':    Room("--- Foyer",
                     """Softly illuminated ahead of you is a staircase, and there are rooms to either side."""),

    'living':   Room("--- Living Room",
                     """You enter what appears to be the living room. Couches covered in plastic are pushed up against the walls and a fireplace sits under the stairs. Moonlight filters in through the window, enough to reveal a shadow to the north, but you can't tell what it is."""),

    'piano':    Room("--- Piano Room",
                     """You continue north and the floor beneath you shifts from worn-down carpet to cracked tiles. A grand piano, covered in dust, takes up the entire space."""),

    'dining':   Room("--- Dining Room",
                     """This room smells of rotting wood - an ancient table sits in the center, with six chairs around it, in various states of destruction. A glint of metal shines to the north."""),

    'kitchen':  Room("--- Kitchen",
                     """This must have been the kitchen once. All the large items have been stripped, leaving gaping holes in their place, but the sink, which was what caught your light, is still here. The cabinets smell worse of rot than the dining room table did."""),

    'stairs':   Room("--- Stairs",
                     """You reach the top of the stairs. Dark hallways extend to either side, and directly in front of you is a cracked-open door."""),

    'whall':    Room("--- Hallway",
                     """There are sliding doors to the north and a regular door to the south. The hallway continues to the west and the east."""),

    'ehall':    Room("--- Hallway",
                     """Nothing but an open door to the south and more hallway to the east."""),

    'whall2':   Room("--- Hallway",
                     """You have gone as far west as you seem to be able to. There are doors to the north and the south."""),

    'ehall2':   Room("--- Hallway",
                     """You have gone as far east as you seem to be able to. There is only a door to the south."""),

    'nursery':  Room("--- Nursery",
                     """This room once held joy, and perhaps that makes it harder to stand in. An empty bassinet sits by the window."""),

    'vacant':   Room("--- Vacant Room",
                     """There is nothing here. The walls feel and look like concrete."""),

    'laundry':  Room("--- Laundry Room",
                     """There is barely enough room for the door to open - you squeeze inside to find a rusted washer and dryer. Something clatters behind them."""),

    'linen':    Room("--- Linen Closet",
                     """You slide the doors open to the smell of musty, damp cloth. There is enough room for a person to fit between the doors and the shelves, but only just."""),

    'primary':  Room("--- Primary Bedroom",
                     """This room carries an aura of strange grandeur; the four-poster bed looks as though it was made just this morning. On the west wall, there seems to be a closet, and to the east, there is another door. A horrid smell leaks out from behind it."""),

    'closet':   Room("--- Closet",
                     """Empty hangers and a single pair of red heels sit neatly in the closet. It is smaller than you would have expected."""),

    'secret':   Room("--- Hidden Room",
                     """You squeeze through the small opening and find yourself in a room, several times larger than the closet. This room is bright, and it takes your eyes a moment to adjust. When they do, you realize what you are looking at - a full sekeleton, slumped against the wall. The panel clicks into place behind you."""),

    'pbath':    Room("--- Primary Bathroom",
                     """You push the door open and the smell intensifies. If not for that, though, this is a perfectly normal bathroom, also pristine."""),

    'bedroom':  Room("--- Bedroom",
                     """This room is bare, except for an empty bed frame and a nightstand."""),

    'bath':     Room("--- Bathroom",
                     """Here, the smell of mold. The porcelain tub is halfway full of brown water."""),
}

# Put items in rooms
room['outside'].add_item('pebble')

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
room['ehall'].e_to = room['ehall2']
room['ehall'].s_to = room['bedroom']
room['ehall'].w_to = room['stairs']
room['ehall2'].s_to = room['bath']
room['ehall2'].w_to = room['ehall']
room['bath'].n_to = room['ehall2']
room['bedroom'].n_to = room['ehall']

# Main
name = input('What is your name? ')

player = Player(name, room['outside'])

print(f'--- Welcome, {player.name}! Your current location is: {player.room_info()}')

def item(player, item):
    interact = input('What would you like to do? (HINT: You may "take" or "ignore" an item.) ')
    interact = interact.lower()

    if interact == 'take':
        player.inventory.append(item)
        print(f'--- You now have {player.inventory} in your inventory.')
        player.current_room.item_taken(item)
        gameplay(player)
    elif interact == 'ignore':
        print('--- You leave it there.')
        gameplay(player)
    else:
        print('--- There seems to have been an error. Please try again.')
        gameplay(player)

def gameplay(player):
    direction = input('What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to interact with your inventory, Q to quit) ')
    direction = direction.lower()

    if direction == 'n':
        location = player.current_room.n_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('--- There is nothing to the north. Please choose a different direction.')
            gameplay(player)
    elif direction == 's':
        location = player.current_room.s_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the south. Please choose a different direction.')
            gameplay(player)
    elif direction == 'e':
        location = player.current_room.e_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the east. Please choose a different direction.')
            gameplay(player)
    elif direction == 'w':
        location = player.current_room.w_to
        if location != None:
            player = Player(name, location)
            print(player.room_info())
            gameplay(player)
        else:
            print('There is nothing to the west. Please choose a different direction.')
            gameplay(player)

    elif direction == 'i':
        print(player.investigate())
        object = player.investigate()[14:-1]

        if player.investigate() != "--- There is nothing here.":
            item(player, object)
        else:
            gameplay(player)

    elif direction == 'in':
        if player.inventory != []:
            print(f'--- You currently have {player.inventory} in your inventory.')
            command = input('You can "drop" an item or "use" an item. Please name the item. (Example: "use pebble") ')
            command = command.lower()
            action, thing = command.split(' ')[0], command.split(' ')[1]
            if action == 'drop':
                if thing in player.inventory:
                    player.inventory.remove(thing)
                    player.current_room.add_item(thing)
                    print(f'--- You currently have {player.inventory} in your inventory.')
                    gameplay(player)
                else:
                    print('--- There seems to have been an error. Please try again.')
                    gameplay(player)
            elif action == 'use':
                if thing == "rope":
                    if player.current_room.name == "--- Grand Overlook":
                        print('--- Success! You fashion a swing and lauch yourself across the chasm, landing safely on the other side.')
                        player.current_room = room['sphinx']
                        print(player.room_info())
                        gameplay(player)
                    else:
                        print(f'The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "sword":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- You draw your sword and manage to slay the sphinx with one quick slash.')
                        print('--- You leave the cave dirty and tired, but alive.')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "coin":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The sphinx contemplates your offering for a moment, then chuckles. "Congratulations, Adventurer." It gets to its feet and steps to the right, revealing a massive pile of treasure.')
                        print('--- You leave the cave richer than when you started, and solved the mystery of the long-lost treasure. Congratulations!')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "key":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The sphinx seems to smile as it silently stands and steps to the left, revealing a door. "You are truly worthy," it says. You step forward, unlock the door, and see a shimmering fountain.')
                        print('--- Congratulations, you have discovered the Fountain of Youth! You now have the ability to live forever.')
                        print('--- Thanks for playing!')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                elif thing == "pebble":
                    if player.current_room.name == "--- Sphinx Chamber":
                        print('--- The laughter of the sphinx is the last thing you hear. It snaps you up in one bite.')
                        print('--- Oh no, you died! Please try again.')
                    else:
                        print(f'--- The {thing} does not do anything here.')
                        gameplay(player)
                else:
                    print(f'--- The {thing} does not do anything here.')
                    gameplay(player)
            else:
                print('--- There seems to have been an error. Please try again.')
                gameplay(player)
        else:
            print('You have nothing in your inventory.')
            gameplay(player)


    elif direction == 'q':
        print('--- Farewell, adventurer!')

    else:
        print('---There seems to have been an error. Please try again.')
        gameplay(player)

if __name__ == '__main__':
    gameplay(player)
