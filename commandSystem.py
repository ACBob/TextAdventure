"""Handles Commands."""

class Command:
    _registry = []
    def __init__(self,Name,Description,Code,Usage=None):
        """Probably Dangerous to make it run python code, WILL have to change."""
        self.Name = str(Name)
        self.Description = str(Description)
        self.Code = Code
        if Usage == None:
            self.Usage = self.Name +' <args>'

        self._registry.append(self)

    def getDescription(self):
        return self.Description

    def getName(self):
        return self.Name

    def RunNoArgs(self):
        exec(self.Code)

    def Run(self,args):
        exec(self.Code)

def HelpCommand(command):
    print(Commands[''.join(command)].getDescription())


Command('Test','Does Test','print("test")')

Command('Help','Provides Useful help to Specified command.','HelpCommand(args)')

Commands = {}

for command in Command._registry:
    print(str(command)+':'+command.getName())
    Commands[command.getName()] = command
print(Commands)
#print(type(Commands))

def RunCommand(command,args):
    print(command)
    if len(args) > 0:
        Commands[command].Run(args)
    else:
        Commands[command].RunNoArgs()
