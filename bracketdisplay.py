#create a program that takes user input and displays it as "[input] at Station X"


stationList = {}
stationTot = -1

# user input to determine how many stations will be available at today's event
while stationTot < 0:
    stationTot =int( input("How many stations at today's event? "))
    if int(stationTot) > 0:
        continue
    else:
        print("Please enter an amount greater than 0.")
        stationTot = -1

# when the event starts, all stations are open, so creating a dictionary that notates that each station
# is open until it isn't

for x in range(0, stationTot):
    stationList ["Station {0}".format(x)] = "Walk-In"

#this is where I want to display the current status of the stations in a for loop
def stationAvail():
    #basic for loop printing out the status and availability of all stations
    for station, patient in stationList.items():
        print(patient, "at", station)

#a function that allows me to make edits to the values
def changeStat():
    changes = True
    while changes == True:
        applicStat = input("Which station does this refer to? (ex: \'Station 3\') ")
        if applicStat not in stationList.keys():
             print("Couldn't find that station. Try it again.")
        else:
            applicPat = input("Which patient/number is at that station? (ex: D433) ")
            stationList[applicStat] = applicPat
            print("Thanks. Should be updated in the system now.")
            verify = input("Any more changes? (Y/N) ")
            if verify == "n" or "N":
                changes = False
            elif verify == "y" or "Y":
                changes = True

