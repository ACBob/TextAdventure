import player
class direction:
    def __init__(self,direction):
        """Probably Wasteful."""
        if direction == 'N'or'W'or'S'or'E':
            self.direction = direction
        else:
            print("Invalid Direction")
            return 1

def getPlayerFromId(ID):
    return player.Players[ID]

def RemovePlayer(ID):
    player.Players.pop(int(ID))
