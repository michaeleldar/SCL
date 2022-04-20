import scratchconnect
from sys import argv
if argv[1] == "sign-in":
    user = scratchconnect.ScratchConnect(argv[2], argv[3])
    userw = open("signed-in-user", 'w')
    userw.write(argv[2] + " " + argv[3])
    userw.close()
else:
    try:
        userr = open("signed-in-user", 'r')
        usert = userr.read().split()
        userr.close()
        user = scratchconnect.ScratchConnect(usert[0], usert[1])
    except:
        print("ERROR: You need to be signed in to use SCL.")
        quit()