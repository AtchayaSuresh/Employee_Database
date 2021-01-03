from tkinter import *
from tkinter import messagebox
import os
from os import path
import json
class Signup:
    def __init__(self):
        self.root=Tk()
        self.root.title("Employee Database Management System")
        
        width= self.root.winfo_screenwidth()  
        height=self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 
        
        title=Label(self.root,text="Employee Database Management System",bd=10,pady=25,font=("times new roman",35,"bold")).pack(fill=X)

        self.userName=StringVar()
        self.password=StringVar()

        signupFrame=Frame(self.root,bd=10,relief=GROOVE)
        signupFrame.place(x=400,y=200,width=650,height=350)

        title=Label(signupFrame,text="Signup Page",font=("times new roman",30,"bold")).grid(row=0,column=0,pady=20,padx=20)
        
        username=Label(signupFrame,text="User Name",font=("times new roman",20,"bold")).grid(row=1,column=0,pady=10,padx=20)
        txtuser=Entry(signupFrame,bd=7,textvariable=self.userName,width=30,font='arial 15 bold').grid(row=1,column=1,padx=10,pady=10)

        Password=Label(signupFrame,text="Password",font=("times new roman",20,"bold")).grid(row=2,column=0,pady=10,padx=20)
        txtpassword=Entry(signupFrame,bd=7,width=30,textvariable=self.password,show='*',font='arial 15 bold').grid(row=2,column=1,padx=10,pady=10)

        buttonSignup=Button(signupFrame,text='Sign Up',bd=7,font='arial 15 bold',width=10,command=self.signup_action).place(x=125,y=250)
        buttonBack=Button(signupFrame,text='Back',bd=7,font='arial 15 bold',width=10,command=self.back_action).place(x=375,y=250)

        self.root.mainloop()

    def back_action(self):
        self.root.destroy()
        import login_page
        login_page.Login()
        
    def signup_action(self):
        if self.userName.get()=='':
            messagebox.showerror("Error","UserName is required")
        elif self.password.get()=='':
            messagebox.showerror("Error","Password is required")
        else:
            present='no'
            if path.exists("Login_Credential.txt"):
                with open("Login_Credential.txt") as json_file:
                    data = json.load(json_file)
                for i in data.keys():
                    if i==self.userName.get():
                        present='yes'
                        break
            else:
                data={}
            if present=='yes':
                messagebox.showerror("Error",f" UserName {self.userName.get()} already exists")
                self.userName.set("")
            else:
                data[self.userName.get()] = {
                    'password': self.password.get()
                }

                with open('Login_Credential.txt', 'w') as outfile:
                    json.dump(data, outfile)
                    
                messagebox.showinfo("Success","Signup successful")
                self.root.destroy()
                import login_page
                login_page.Login()

                        
