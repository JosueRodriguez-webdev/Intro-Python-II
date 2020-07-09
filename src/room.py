# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, items=[], n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.desc = desc
        self.items = items
        self.connections = {
            "n": n_to,
            "e": e_to,
            "s": s_to,
            "w": w_to,
        }
