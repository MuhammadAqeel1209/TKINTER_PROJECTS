from tkinter import *
from tkinter import messagebox 
from PIL import Image, ImageTk 
from plyer import notification

root = Tk()
root.title("Notification App")
root.geometry("1200x900")
root.iconbitmap("Notify.ico")

def Detail():
    title_get = titleEntry.get()
    msg_get = msgEntry.get()
    time_get = timeEntry.get()
    if title_get == "" or msg_get == "" or time_get == "":
        messagebox.showwarning("Alert","All Field required")
    else:
        messagebox.showinfo("notifier set","Notification Set")
    titleEntry.delete(0,END)
    msgEntry.delete(0,END)
    timeEntry.delete(0,END)
    notification.notify(
            title = title_get,
            message = msg_get,
            app_icon = "Notify.ico",
            timeout = time_get
        )

titleImg = ImageTk.PhotoImage(Image.open("Notification.jpg"))
Label(image=titleImg,height=80,width=70).grid(row=2,column=2,padx=40,pady=20)

Label(text="Notification App For Desktop",font= "Algerian 30 bold").grid(row=2,column=3,padx=40)


Label(root,text="Title To Notify",font="calibri 14",pady=30).grid(row=5,column=2,padx=20)

titleEntry = Entry(root,width=25)
titleEntry.grid(row=5,column=3)
Label(root,text="Message",font="calibri 14",pady=30).grid(row=6,column=2,padx=20)

msgEntry = Entry(root,width=60)
msgEntry.grid(row=6,column=3)

Label(root,text="Time",font="calibri 14",pady=30).grid(row=7,column=2,padx=20)

timeEntry = Entry(root,width=25)
timeEntry.grid(row=7,column=3)

btn = Button(text="Set Notofication",font="calibri 14",bg="Blue",command=Detail).grid(row=9,column=3)

root.mainloop()