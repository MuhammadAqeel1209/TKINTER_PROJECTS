from tkinter import * # 👉 -->import the libraray
from PIL import Image, ImageTk # 👉 --> import the library for jpeg Images

def Final_Text_News(text): # 👈👈👈 Function use to jum the next line when one lines contain 100 characters
    final_text = ""
    for i in range(len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text        

root = Tk()

root.title("Welcome in Ary News") # 👉 --> Change the title
root.geometry("1000x1000") # 👉 --> set width and height of page
frameTitle = Frame(root,width=800,height=70,pady=30) # --> Frame of title and title images
TitleLabel = Label(frameTitle,text="Welcome in Ary News",font=("Algeraian",12,"bold")) #👉-->Text Label
TitleLabel.pack() #👉 -->write any thing in the form
Label(frameTitle,text="20 June 2023",font="lucida 13").pack()
frameTitle.pack() # --> Frame show in the form 

# --> 👇👇👇 Title Images 
TitlePic = Image.open("NewsPaper/AryNews.jpg")
picAry = ImageTk.PhotoImage(TitlePic)
Titlepiclabel = Label(frameTitle,image=picAry)
Titlepiclabel.pack()
Titlepiclabel.config(width=135,height=80)

"""make 2 list 
    1st list contain all text 
    2nd list contain all images"""
texts = []
images = []

# --> 👇👇👇 Loop for post all three news in paper 
for i in range(0, 3):
    with open(f"NewsPaper/{i+1}.txt") as f:
        text = f.read()
        texts.append(Final_Text_News(text))
    image = Image.open(f"NewsPaper/{i+1}.png")    
    #TODO: resize the images 
    image = image.resize((200,200),Image.ANTIALIAS)
    images.append(ImageTk.PhotoImage(image))

# --> 👇👇👇 First Frame for first news
FrameOne = Frame(root,width=900,height=200)
Label(FrameOne,text= texts[0],padx=22,pady=22).pack(side=LEFT)
Label(FrameOne,image=images[0],anchor="e").pack()
FrameOne.pack(anchor="w")

# --> 👇👇👇 Second Frame for Second news
FrameTwo = Frame(root,width=900,height=200,padx=100)
Label(FrameTwo,text= texts[1],padx=22,pady=22).pack(side=RIGHT)
Label(FrameTwo,image=images[1],anchor="e").pack()
FrameTwo.pack(anchor="w")

# --> 👇👇👇 Third Frame for Third news
FrameThree = Frame(root,width=900,height=200)
Label(FrameThree,text= texts[2],padx=22,pady=22).pack(side=LEFT)
Label(FrameThree,image=images[2],anchor="e").pack()
FrameThree.pack(anchor="w")

root.mainloop()  