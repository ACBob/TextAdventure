
import shared
import datetime

def Info(text):
    print("[Info]: "+text)
def Debug(text):
    if shared.debug: print("%s{DEBUG} "%(str(datetime.datetime.now().time())[0:5])+text)
