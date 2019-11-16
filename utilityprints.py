
import shared
import datetime

def Info(text):
    print("\u001b[33;1m[Info]: {}\u001b[0m".format(text))
def Debug(text):
    if shared.debug: print("\u001b[32;1m<Debug>: {}\u001b[0m".format(text))
