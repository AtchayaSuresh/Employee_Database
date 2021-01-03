from tkinter import *
from tkinter import messagebox
import time
import os
class File_App:
    def __init__(self):
        self.root=Tk()
        self.root.title("Employee Database Management System")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 
        
        title=Label(self.root,text="Employee Database Management System",bd=10,pady=25,font=("times new roman",40,"bold")).pack(fill=X)
        
        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=450,y=150,width=650,height=500)

        btnCreate=Button(btnFrame,text="Create",command=self.save_data,font="arial 23 bold",bd=7,width=15).place(x=150,y=40)
        btnRead=Button(btnFrame,command=self.get_data,text="Show Details",font="arial 23 bold",bd=7,width=15).place(x=150,y=145)
        btnDelete=Button(btnFrame,command=self.delete,text="Delete",font="arial 23 bold",bd=7,width=15).place(x=150,y=250)
        btnLogout=Button(btnFrame,command=self.logout,text="Logout",font="arial 23 bold",bd=7,width=15).place(x=150,y=355)

        self.root.mainloop()

    def save_data(self):
        self.root.destroy()
        import create_profile
        create_profile.Create()
            
    def get_data(self):
        self.root.destroy()
        import show_details
        show_details.Read()

    def delete(self):
        self.root.destroy()
        import delete_profile
        delete_profile.Delete()

    def logout(self):
        self.root.destroy()
        import login_page
        login_page.Login()
