"""Handles Players."""

import util

class spPlayer:
    def __init__(self,rx,ry,name):
        """rx = Room X
           ry = Room Y
           Name is for a little customisation.
           rx/ry is used for getting the current room.
           Will reset to 0,0 if we go out of bounds."""

        self.name = name
        self.rx = rx
        self.ry = ry
    def directionalMove(direction):
        """Will move the player in a direction.
           Expects a direction.
           N/W/E/S. Will error out if not one of these."""
        if not type(direction) == util.direction:
            print("Given is not a direction!")
            return 1 #Linux Documentation, Exit Codes.
        else:
            print("TODO: Implement Directional Change.")
            print(direction)
