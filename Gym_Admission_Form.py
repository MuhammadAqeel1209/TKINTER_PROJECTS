from tkinter import *  # --> import for all basic tkinter
from tkinter import messagebox # --> Import to show message box
from tkinter import ttk # --> Import the combo box
import pyodbc # --> Import for connection with data base
import re # --> import the for rematch the pattren of gmail 

class GYM(Tk): # --> making class which inherit base class of tkinter
    def __init__(self): # --> Constructor
        super().__init__() # --> Base class constructor
        self.title("Gym Admmission Form") # --> Title Of Form
        width = 844
        height = 644
        self.geometry(f"{width}x{height}") # --> Set The Geometry 
        self.iconbitmap("Gym.ico") # --> Set The Icon

    # --> Connect to data base Function 👇👇👇
    def ConnectToDataBase(self):

        # -->👇👇👇 Syntax to connect the Python connect to sql server
        # --> conn_str = 'Driver={SQL Server};Server=your_server_name;Database=your_database_name;Trust_Connection = yes'
        
        # --> String Of connection 👇👇👇
        conn_str = 'Driver={SQL Server};Server=DESKTOP-FPO2BUS\SQLEXPRESS;Database=PYTHON;Trust_Connection = yes;'
        
        # -->Here Execption Handling to handle the error
        try:
            conn = pyodbc.connect(conn_str)
        except:
            messagebox.showerror("Error","Error in Connecting to Data Base") # --> Show Error message if not connect to data base
        else:
            cursor = conn.cursor()
            return cursor
        
        # --> Back to home page function by clicking button 👇👇👇
    def BackToPage(self,data):
                data.destroy()
                HomePage = GYM()
                HomePage.HomePage()

    # --> Home page of form  Start Here --> 👇👇👇 
    def HomePage(self):

        def on_combobox_selected(event): # --> Calling function to get value from event that created for gt value from combo box
            return cmbUser.get()
            
            # --> 👇👇👇 Label 
        Label(self,text="Gym Admission Form",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8,padx=50).grid(row=0,column=3,pady=20)
        Label(self,text="Home Page",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8,padx=25).grid(row=1,column=3,pady=25)
        Label(self,text="Enter the user choice",font="calibri 14",padx=10).grid(row=8,column=1,pady=22)
        
        user = ["New User of gym","Manager"] # --> Making list thet value show in combo box

        cmbUser = ttk.Combobox(self,values=user,width=20) # --> Making Combo box 
        cmbUser.current(0)
        cmbUser.grid(row=8,column=2,padx=12)
        # --> Bind is a function which use to create special event of tkinter application
        cmbUser.bind("<<ComboboxSelected>>", on_combobox_selected) # --> Create event to get value from combo box 
        
        def Choice(): # --> Get Choice for combo box in home page
            if(user[0] == on_combobox_selected(event=cmbUser)): # --> value = new user
                self.FormPage()  # --> Open Admission form page
            elif(user[1] == on_combobox_selected(event=cmbUser)): # --> value = manager 
                self.ManagerChecking() # --> Open Admin Page
            else:
                messagebox.showerror("Error","Plz Choice Correct User Types")    
        # --> Here Command --> Choice on home page
        Button(self,text="Next ",font="calibri 14 bold",command=Choice,width=12,bg="Red").grid(row=10,column=2,pady=20)
        Button(self,text="Exit ",font="calibri 14 bold",command=self.destroy,width=12,bg="Red").grid(row=10,column=3,pady=20)
        
    # --> Home page of form End Here --> 👆👆👆
    
    
    # --> Admin page of form  Start Here --> 👇👇👇 
    def ManagerChecking(self):

        self.destroy() # --> Home Page Close
        Manger = GYM() # --> Admin Page Open

        Label(Manger,text="Gym Admission Form",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8,padx=50).grid(row=0,column=5,pady=20)
        Label(Manger,text="Admin Page",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8,padx=20).grid(row=1,column=5,pady=25)
        
        def move_to_next(event): # --> We Click the "Enter" button to move next Entry in the form 
            event.widget.tk_focusNext().focus() 
        
        # --> Labels --> 👇👇👇
        Label(Manger,text="Name",font="calibri 14",padx=10).grid(row=3,column=3)
        Label(Manger,text="Password",font="calibri 14",padx=10).grid(row=4,column=3)
        
        # --> Varaible --> 👇👇👇
        nameVar = StringVar()
        PasswordVar = StringVar()

        # --> Entry --> 👇👇👇
        nameEntry = Entry(Manger,textvariable=nameVar,width=25)
        nameEntry.grid(row=3,column=4)
        nameEntry.bind("<Return>",move_to_next) # --> Create event to move one entry to other entry by clicking "enter" button
        nameEntry.focus_set() # --> set cursor at that entry 

        PasswordEntry = Entry(Manger,textvariable=PasswordVar,show="*",width=25)
        PasswordEntry.grid(row=4,column=4)

        # --> Search Page Open by clicking the button Next On Admin Page
        # --> Search page of form  Start Here --> 👇👇👇 
        def SearchDataInDB():
            Manger.destroy() # --> Admin Page Close
            SearchData = GYM() # --> Search Page Open

            # --> Label --> 👇👇👇
            Label(SearchData,text="Gym Admission Form",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8).grid(row=0,column=6,pady=20)
            Label(SearchData,text="Search page",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=8).grid(row=1,column=6,pady=25)


             # --> Data Display page of form  Start Here --> 👇👇👇 
            def Find(): 
                SearchData.destroy() # --> Search Page Close
                data = GYM() # --> Data Display Page Open

                cursor = data.ConnectToDataBase() # --> Return the connection 
                search_sql = """ 
                    SELECT * FROM RecordGYM
                    """   # --> Sql Command For Show all record
        
                # -->Here Execption Handling to handle the error        
                try:
                    cursor.execute(search_sql) # --> Here Show Command Execute
                    bar = Scrollbar(data,orient=VERTICAL)
                    bar.grid(row=3,column=5)
                    # --> Make The Column Heading 👇👇👇
                    cols = ("ID","Name","PhoneNo","Email","PassWordGYM" ,"Gender","Packages")
                    tree = ttk.Treeview(data,yscrollcommand=bar.set,show="headings",columns=cols) # --> Make a Table on GUI Page
                    bar.config(command=tree.yview)
                    style = ttk.Style(data) # --> Style the Heading
                    style.theme_use("clam") # --> Set THe Theme
                    

                    data.geometry("1000x500") # --> Set The Width and Height
                    tree.column("ID",width=30,anchor=CENTER) # --> Make the column 
                    tree.column("Name",width=70,anchor=CENTER) # --> Make the column
                    tree.column("PhoneNo",width=100,anchor=CENTER) # --> Make the column
                    tree.column("Email",width=180,anchor=CENTER) # --> Make the column
                    tree.column("PassWordGYM",width=100,anchor=CENTER) # --> Make the column
                    tree.column("Gender",width=70,anchor=CENTER) # --> Make the column
                    tree.column("Packages",width=300,anchor=CENTER) # --> Make the column

                    tree.heading("ID",text="ID",anchor=CENTER) # --> Make the heading text
                    tree.heading("Name",text="Name",anchor=CENTER) # --> Make the heading text
                    tree.heading("PhoneNo",text="PhoneNo",anchor=CENTER)# --> Make the heading text
                    tree.heading("Email",text="Email",anchor=CENTER) # --> Make the heading text
                    tree.heading("PassWordGYM",text="PassWordGYM",anchor=CENTER) # --> Make the heading text
                    tree.heading("Gender",text="Gender",anchor=CENTER) # --> Make the heading text
                    tree.heading("Packages",text="Packages",anchor=CENTER) # --> Make the heading text

                    for row in cursor: # --> Data Insert into the table for show the data
                        tree.insert("","end",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                    tree.grid(row=3,column=4) # --> adjust the tree on GUI Page
                    cursor.close() # --> Close the connection
                    Button(data,text="Back to Home Page",command=lambda:self.BackToPage(data),width=20,bg="Red",font="calibri 14 bold").grid(row=5,column=4,padx=10,pady=25)
                except EXCEPTION as e:
                    print(e.value)
                    messagebox.showwarning("Message","Error in Searching") 
                 # --> Data Display page of form  End Here --> 👆👆👆
                  
                # --> Here Command --> Find which Show the member of gym (home --> Admin --> Search --> Data Display)
            Button(SearchData,text="Search",command=Find,width=12,bg="Red",font="calibri 14 bold").grid(row=5,column=4,padx=35,pady=25)
            Button(SearchData,text="Back to home page",command=lambda:self.BackToPage(SearchData),width=20,bg="Red",font="calibri 14 bold").grid(row=5,column=5)
            # --> Search page of form  End Here --> 👆👆👆 

        def Check(): # --> Check Function --> use to check Manager User Name And Password --> Work the Function when click the next Button On Admin Page
            if(nameVar.get() == "Admin" and PasswordVar.get() == "12345"):
                SearchDataInDB() # --> Search Page open 
            else:
                messagebox.showinfo("Error","Plz enter the correct name and password")    
        
        # --> Here Command --> Check the password and user of admin (home --> Admin page)
        Button(Manger,text="Next",command=Check,width=12,bg="Red",font="calibri 14 bold").grid(row=6,column=3,padx=35,pady=25)
        Button(Manger,text="Back to Home Page",command=lambda:self.BackToPage(Manger),width=20,bg="Red",font="calibri 14 bold").grid(row=6,column=4)

        # --> Admin page of form  End Here --> 👆👆👆 
        
    # --> Adminssion form page of form Start Here --> 👇👇👇
    def FormPage(self):  
        self.destroy() # --> Home page Close
       
        # Start --> All Function Defination which use to in form 
        def SaveData(): # ==> 1
            Data = self.ConnectToDataBase() #--> Connection return
            Name = nameVar.get() # --> Get the Value from entry widget
            PhoneNo = phoneNo.get() # --> Get the Value from entry widget
            Email = email.get() # --> Get the Value from entry widget
            Password = password.get() # --> Get the Value from entry widget
            Gender = gender.get() # --> Get the Value from entry widget
            LbxValue = GetDataLBX() # --> Get the Value from List Box Function
            insertData = """
            INSERT INTO RecordGYM
            VALUES (?,?,?,?,?,?)
            """   # --> SQL data inser Statment
        
            # -->Here Execption Handling to handle the error
            try:
                Data.execute(insertData,Name,PhoneNo,Email,Password,Gender,LbxValue)
            except :

                # --> RollBack Function --> 👇👇👇
                # -->In pyodbc, the rollback() function is used to rollback a transaction
                #  in a database connection. It is typically used in error handling
                #  scenarios or when you want to cancel the changes made within
                #  a transaction and revert to the previous state.

                Data.rollback()
                messagebox.showerror("Error","Error for inserting data")
            else:

                # --> Commit Function --> 👇👇👇
                # In the context of pyodbc, the commit() function is used to permanently
                #  save any changes made to the database through a database connection. 
                # The commit() function is generally used in combination with data manipulation
                #  operations such as INSERT, UPDATE, or DELETE statements.

                Data.commit()
                messagebox.showinfo("Message","Data are inserted into DB")          
                Data.close()   #--> Close the function      

            SubmitForm() # --> Calling the submit form function 
        def EmailCheck(): # ==> 2 # --> Check the Email 
            if validate_email_format(email.get()): # --> Check Email Validate or Not 
                SaveData() # --> Save the data in data base
            else:
                messagebox.showerror("Message Box", "Invalid e mail format")# --> Show the message box when email is not valid
        def validate_email_format(email): # ==> 3 # --> Pattern of Email Check
            pattern = r"^\w+([\.-]?\w+)*@gmail\.com$" # --> This is Correct Format of Email 
            if re.match(pattern, email): # --> Check your email with the Correct Pattern 
                return True
            else:
                return False 

        def toggle_password_visibility():# ==> 5 # --> Visibility of Password 
            if show_password.get(): # --> Get The Password
                passwordEntry.config(show="") # --> Config the password --> Show the Password
            else:
                passwordEntry.config(show="*") # --> Config the password --> do not show  the Password          
        
        def SubmitForm(): # ==> 6 # --> Clear AnyThing When we enter the submit button 
            messagebox.showinfo("Message","Your Addmission in the Gym are Confrim")
            nameEntry.delete(0,END)
            phoneNoEntry.delete(0,END)
            phoneNoEntry.insert(0,"+92")
            emailEntry.delete(0,END)
            emailEntry.insert(0,"@gmail.com")
            passwordEntry.delete(0,END)

        def move_to_next(event): # ==> 7 # --> We Click the "Enter" button to move next Entry in the form 
            event.widget.tk_focusNext().focus()

        def DataInsert(listbox,list): # ==> 8 --> Dta insert into the list box
            for i in range(0,len(list)):
                listbox.insert(END,list[i])

        formPage = GYM() #--> Open the form page

        # --> 👇👇👇 Label 
        Label(formPage,text="Gym Admission Form",font="Algerian 15 bold",bg="Blue",relief=SUNKEN,pady=12,padx=50).grid(row=0,column=4,pady=12)
        

        # --> 👇👇👇 All Labels of Form and Grid is used to show data on the form 
        Label(formPage,text="Name",font="calibri 14",padx=10).grid(row=1,column=3,pady=5)
        Label(formPage,text="Phone No",font="calibri 14",padx=10).grid(row=2,column=3)
        Label(formPage,text="Email",font="calibri 14",padx=10).grid(row=3,column=3)
        Label(formPage,text="Password",font="calibri 14",padx=10).grid(row=4,column=3)
        Label(formPage,text="Gender",font="calibri 14",padx=10).grid(row=5,column=3)
        Label(formPage,text="Package",font="calibri 14",padx=10).grid(row=6,column=3)

        # --> 👇👇👇 Making the Varaible of All Label4
        nameVar = StringVar()
        phoneNo = StringVar()
        email = StringVar()
        password = StringVar()
        gender = StringVar()
        show_password = BooleanVar()


        # --> 👇👇👇 Making the Entry of All Labels and Grid is used to show data on the form 
        nameEntry = Entry(formPage,textvariable=nameVar,width=25)
        nameEntry.grid(row=1,column=4)
        nameEntry.bind("<Return>",move_to_next) # --> Create event to move one entry to other entry by clicking "enter" button
        nameEntry.focus_set()

        

        phoneNoEntry = Entry(formPage,textvariable=phoneNo,width=25)
        phoneNoEntry.grid(row=2,column=4)
        phoneNoEntry.insert(0,"+92")
        phoneNoEntry.bind("<Return>", move_to_next)  # --> Create event to move one entry to other entry by clicking "enter" button

        emailEntry = Entry(formPage,textvariable=email,width=25)
        emailEntry.insert(0, "@gmail.com")
        emailEntry.grid(row=3,column=4)
        emailEntry.bind("<Return>", move_to_next)  # --> Create event to move one entry to other entry by clicking "enter" button

        passwordEntry = Entry(formPage,textvariable=password,show="*",width=25)
        passwordEntry.grid(row=4,column=4)
        passwordEntry.bind("<Return>", move_to_next)  # --> Create event to move one entry to other entry by clicking "enter" button
        # --> 👇👇👇 Making The Check Button To show the Password 
        show_password_CheckButton = Checkbutton(formPage,text="👁",variable=show_password,command=toggle_password_visibility)
        show_password_CheckButton.grid(row=4,column=5)

        # --> 👇👇👇 Radio Button For Selection the Gender
        RadiobuttonMale = Radiobutton(formPage,text="Male",variable=gender,value="Male")
        RadiobuttonFemale = Radiobutton(formPage,text="Female",variable=gender,value="Female")
        RadiobuttonOther = Radiobutton(formPage,text="Other",variable=gender,value="Other")
        RadiobuttonMale.grid(row=5,column=4)
        RadiobuttonFemale.grid(row=5,column=5)
        RadiobuttonOther.grid(row=5,column=6)

        bar = Scrollbar(formPage,orient=HORIZONTAL)
        bar.grid(row=6, column=4, sticky="nsew")
        lbx = Listbox(formPage,xscrollcommand=bar.set)
        lbx.grid(row=7,column=4,sticky="nsew")
        listGym = ["Exercise Full With Out Trainer 2200 Rs",
                   "Exercise Full With Trainer 3000 Rs",
                   "Exercise Day By Day Fees  80 Rs",
                   "Membership Card Advance 2 Month Fees 4000 Rs"]
        DataInsert(lbx,listGym)
        bar.config(command=lbx.xview)

        def GetDataLBX(): # ==> 9 --> Get Value from List Box
            index = lbx.curselection()
            return lbx.get(index)

        # --> 👇👇👇 Making Button to Submit the data 

        # --> Here Command --> Check the Email amd Checking other command on the Form Page 
        submitBtn = Button(formPage,text="Submit Record",command=EmailCheck,width=12,bg="Red",font="calibri 14 bold")
        submitBtn.grid(row=10,column=4,pady=15)
        Button(formPage,text="Back To Home Page",command=lambda:self.BackToPage(formPage),width=20,bg="Red",font="calibri 14 bold").grid(row=10,column=6)


form = GYM() # --> Make the object
form.HomePage() # --> calling the Home Page

form.mainloop()

# Important Note 
      # --> 👇👇👇 Use Of Config Function 
"""use of configure() in tkinter python? config or configure is
        used to access an object's attributes after its initialisation. 
        For example, here, you define l = Label(root, bg="ivory", fg="darkgreen")
          but then you want to set its text attribute, so you use config: l.
            config(text="Correct answer!")"""
 