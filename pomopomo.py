#THIS APP NEED ACCESS TO WRITE,READ,WATCH THE TIME
#TODO IMPLEMENT "TITLE" COMPATIBILITY
#TODO CRON IMPLEMENTATION / (AUTO TASKs)..
#TODO WHATSAPP API / SOCIAL NETWORK NOTIFICATIONS
###################################################

import time

def remove_decimals(string_or_float_int):
    return str(int(float(string_or_float_int)))

#Reads the last register
#TODO TITLES
def readfile():
    lastrecord = ""
    with open("db","r") as f:
        lastrecord = f.read()
    return lastrecord

#Write the database
#TODO TITLES
def startpomodoro_now():
    with open("db","w+") as f:
        f.write(remove_decimals(time.time()))
    

def calculate_expiration(register):
    register = int(register)
    timenow = time.time()
    #Removes decimals for easy use
    timenow = int(remove_decimals(time.time()))

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
        #TODO TITLE
        # startpomodoronow(input("What is the title? Enter=Default\n"))
        startpomodoro_now()
        print(readfile())
    if choice == "2":
        #TODO TITLE (PRINT LIST OF CHOICES)
        #print(calculate_expiration(readfile(input("has a title? Enter=Default\n"))))
        print(calculate_expiration(readfile()))
    elif choice == "3":
        exit()