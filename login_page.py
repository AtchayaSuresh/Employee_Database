from tkinter import *
from tkinter import messagebox
from os import path
import json
import os
class Login:
    def __init__(self):
        self.root=Tk()
        self.root.title("Employee Database Management System")
        
        width=self.root.winfo_screenwidth()  
        height=self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 
        
        title=Label(self.root,text="Employee Database Management System",bd=10,pady=25,font=("times new roman",35,"bold")).pack(fill=X)

        self.userName=StringVar()
        self.password=StringVar()

        loginFrame=Frame(self.root,bd=10,relief=GROOVE)
        loginFrame.place(x=400,y=200,width=650,height=350)

        title=Label(loginFrame,text="Login Page",font=("times new roman",30,"bold")).grid(row=0,column=0,pady=20,padx=20)
        
        username=Label(loginFrame,text="User Name",font=("times new roman",20,"bold")).grid(row=1,column=0,pady=10,padx=20)
        txtuser=Entry(loginFrame,bd=7,textvariable=self.userName,width=30,font='arial 15 bold').grid(row=1,column=1,padx=10,pady=10)

        Password=Label(loginFrame,text="Password",font=("times new roman",20,"bold")).grid(row=2,column=0,pady=10,padx=20)
        txtpassword=Entry(loginFrame,bd=7,width=30,textvariable=self.password,show='*',font='arial 15 bold').grid(row=2,column=1,padx=10,pady=10)

        buttonlogin=Button(loginFrame,text='Login',bd=7,font='arial 15 bold',width=10,command=self.login_action).place(x=10,y=250)
        buttonsignup=Button(loginFrame,text='Sign up',bd=7,font='arial 15 bold',width=10,command=self.sign_up).place(x=160,y=250)
        buttonreset=Button(loginFrame,text='Reset',bd=7,font='arial 15 bold',width=10,command=self.reset_function).place(x=310,y=250)
        buttonexit=Button(loginFrame,text='Exit',bd=7,font='arial 15 bold',width=10,command=self.exit_function).place(x=460,y=250)

        self.root.mainloop()

    def login_action(self):
        if self.userName.get()=='':
            messagebox.showerror("Error","User Name is required")
        elif self.password.get()=='':
            messagebox.showerror("Error","Password is required")
        else:
            if not path.exists("Login_Credential.txt"):
                messagebox.showerror("Error","Invalid User Name or Password")
            else:
                with open("Login_Credential.txt") as json_file:
                    data = json.load(json_file)
                for i in data.keys():
                    if i==self.userName.get():
                        if data[i]['password']==self.password.get():
                            messagebox.showinfo("Info",f"Welcome {self.userName.get()}")
                            self.root.destroy()
                            import main_page
                            main_page.File_App()
                        else:
                            messagebox.showerror("Error","Invalid User Name or Password ")
                        break
                else:
                    messagebox.showerror("Error","Invalid User Name or Password")
                    
    def reset_function(self):
        self.userName.set("")
        self.password.set("")

    def exit_function(self):
        option=messagebox.askyesno("Exit","Do you really want to exit")
        if option>0:
            self.root.destroy()

    def sign_up(self):
        self.root.destroy()
        import signup_page
        signup_page.Signup()

                       
