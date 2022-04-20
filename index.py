import scratchconnect
from sys import argv
if argv.__len__() == 1:
    print("""
Usage:
scl sign-in <username> <password>
""")
else:
    if argv[1] == "sign-in":
        if argv.__len__() == 4:
            try:
                user = scratchconnect.ScratchConnect(argv[2], argv[3])
                userw = open("signed-in-user", 'w')
                userw.write(argv[2] + " " + argv[3])
                userw.close()
            except:
                print("ERROR: Incorrect password or username.")
                quit()
        else:
            print("ERROR: Incorrect usage, scl sign-in <username> <password>.")
            quit()
    else:
        try:
            userr = open("signed-in-user", 'r')
            usert = userr.read().split()
            userr.close()
            user = scratchconnect.ScratchConnect(usert[0], usert[1])
        except:
            print("ERROR: You need to be signed in to use SCL.")
            quit()
