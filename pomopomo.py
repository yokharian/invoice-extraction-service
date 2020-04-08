#THIS APP NEED ACCESS TO WRITE,READ,WATCH THE TIME
#TODO GPIO RASPBERRY PI ACCESS, BUTTONS AND AUTOMATION
#TODO CRON IMPLEMENTATION / (AUTO TASKs)..
###################################################

import time


#Reads the last register
def readfile():
    lastrecord = ""
    with open("db","r") as f:
        lastrecord = f.read()
    return lastrecord

#Write the database
def startpomodoro_now():
    with open("db","w+") as f:
        f.write(time.time())
    

def calculate_expiration(register):
    register = int(register)
    timenow = int(time.time())

    is_expirated = lambda old: (old + (60*25) ) <= timenow
    if is_expirated(register):
        return "Finalizó"
    else:
        return ("hacen falta {} segundos para terminar".format(
            (25*60) - (timenow-register))) 


#MAIN LOOP
while(True):
    choice = input("""Choose an option
    (1) Start a pomodoro
    (2) Check date of expiration
    (3) Exit\n""")

    if choice == "1":
        startpomodoro_now()
        print(readfile())
    elif choice == "2":
        print(calculate_expiration(readfile()))
    elif choice == "3":
        exit()
