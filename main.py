#another? seriously?


import player
import commandSystem
import shared

from utilityprints import *

def mainLoop():
    Debug("Main loop")
    isRunning = True
    playerCharacter = player.spPlayer(0,0,'George')
    while isRunning:
        action = input(': ')
        actionArgs = action.split(' ')[1:]
        command = action.split(' ')[0]
        if action == 'Quit':
            Info("Quit.")
            return 0
        else:
            commandSystem.RunCommand(command,actionArgs,playerCharacter.getId())



shared.debug = True
Info("Debug. Remember to disable.")

mainLoop()
