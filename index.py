import scratchconnect
from sys import argv
import os
import browser_config
if argv.__len__() == 1:
    print("""
parameters between < and > are required, while paramaters between [ and ] are optional
Usage:
scl sign-in <username> <password>: Signs you in to your scratch account.
scl version: Prints the version and exits.
scl myid: Prints your scratch ID.
scl mythumbnail: Opens your thumbnail in the browser.
scl messages [amount to view]: Prints out how many unread messages you have, and if amount to view to set, the latest <amount of view> messages else it will show all unread messages.

report errors at https://scratch.mit.edu/users/applejuiceproduc
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
            print("report errors at https://scratch.mit.edu/users/applejuiceproduc")
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
                
                for x in range(0, int(argv[2])):
                    if user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['type'] == "addcomment":
                        print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['actor_username'], end=" ")
                        if user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['comment_type'] == 0:
                            print("commented on the project,", end=" ")
                        elif user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['comment_type'] == 1:
                            print("commented on your profile,", end=" ")
                        elif user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['comment_type'] == 2:
                            print("replied to your all in the studio,", end=" ")
                        else:
                            print("ERROR: scl error, unhandled all type. Please report this at https://scratch.mit.edu/users/applejuiceproduc")
                            quit()
                        if not user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['comment_type'] == 1:
                            print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]["comment_obj_title"], end=" ")
                        print("\"" + user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['comment_fragment'].replace("&#39;", "'") + "\"", end="\n\n")
                    elif user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['type'] == "studioactivity":
                        print("There was new activity in the studio", end=" ")
                        print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['title'], end=" ")
                        print("today.", end="\n\n")
                    elif user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['type'] == "remixproject":
                        print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['actor_username'], end=" ")
                        print("remix your project \"", end="")
                        print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['parent_title'], end="")
                        print("\" into \"", end="")
                        print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][x]['title'], end="")
                        print("\".\n\n")
                    else:
                        print("ERROR: scl error, unhandled message type. Please report this at https://scratch.mit.edu/users/applejuiceproduc")
                        quit()
                
                #print(user.messages(all=False, limit=int(argv[2]), offset=0, filter="all")[0][5], end=" ")
            else:
                print(user.messages(all=False, limit=user.messages_count(), offset=0, filter="all"))
                
        else:
            print("ERROR: No command \"" + argv[1] + "\".")