from textwrap import wrap

from tkinter import *

top = Tk()

#getting screen width and height of display
width= top.winfo_screenwidth() 
height= top.winfo_screenheight()
#setting tkinter window size
top.geometry("%dx%d" % (width, height))
top.title("BibleVerse")

LF = LabelFrame(top, text = "Welcome to BibleVerse!", font ="Courier 18 bold", labelanchor = N)
LF.pack(fill = "both", expand = "yes")

multiStr = ""

#-------------------------------------------------------------------------#
def displayText(line):
  
  label.configure(text=line)
  label.place(x = (width/2)-400, y = 400)
  
  B2 = Button(top, text="Remove Text", command= clearText)
  B2.place(x = (width/2)-150, y = 250)
#-------------------------------------------------------------------------#

def concatLine(line):
  global multiStr
  newStr = multiStr + line + "\n"
  multiStr = newStr
#-------------------------------------------------------------------------#
def clearText():
  global multiStr
  label.configure(text = "")
  multiStr = ""
#-------------------------------------------------------------------------#

#-------------------------------------------------------------------------#
def play():
  file = "Bible.txt"
  book = E1.get()
  chapter = E2.get()
  verse = E3.get()

  #--Condition flags--#
  #Verse was found
  foundFlag = 0
  #Stop reading lines from file
  stopFlag = 0
  #User requested multiple verses
  multiFlag = 0
  #Line number
  index = 0
  #Concatenate entries
  userInput = book + " " + chapter + ":" + verse

  bible = open(file, "r")

  #If the user wants multiple verses
  if "-" in verse:
    lhs, rhs = verse.split("-", 1)
    lhs = book + " " + chapter + ":" + lhs
    rhs = book + " " + chapter + ":" + rhs
    multiFlag = 1
  #If user only wants a single verse
  if multiFlag == 0:
    for line in bible:
      index += 1
      if userInput in line:
        foundFlag = 1
        break
    if foundFlag == 1:
      displayText(line)

  #If user wants multiple verses
  else:
    stopFlag = 1
    for line in bible:
      if stopFlag == 0:
        displayText(multiStr)
        break
      index += 1
      if lhs in line:
        foundFlag = 1
        concatLine(line)
        for line in bible:
          index += 1
          concatLine(line)
          if rhs in line:
            stopFlag = 0
            break
#------------------------------------------------------------#

#------------------------------------------------------------#
L1 = Label(top, text = "Enter a Book: ", font="Courier")
L1.place(x = (width/2)-200, y = 100)
E1 = Entry(top, bd = 5)
E1.place(x =  (width/2)+25 , y = 100)


L2 = Label(top, text = "Enter a Chapter: ", font="Courier")
L2.place(x = (width/2)-200, y = 150)
E2 = Entry(top, bd = 5)
E2.place(x =  (width/2)+25, y = 150)


L3 = Label(top, text = "Enter a Verse: ", font="Courier")
L3.place(x = (width/2)-200, y = 200)
E3 = Entry(top, bd = 5)
E3.place(x =  (width/2)+25, y = 200)


B1 = Button(top, text="Find", command= play)
B1.place(x =  (width/2)+25, y = 250)

label = Label(top, text="", font = ("Courier 12"), wraplength=1000, justify= LEFT)

top.mainloop()