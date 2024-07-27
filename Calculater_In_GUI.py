from tkinter import *
import tkinter.messagebox as tmsg

root = Tk() # --> Creating the object of Tk 

def ClickButton(event): # --> Function that tell us all the functionality of all buttons
    global scvalue
    data = event.widget.cget("text") # --> Get Text 
    if data == "=": # --> Is press Equall that give the answer of equation after solving the equation
        if scvalue.get().isdigit(): # --> Get Digit only
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())  # --> Eval use to solve full algebraic expression like 2 * 5 = 10
            except Exception as e: # --> Check Error message
                tmsg.showerror("Error","Error Message")
                scvalue.set("Error")
        scvalue.set(value) # --> update the entry widget
        screen.update()             
    elif data == "C":
        scvalue.set("")  # --> clear the creen of calculators
        screen.update()
    else:
        scvalue.set(scvalue.get() +  data)

def DrawButtonOnGUI(FrameOne,listData): # --> Make All Button and write all the text
    for i in range(len(listData)):
        Btn = Button(FrameOne,text=listData[i],font="lucida 18 bold",padx=12,pady=10)
        Btn.pack(side=LEFT,padx=12,pady=2)
        Btn.bind("<Button-1>",ClickButton) # --> Handling event click button use there 
    FrameOne.pack()

root.geometry("644x900") # --> width and height
root.title("Calculator") # --> title
root.wm_iconbitmap("CalIcon.ico") # --> set Icon
Label(text="Calculator",font="ArielBlack,35,bold").pack()
scvalue = StringVar() # --> Varaiable 
scvalue.set("")

screen = Entry(root,textvariable=scvalue,font="lucida 20 bold") # --> Making Entry 
screen.pack(fill=X,ipadx=8,padx=12,pady=12)

# --> 👇👇👇 Making frame and calling button making function 

FraomeOne = Frame(root,bg="grey")
listNumber = ["0","1","2","3"]
listNumber2 = ["4","5","6","7"]
listNumber3 = ["8","9","10","C"]
operators = ["+","-","/","*","%","="]

DrawButtonOnGUI(FraomeOne,listNumber) 
FraomeOne = Frame(root,bg="grey")

DrawButtonOnGUI(FraomeOne,listNumber2) 
FraomeOne = Frame(root,bg="grey")

DrawButtonOnGUI(FraomeOne,listNumber3) 
FraomeOne = Frame(root,bg="grey")

DrawButtonOnGUI(FraomeOne,operators) 

root.mainloop()