"""Handles Commands."""

import shared
from utilityprints import *
import util
import mapSystem

class Command:
    _registry = []
    def __init__(self,Name,Description,Code,HasArgs,Usage=None):
        """Probably Dangerous to make it run python code, WILL have to change."""
        self.Name = Name
        self.Description = Description
        self.Code = Code
        self.HasArgs = HasArgs
        if Usage == None and HasArgs:
            self.Usage = self.Name +' <args>'
        elif Usage == None and not HasArgs:
            self.Usage = self.Name
        else: self.Usage = Usage

        self._registry.append(self)

    def getDescription(self):
        return self.Description

    def getName(self):
        return self.Name

    def Run(self,args,FirerId):
        if len(args)>0 and self.HasArgs: exec(self.Code)
        elif not self.HasArgs: exec(self.Code)
        else: Info(self.Usage)

def HelpCommand(command):
    print(Commands[''.join(command)].getDescription())
def MapCommand(pId):
    the_Map = mapSystem.getMap()
    thePlayer = util.getPlayerFromId(pId)
    the_Map[thePlayer.ry] = the_Map[thePlayer.ry][:thePlayer.rx]+'x'+the_Map[thePlayer.ry][thePlayer.rx+1:]
    for i in the_Map:
        print(i.replace('\n',''))

#if shared.debug: Command('Test','Does Test','print("This should say this.")',False)

Command('Help','Provides Useful help to Specified command.','HelpCommand(args)',True)

Command('MyID','Provides Your ID.','print(FirerId)',False)
Command('MyName','Provides Your Name.','print(util.getPlayerFromId(FirerId).getName())',False)

#Command('Die','Stops your heart.','print("Your heart stops beating, and you stop breathing. You are Dead. Game Over.") ; exit',False)

Command('Move','Moves in Specified Direction.','print(len(args[0]));util.getPlayerFromId(FirerId).directionalMove(args[0])',True)

Command('Map','Shows the Map.',"MapCommand(FirerId)",False)

global Commands
Commands = {}

for command in Command._registry:
    print(str(command)+':'+command.getName())
    Commands[command.getName()] = command
print(Commands)
#print(type(Commands))

def RunCommand(command,args,FirerId):
    #print(command)
    try: Commands[command].Run(args,FirerId)
    except KeyError:
        print("I don't know how to %s."%command)

