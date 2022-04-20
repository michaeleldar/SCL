import scratchconnect
from sys import argv
if argv[1] == "sign-in":
    user = scratchconnect.ScratchConnect(argv[2], argv[3])