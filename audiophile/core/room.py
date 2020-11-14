import pygame

pygame.display.init()
pygame.display.set_mode((640, 480))

class Room():
    def __init__(self, name, description, background, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load(background)
        self.background = self.background.convert()
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def add_item(self, item_name):
        self.items = item_name

    def item_taken(self, item):
        self.items = None

# Declare all the rooms
room = {
    'outside':  Room("Outside the House",
                     """You stand outside a simple, two-story house. Will you open the door?""",
                     './data/house.jpg'),

    'foyer':    Room("Foyer",
                     """Softly illuminated ahead of you is a staircase, and there are rooms to either side. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/foyer.jpg'),

    'living':   Room("Living Room",
                     """You enter what appears to be the living room. Couches covered in plastic are pushed up against the walls and a fireplace sits under the stairs. Moonlight filters in through the window, enough to reveal a shadow to the north, but you can't tell what it is. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/living.jpg'),

    'piano':    Room("Piano Room",
                     """You continue north and the floor beneath you shifts from worn-down carpet to cracked tiles. A grand piano, covered in dust, takes up the entire space. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/piano.jpg'),

    'dining':   Room("Dining Room",
                     """This room smells of rotting wood - an ancient table sits in the center, with six chairs around it, in various states of destruction. A glint of metal shines to the north. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/dining.jpg'),

    'kitchen':  Room("Kitchen",
                     """This must have been the kitchen once. All the large items have been stripped, leaving gaping holes in their place, but the sink, which was what caught your light, is still here. The cabinets smell worse of rot than the dining room table did. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/kitchen.jpg'),

    'stairs':   Room("Stairs",
                     """You reach the top of the stairs. Dark hallways extend to either side, and directly in front of you is a cracked-open door. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/stairs.jpg'),

    'whall':    Room("Hallway",
                     """There are sliding doors to the north and a regular door to the south. The hallway continues to the west and the east. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/hallway.jpg'),

    'ehall':    Room("Hallway",
                     """Nothing but an open door to the south and more hallway to the east. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/hallway.jpg'),

    'whall2':   Room("Hallway",
                     """You have gone as far west as you seem to be able to. There are doors to the north and the south. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/wall.jpg'),

    'ehall2':   Room("Hallway",
                     """You have gone as far east as you seem to be able to. There is only a door to the south. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/wall.jpg'),

    'nursery':  Room("Nursery",
                     """This room once held joy, and perhaps that makes it harder to stand in. An empty bassinet sits by the window. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/nursery.jpg'),

    'vacant':   Room("Vacant Room",
                     """There is nothing here. The walls feel and look like concrete. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/vacant.jpg'),

    'laundry':  Room("Laundry Room",
                     """There is barely enough room for the door to open - you squeeze inside to find a rusted washer and dryer. Something clatters behind them. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/laundry.jpg'),

    'linen':    Room("Linen Closet",
                     """You slide the doors open to the smell of musty, damp cloth. There is enough room for a person to fit between the doors and the shelves, but only just. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/linen.jpg'),

    'primary':  Room("Primary Bedroom",
                     """This room carries an aura of strange grandeur; the bed looks as though it was made just this morning. On the west wall, there seems to be a closet, and to the east, there is another door. A horrid smell leaks out from behind it. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/primary.jpg'),

    'closet':   Room("Closet",
                     """Empty hangers and a single pair of red heels sit neatly in the closet. It is smaller than you would have expected. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/closet.jpg'),

    'secret':   Room("Hidden Room",
                     """You squeeze through the small opening and find yourself in a room, several times larger than the closet. This room is bright, and it takes your eyes a moment to adjust. When they do, you realize what you are looking at - a full skeleton, slumped against the wall. Its hand is wrapped around something, but you only just have time to notice this before there is a noise from behind you. The panel whirs and clicks back into place. The surface is smooth except for a keyhole in in the center. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/secret.jpg'),

    'pbath':    Room("Primary Bathroom",
                     """You push the door open and the smell intensifies. If not for that, though, this is a perfectly normal bathroom, also pristine. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/pbath.jpg'),

    'bedroom':  Room("Bedroom",
                     """This room is bare, except for an empty bed frame and a nightstand. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/bedroom.jpg'),

    'bath':     Room("Bathroom",
                     """Here, the smell of mold. The porcelain tub is halfway full of brown water. What would you like to do? (N to go north, S to go south, E to go east, W to go west, I to investigate the room, IN to view your inventory, USE to use an item, DROP to drop an item, H for a hint, Q to quit)""",
                     './data/bathroom.jpg'),
}

ghost_rooms = ['living', 'piano', 'dining', 'kitchen', 'nursery', 'laundry',
               'bedroom', 'bath', 'pbath', 'primary', 'closet', 'vacant',
               'linen']
