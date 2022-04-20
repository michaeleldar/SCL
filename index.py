import scratchconnect
from sys import argv
import os
import browser_config
import datetime
if argv.__len__() == 1:
    print("""
Usage:
scl sign-in <username> <password>: Signs you in to your scratch account.
scl version: Prints the version and exits.
scl myid: Prints your scratch ID.
scl mythumbnail: Opens your thumbnail in the browser.
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
            url = user.thumbnail_url()
            print("Going to " + url["90x90"])
            os.system(browser_config.browser_command + url["90x90"])
        elif argv[1] == "messages":
            if user.messages_count() == 1:
                print("You have " + str(user.messages_count()) + " new message.")
            else:
                print("You have " + str(user.messages_count()) + " new messages.")
            if argv.__len__() == 3:
                print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[2], end=" ")
                print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][0]['id'], end=" ")
            else:
                print(user.messages(all=False, limit=user.messages_count(), offset=0, filter="all"))
                
        else:
            print("ERROR: No command \"" + argv[1] + "\".")