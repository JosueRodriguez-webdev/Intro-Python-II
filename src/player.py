# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def move(self, direction):
        if self.location.connections[direction] is not None:
            self.location = self.location.connections[direction]
        else:
            print('try again')
