import scratchconnect
from sys import argv
import os
import browser_config
if argv.__len__() == 1:
    print("""
Usage:
scl sign-in <username> <password>: Signs you in to your scratch account.
scl version: Prints the version and exits.
scl myid: Prints your scratch ID.
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
        if argv[1] == "version" or argv[1] == "--version" or argv[1] == "-v":
            print("Scratch Command Line 1.0.0 by Michael Halpin.")
            quit()
        elif argv[1] == "myid":
            print(user.id())
            quit()
        elif argv[1] == "mythumbnail":
            os.system(browser_config.browser_command + user.thumbnail_url)
        else:
            print("ERROR: No command \"" + argv[1] + "\".")