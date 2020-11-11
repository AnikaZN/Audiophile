from core.room import Room


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
        if item != None:
            return f'You see a {item}.'
        else:
            return "There is nothing here."
