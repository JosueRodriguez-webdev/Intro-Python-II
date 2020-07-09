from room import Room
from player import Player
from item import Item
import textwrap


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item('knife', 'cuts'), Item('gun', 'shoots')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item('knife', 'cuts'), Item('gun', 'shoots')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item('knife', 'cuts'), Item('gun', 'shoots')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item('knife', 'cuts'), Item('gun', 'shoots')]),
}


# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
user = Player('josue', room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game..

user_is_playing = True

while user_is_playing:
    print(user.location.name)

    for line in textwrap.wrap(user.location.desc, 40):
        print(line)

    player_quits = False

    if len(user.location.items) > 0:
        player_quits = True
    print(user.inventory)

    while player_quits:
        for item in user.location.items:
            print(
                f'Item Found!:\n{item.name}: {item.desc}')
        user_choice = input(
            "Items Found! pick up item (p), drop item(d), or skip (s)\n\n")
        if user_choice.lower() == 's':
            player_quits = False
        elif user_choice.lower() == 'p':
            user.add_item(item.name, item.desc)
        elif user_choice.lower() == 'd':
            pass
        else:
            print(f"command not recognized, try again...")
    print(user.inventory)

    direction = input("Pick a direction (n,e,s,w) or quit the game (q):")

    if direction in ["n", "e", "s", "w"]:
        user.move(direction)
    elif direction == 'q':
        print('Quitting game')
        user_is_playing = False
    elif direction == 'i':
        player_quits = True
    else:
        print("\ndirection not valid, please submit one of these choices ((n,e,s,w) to move, or quit the game (q))\n")
