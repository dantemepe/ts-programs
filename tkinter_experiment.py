from tkinter import *
root = Tk()
# |  ### WINDOW PROPERTIES SECTION ###  | #
root.title(":P")
root.geometry("275x300")

# |  ### WIDGET PROPERTIES SECTION ###  | #
txt = Label(root, text = "Basic label") #root indicates where it is located and then goes the properties (this is a basic label)
txt.pack() #i think this makes the widget like appear and exist in a way so that its centered and blah blah blah but it incorporates it
btn = Button(root, text='Close window', width=25, command=root.destroy) #this is a basic button that destroys the windows so when its clicked it basically does something that is defifned within the command thing
btn.pack() # incorporates the button
ntry=Entry(root) #this lets you input text
ntry.pack() # incorporates the text entry
chkbtn = Checkbutton(root, text="check_button").pack()
v = IntVar()
Radiobutton(root, text="Radio1", variable=v, value=1).pack()
Radiobutton(root, text="Radio2", variable=v, value=2).pack()

mainloop()
root.mainloop()

