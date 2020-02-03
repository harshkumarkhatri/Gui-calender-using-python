from tkinter import *
import calendar

#in it we have passed 2020 as we want the calender for the year 2020
text=calendar.calendar(2020)
#initializing the tkinter function
root=Tk()
#defining the size of window in which the calender will be displayed
root.geometry("500x600")
#giving it a title.
root.title("CALENDAR")
#writing the heading(calendar) in the window made above
label1=Label(root,text="CALENDAR",bg='dark gray',font=("times",28,"bold"))
#adding the title to the window we made
label1.grid(row=1,column=2)
#configuring th window to have a white color in the background.
root.config(background="white")
#providing the dates and the format in which they will be displayed.
#it is necessary to use the "Consolas" font else the orientation of the numbers will be incorrect
l1=Label(root,text=text,font="Consolas 10")
#adding the things to our window
l1.grid(row=2,column=2,padx=20)
#colsing the main loopf tkinter
root.mainloop()