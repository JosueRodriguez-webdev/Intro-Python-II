# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, location, inventory=None):
        self.name = name
        self.location = location
        self.inventory = []

    def move(self, direction):
        if self.location.connections[direction] is not None:
            self.location = self.location.connections[direction]
        else:
            print('try again')

    def add_item(self, name, description):
        self.inventory.append(name)

    def remove_item(self):
        self.inventory.pop()
