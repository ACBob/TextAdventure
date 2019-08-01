#another? seriously?


import player
import commandSystem

def mainLoop():
    print("Main loop")
    isRunning = True
    playerCharacter = player.spPlayer(0,0,'George')
    while isRunning:
        action = input(': ')
        actionArgs = action.split(' ')[1:]
        command = action.split(' ')[0]
        if action == 'Quit':
            print("Quit.")
            return 0
        else:
            commandSystem.RunCommand(command,actionArgs)




mainLoop()
