"""Handles Players."""

import util
import mapSystem

Players = [
    0 #Player 0 is the U n i v e r s e (it's actually not)
    ]

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

        self.PlayerId = Players[-1]+1
        Players.append(self)

    def getId(self):
        return self.PlayerId

    def getName(self):
        return self.name

    def turn(self):
        print(mapSystem.getMapPosInfo(self.rx,self.ry))
        
    def directionalMove(self,direction):
        """Will move the player in a direction.
           Expects a direction.
           N/W/E/S. Will error out if not one of these."""
        if direction == 'N' or direction == 'E' or direction == 'S' or direction == 'W':
            if mapSystem.getMapPosInfo(self.rx,self.ry)[direction]:
                oldx,oldy = self.rx,self.ry
                if direction == 'N':
                    self.ry -= 1
                elif direction == 'E':
                    self.rx += 1
                elif direction == 'S':
                    self.ry += 1
                elif direction == 'W':
                    self.rx -= 1
                if not mapSystem.isMapPosValid(self.rx,self.ry):
                    self.rx,self.ry = oldx,oldy
            else:
                print("Can't go that way!")
                
            if mapSystem.isMapPosValid(self.rx,self.ry) == 'Valid':
                print("Valid.")
            else:
                print("Position Invalid.")
                self.rx,self.ry = oldx,oldy
        else:
            print(direction)
            
