from tkinter import *
from tkinter import messagebox
import time
import os
class File_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database Management System")
        
        width= root.winfo_screenwidth()  
        height= root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 
        
        title=Label(self.root,text="Employee Database Management System",bd=10,pady=15,font=("times new roman",35,"bold")).pack(fill=X)
        
        btnFrame=Frame(self.root,bd=10)
        btnFrame.place(x=200,y=600)

        btnCreate=Button(btnFrame,text="Create",command=self.save_data,font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnRead=Button(btnFrame,command=self.get_data,text="Show Details",font="arial 15 bold",bd=7,width=15).grid(row=0,column=3,padx=20,pady=20)
        btnDelete=Button(btnFrame,command=self.delete,text="Delete",font="arial 15 bold",bd=7,width=15).grid(row=0,column=5,padx=20,pady=20)

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
                    
    
root=Tk()
ob=File_App(root)
root.mainloop()
                                                                              
