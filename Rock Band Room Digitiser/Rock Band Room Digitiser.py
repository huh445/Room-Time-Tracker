import tkinter as tk  # imports tkinter
from tkinter import PhotoImage # needed to import an image
import time  # imports the time module for the stopwatch
import mysql.connector # needed for compatibility with mySQL
from pathlib import Path # needed to get the relative path of an image

root = tk.Tk()  # defines tkinter as root
root.title('Rock Band Room Tracker') # the title of the tkinter window

cnx = None # initialises the variable
cnx = mysql.connector.connect(user='root', password='root',
                            host='localhost', port='3306',
                            unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
                            database='db_rockband') # connects to the mySQL database

# initialises the variables so they can be used globally
room = 0
checkTimer1 = 0
checkTimer2 = 0
checkTimer3 = 0
checkTimer4 = 0
checkRoomOne = 0
checkRoomTwo = 0
checkRoomThree = 0
checkRoomFour = 0
studentName = 0
room1Student = 0
room2Student = 0
room3Student = 0
room4Student = 0
okButtonCheck1 = 0
okButtonCheck2 = 0
okButtonCheck3 = 0
okButtonCheck4 = 0

# Room 1 Timer
def timer_room1():
    global checkTimer1
    global start1
    if checkTimer1 == 1: # if the timer is currently running
        stop1 = time.time() # defines a variable that helps in the final calculation
        how_long1 = stop1 - start1 # start of timer minus end of timer
        time_maker(how_long1) # calls the time_maker module to fix the time
        room1Timer.configure(text=timeactual) # changes the label to the stopwatch
        sqlTime() # calls the sqlTime module so that the database can be updated
        checkTimer1 = 0 # resets the timer so it can be run again
    elif checkTimer1 == 0: # if the timer hasnt been running
        start1 = time.time() # starts the timer
        checkTimer1 = 1 # so it can stop the timer when run again

# Room 2 Timer
def timer_room2():
    global checkTimer2
    global start2
    if checkTimer2 == 1: # if the timer is currently running
        stop2 = time.time() # defines a variable that helps in the final calculation
        how_long2 = stop2 - start2 # start of timer minus end of timer
        time_maker(how_long2) # calls the time_maker module to fix the time
        room2Timer.configure(text=timeactual) # changes the label to the stopwatch
        sqlTime() # calls the sqlTime module so that the database can be updated
        checkTimer2 = 0 # resets the timer so it can be run again
    elif checkTimer2 == 0: # if the timer hasnt been running
        start2 = time.time() # starts the timer
        checkTimer2 = 1 # so it can stop the timer when run again

# Room 3 Timer
def timer_room3():
    global checkTimer3
    global start3
    if checkTimer3 == 1: # if the timer is currently running
        stop3 = time.time() # defines a variable that helps in the final calculation
        how_long3 = stop3 - start3 # start of timer minus end of timer
        time_maker(how_long3) # calls the time_maker module to fix the time
        room3Timer.configure(text=timeactual) # changes the label to the stopwatch
        sqlTime() # calls the sqlTime module so that the database can be updated
        checkTimer3 = 0 # resets the timer so it can be run again
    elif checkTimer3 == 0: # if the timer hasnt been running
        start3 = time.time() # starts the timer
        checkTimer3 = 1 # so it can stop the timer when run again

# Room 4 Timer
def timer_room4():
    global checkTimer4
    global start4
    if checkTimer4 == 1: # if the timer is currently running
        stop4 = time.time() # defines a variable that helps in the final calculation
        how_long4 = stop4 - start4 # start of timer minus end of timer
        time_maker(how_long4) # calls the time_maker module to fix the time
        room4Timer.configure(text=timeactual) # changes the label to the stopwatch
        sqlTime() # calls the sqlTime module so that the database can be updated
        checkTimer4 = 0 # resets the timer so it can be run again
    elif checkTimer4 == 0: # if the timer hasnt been running
        start4 = time.time() # starts the timer
        checkTimer4 = 1 # so it can stop the timer when run again

# Time Converter
def time_maker(seconds): 
    global timeactual
    minutes = seconds // 60 # Minutes are seconds divided by 60
    seconds = seconds % 60 # Seconds are seconds of a modulus of seconds
    hours = minutes // 60 # Hours are minutes divided by 60
    minutes = minutes % 60 # Minutes are minutes by a modulus of minutes
    timeactual = "{0}:{1}:{2}".format(int(hours), int(minutes), int(seconds)) # Formats the time so it is readable.

def sqlTime():
    cursor = cnx.cursor() # for being able to talk to the database
    roomstr  = str(room) # converts the room number to a string so it can be used in the query
    # the query needed to update the database with the correct variables
    query = "INSERT INTO `tbl_records` (`id_time`, `id_student`, `time_student`, `id_room`) VALUES (NULL, '" + value1 + "', '" + timeactual + "', '" + roomstr + "');"
    cursor.execute(query) # executes the query
    cnx.commit() # commits the changes to the database

# For running the correct code corresponding to the room when enter is pressed
def checkRoom(event): 
    if room == 1:
        roomOneOk()
    elif room == 2:
        roomTwoOk()
    elif room == 3:
        roomThreeOk()
    elif room == 4:
        roomFourOk()
    else:
        printCommand = "Non-Critical Error: Pressed enter too early."
        print(printCommand) # only happens if you press enter before pressing room button
        errors.configure(text=printCommand)
 
def sqlName():
    global studentName
    cursor = cnx.cursor()
    query = "SELECT `name_student` FROM tbl_students WHERE id_student = " + value1
    cursor.execute(query)
    studentName = cursor.fetchone()
    return studentName

def roomOne():  
    # these globals are for other modules to be able to use the variables
    global checkRoomOne
    global room
    global okButtonCheck1
    global value1
    global room1Student
    room = 1 # needed so checkroom code knows what to run
    # Resets the room and stops the timer
    if checkRoomOne == 1:
        room1Occupied.configure(text="Not Occupied")
        room1User.configure(text="No User")
        checkRoomOne = 0
        okButtonCheck1 = 0
        timer_room1()
        value1 = None
        room1Student = None
    # Launches the text entry.
    else:
        textEntry.pack()
        # validation to close the other buttons if they are showing
        if okButtonCheck2 or okButtonCheck3 or okButtonCheck4 == 1:
            okButtonTwo.pack_forget()
            okButtonThree.pack_forget()
            okButtonFour.pack_forget()
        okButtonOne.pack()
        okButtonCheck1 = 1
        textEntry.focus_set() # sets focus so you dont have to click on the text entry

 # Changes labels to match what is in the text entry, and starts the timer. Also closes the OK button and text entry button.
def roomOneOk():
    global checkRoomOne
    global value1
    global room1Student
    value1 = textEntry.get()
    # validates to see if the student trying to enter is already in another room
    if value1 == room2Student or room3Student or room4Student:
        printCommand = "Error: Student in another room already. Please log out of that room before continuing."
        print(printCommand)
        errors.configure(text=printCommand)
        textEntry.pack_forget()
        okButtonOne.pack_forget()
        textEntry.delete(0, 'end')
        return
    sqlName() # gets the name of the student from the database
    room1Occupied.configure(text="Currently Occupied")
    # if exit is typed, the program closes
    if value1 == 'exit':
        root.destroy()
    else:
        room1Student = value1
        room1User.configure(text=studentName)
        textEntry.pack_forget()
        okButtonOne.pack_forget()
        checkRoomOne = 1
        timer_room1()
        textEntry.delete(0, 'end')

# Second Room
def roomTwo():  
    # these globals are for other modules to be able to use the variables
    global checkRoomTwo
    global value1
    global room
    global okButtonCheck2
    global room2Student
    room = 2  # needed so checkroom code knows what to run
    # Resets the room and stops the timer
    if checkRoomTwo == 2:
        room2Occupied.configure(text="Not Occupied")
        room2User.configure(text="No User")
        checkRoomTwo = 0
        okButtonCheck2 = 0
        timer_room2()
        room2Student = None
    # Launches the text entry.
    else:
        textEntry.pack()
        # validation to close the other buttons if they are showing
        if okButtonCheck1 or okButtonCheck3 or okButtonCheck4 == 1:
            okButtonOne.pack_forget()
            okButtonThree.pack_forget()
            okButtonFour.pack_forget()
        okButtonTwo.pack()
        okButtonCheck2 = 1
        textEntry.focus_set()

 # Changes labels to match what is in the text entry, and starts the timer. Also closes the OK button and text entry button.
def roomTwoOk():
    global checkRoomTwo
    global value1
    global room2Student
    value1 = textEntry.get()
    # validates to see if the student trying to enter is already in another room
    if value1 == room1Student or room3Student or room4Student:
        printCommand = "Error: Student in another room already. Please log out of that room before continuing."
        print(printCommand)
        errors.configure(text=printCommand)
        textEntry.pack_forget()
        okButtonTwo.pack_forget()
        textEntry.delete(0, 'end')
        return
    sqlName() # gets the name of the student from the database
    room2Occupied.configure(text="Currently Occupied")
    room2User.configure(text=studentName)
    # if exit is typed the program closes
    if value1 == 'exit':
        root.destroy()
    else:
        room2Student = value1
        textEntry.pack_forget()
        okButtonTwo.pack_forget()
        checkRoomTwo = 2
        textEntry.delete(0, 'end')
        timer_room2()

# Third Room
def roomThree():  
    # these globals are for other modules to be able to use the variables
    global checkRoomThree
    global value1
    global room
    global okButtonCheck3
    global room3Student
    room = 3 # needed so checkroom code knows what to run
    # Resets the room and stops the timer
    if checkRoomThree == 3:
        room3Occupied.configure(text="Not Occupied")
        room3User.configure(text="No User")
        checkRoomThree = 0
        okButtonCheck3 = 0
        timer_room3()
        room3Student = None
    # Launches the text entry.
    else:
        textEntry.pack()
        # validation to close the other buttons if they are showing
        if okButtonCheck2 or okButtonCheck1 or okButtonCheck4 == 1:
            okButtonTwo.pack_forget()
            okButtonOne.pack_forget()
            okButtonFour.pack_forget()
        okButtonThree.pack()
        okButtonCheck3 = 1  
        textEntry.focus_set()

 # Changes labels to match what is in the text entry, and starts the timer. Also closes the OK button and text entry button.
def roomThreeOk():
    global checkRoomThree
    global value1
    global room3Student
    value1 = textEntry.get()
    # validates to see if the student trying to enter is already in another room
    if value1 == room1Student or room2Student or room4Student:
        printCommand = "Error: Student in another room already. Please log out of that room before continuing."
        print(printCommand)
        errors.configure(text=printCommand)
        textEntry.pack_forget()
        okButtonThree.pack_forget()
        textEntry.delete(0, 'end')
        return
    sqlName() # gets the name of the student from the database
    room3Occupied.configure(text="Currently Occupied")
    room3User.configure(text=studentName)
    # if exit is typed the program closes
    if value1 == 'exit':
        root.destroy()
    else:
        room3Student = value1
        textEntry.pack_forget()
        okButtonThree.pack_forget()
        checkRoomThree = 3
        textEntry.delete(0, 'end')
        timer_room3()

# Fourth Room
def roomFour():  
    # these globals are for other modules to be able to use the variables
    global checkRoomFour
    global value1
    global okButtonCheck4
    global room
    global room4Student
    room = 4 # needed so checkroom code knows what to run
    # Resets the room and stops the timer
    if checkRoomFour == 4:
        room4Occupied.configure(text="Not Occupied")
        room4User.configure(text="No User")
        checkRoomFour = 0
        okButtonCheck4 = 0
        timer_room4()
        room4Student = None
    # Launches the text entry.
    else:
        textEntry.pack()
        # validation to close the other buttons if they are showing
        if okButtonCheck2 or okButtonCheck3 or okButtonCheck4 == 1:
            okButtonTwo.pack_forget()
            okButtonThree.pack_forget()
            okButtonOne.pack_forget()
        okButtonFour.pack()
        okButtonCheck4 = 1
        textEntry.focus_set()

 # Changes labels to match what is in the text entry, and starts the timer. Also closes the OK button and text entry button.
def roomFourOk():
    global checkRoomFour
    global value1
    global room4Student
    value1 = textEntry.get()
    # validates to see if the student trying to enter is already in another room
    if value1 == room1Student or room2Student or room3Student:
        printCommand = "Error: Student in another room already. Please log out of that room before continuing."
        print(printCommand)
        errors.configure(text=printCommand)
        textEntry.pack_forget()
        okButtonFour.pack_forget()
        textEntry.delete(0, 'end')
        return
    sqlName() # gets the name of the student from the database
    room4Occupied.configure(text="Currently Occupied")
    room4User.configure(text=studentName)
    # if exit is typed the program closes
    if value1 == 'exit':
        root.destroy()
    else:
        room4Student = value1
        textEntry.pack_forget()
        okButtonFour.pack_forget()
        checkRoomFour = 4
        textEntry.delete(0, 'end')
        timer_room4()




# to be able to see the errors
errors = tk.Label(root)
errors.pack()

room1 = tk.Button(root, text="", command=roomOne)  # Runs the relevant code when clicking on room one.
room1.pack()

room1Occupied = tk.Label(root, text="Not Occupied")  # A label to show if room one is occupied
room1Occupied.pack()

room1User = tk.Label(root, text="No User")  # The current user of room one
room1User.pack()

room1Timer = tk.Label(root) # The timer for room one (only shows up after person exits)
room1Timer.pack()

room2 = tk.Button(root, text="", command=roomTwo)  # Runs the relevant code when clicking on room two
room2.pack()

room2Occupied = tk.Label(root, text="Not Occupied")  # A label to show if room two is occupied
room2Occupied.pack()

room2User = tk.Label(root, text="No User")  # The current user of room two
room2User.pack()

room2Timer = tk.Label(root) # The timer for room two (only shows up after person exits)
room2Timer.pack()

room3 = tk.Button(root, text="", command=roomThree)  # Runs the relevant code when clicking on room three
room3.pack()

room3Occupied = tk.Label(root, text="Not Occupied")  # A label to show if room three is occupied
room3Occupied.pack()

room3User = tk.Label(root, text="No User")  # The current user of room three
room3User.pack()

room3Timer = tk.Label(root) # The timer for room three (only shows up after person exits)
room3Timer.pack()

room4 = tk.Button(root, text="", command=roomFour)  # Runs the relevant code when clicking om room four
room4.pack()

room4Occupied = tk.Label(root, text="Not Occupied")  # A label to show if room four is occupied
room4Occupied.pack()

room4User = tk.Label(root, text="No User")  # The current user of room four
room4User.pack()

room4Timer = tk.Label(root) # The timer for room four (only shows up after person exits)
room4Timer.pack()

#Entry Box
textEntry = tk.Entry(root, text="Ref1")  # text entry
textEntry.pack()
root.bind('<Return>',checkRoom) # binds enter to running the code
textEntry.pack_forget()


# the following code is not relevant anymore due to pressing enter activating the room
okButtonOne = tk.Button(root, text="OK", command=roomOneOk) 
okButtonOne.pack()
okButtonOne.pack_forget()

okButtonTwo = tk.Button(root, text="OK", command=roomTwoOk)
okButtonTwo.pack()
okButtonTwo.pack_forget()

okButtonThree = tk.Button(root, text="OK", command=roomThreeOk)
okButtonThree.pack()
okButtonThree.pack_forget()

okButtonFour = tk.Button(root, text="OK", command=roomFourOk)
okButtonFour.pack()
okButtonFour.pack_forget()



#Configuration for Room buttons
room1.configure(width=60, height=9)#Room 1 Config
room1.config(bg='#ffc550',borderwidth=0)  

room2.configure(width=60, height=9)#room2 Config
room2.config(bg='#ffc550',borderwidth=0)

room3.configure(width=60, height=9)#Room 3 config
room3.config(bg='#ffc550',borderwidth=0)

room4.configure(width=60, height=9)#Room4 Config
room4.config(bg='#ffc550',borderwidth=0)

#Room Button Postitions
room1.place(x=50,y=75)
room2.place(x=800,y=75)
room3.place(x=50,y=535)
room4.place(x=800,y=535)


#Occupied/Not occupied label postions
room1Occupied.place(x=190,y=250)
room2Occupied.place(x=1000,y=250)
room3Occupied.place(x=190,y=400)
room4Occupied.place(x=1000,y=400)

#user labal positions
room1User.place(x=190,y=270)
room2User.place(x=1000,y=270)
room3User.place(x=190,y=420)
room4User.place(x=1000,y=420)

# closes the tkinter window when the button is pressed
exitButton = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack()

#exit button location and size
exitButton.configure(width=20,height=3)
exitButton.configure(bg='red')
exitButton.place(x=570,y=520)

root.geometry("1280x720")  # size of the tkinter window

root.mainloop()  # make so the window can recieve input from the user
