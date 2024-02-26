import pygame
import os
from natsort import natsorted, ns

# Initialize the pygame mixer 
pygame.mixer.init() 
 
# Load a sound file 
dir = os.fsencode("sounds")
loadedSounds = {}

def loadSounds():
    index = 0
    for f in natsorted(os.listdir("sounds"), alg=ns.PATH | ns.IGNORECASE):
        path = os.fsdecode("sounds/%s" % os.fsdecode(f))
        loadedSounds[path] = pygame.mixer.Sound(path)
        index = index + 1
    print("Loaded %s sounds!" % index)

loadSounds()

while (True):
    print("Sound yang ke load:")
    i = 0
    for p in loadedSounds:
        print("{}: {}".format(i, p))
        i = i + 1
    inp = input("Mau play yang mana?: ")
    if (inp.startswith("s")):
        if (len(inp.split(" ")) == 1):
            pygame.mixer.fadeout(1000)
            print("Stopped music with fadeout of 1000ms")
        else:
            pygame.mixer.fadeout(int(inp.split(" ")[1]))
            print("Stopped music with fadeout of " + inp.split(" ")[1] + "ms")
        
    elif (inp == "e"):
        exit(0)
    else:
        #try:
            list(loadedSounds.values())[int(inp)].play()
            print("played")
        #except:
            #print("maksute lo")