"""Handles Commands."""

import shared
from utilityprints import *
import util

class Command:
    _registry = []
    def __init__(self,Name,Description,HasArgs,Usage=None):
        """Probably Dangerous to make it run python code, WILL have to change."""
        self.Name = Name
        self.Description = Description
        self.Code = 'print("Depracated.")'
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
        print('Running',self.Name)
        if len(args)>0 and self.HasArgs:
            print('We have arguments, and they are there. Executing.')
            output = exec(self.Code)
            print(output)
            return Magic[self.Name](args)
        elif not self.HasArgs:
            print('We dont have arguments, and were executing.')
            return Magic[self.Name](args)
        else:
            print('We probably have arguments, and they arent there, not executing.')
            return self.Usage

def Say(text):
    print('We are the Say Command, and weve been told to run.')
    return text

def Help(command):
    print('We are the Help Command, and weve been told to run.')
    Output = Commands[''.join(command)].getDescription()
    print('Output of Help is',Output)
    return Output


#if shared.debug: Command('Test','Does Test','print("This should say this.")',False)

Command('Help','Provides Useful help to Specified command.',True)

Command('Say','Says the Input Text.',True,'You attempt to speak, but nothing escapes your lips.')

#Command('MyID','Provides Your ID.','print(FirerId)',False)
#Command('MyName','Provides Your Name.','print(util.getPlayerFromId(FirerId).getName())',False)

#Command('Die','Stops your heart.','print("Your heart stops beating, and you stop breathing. You are Dead. Game Over.") ; exit',False)

#Command('Move','Moves in Specified Direction.','util.getPlayerFromId(id).directionalMove(direction)',False)

global Commands
Commands = {}

global Magic
Magic = locals()

for command in Command._registry:
    print(str(command)+':'+command.getName())
    Commands[command.getName()] = command
print(Commands)
#print(type(Commands))

def RunCommand(command,args,FirerId):
    #print(command)
    print('Command system was told to run',command,'with',args,'by',FirerId)
    try: Command = Commands[command]
    except KeyError:
        print('Failed, retruning error message.')
        return "I don't know how to %s."%command
    print('Attempting to run said command.')
    return Command.Run(args,FirerId)

