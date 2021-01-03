from tkinter import *
from tkinter import messagebox
import os
from os import path
import json

class Delete:
    def __init__(self):
        self.root=Tk()
        self.root.title("Delete")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height))

        title=Label(self.root,text="Delete Employee Profile",bd=10,pady=25,font=("times new roman",35,"bold")).pack(fill=X)

        deleteFrame=Frame(self.root,bd=10,relief=GROOVE)
        deleteFrame.place(x=400,y=250,width=650,height=200)

        deleteTitle=Label(deleteFrame,text="Delete profile",font=("times new roman",25,"bold")).grid(row=0,column=0,pady=20,padx=30)

        self.deleteID=StringVar()
        
        DeleteID=Label(deleteFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        IdDelete=Entry(deleteFrame,bd=7,width=25,textvariable=self.deleteID,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)

        buttonFrame=Frame(self.root,bd=10)
        buttonFrame.place(x=480,y=550)
        
        btnDelete=Button(buttonFrame,command=self.delete_detail,text="Delete",font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnCancel=Button(buttonFrame,command=self.cancel,text="Back",font="arial 15 bold",bd=7,width=15).grid(row=0,column=1,padx=30,pady=20)
        
    def cancel(self):
        self.root.destroy()
        import main_page
        main_page.File_App()
    
    def delete_detail(self):
        if self.deleteID.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            if not path.exists("Employee_Details.txt"):
                messagebox.showerror("Error",f"Employee Id {self.deleteID.get()} not found")
                self.deleteID.set("")
            else:
                with open("Employee_Details.txt") as json_file:
                    data = json.load(json_file)
                for i in data.keys():
                    if i==self.deleteID.get():
                        deleteFrame=Frame(self.root,bd=15,relief=GROOVE)
                        deleteFrame.place(x=400,y=200,width=650,height=350)
                  
                        eID=Label(deleteFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
                        textID=Label(deleteFrame,text="%s"%(i),font=("times new roman",25,"bold")).grid(row=1,column=1,padx=20,pady=10)
                        
                        eName=Label(deleteFrame,text="Name",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
                        textContact=Label(deleteFrame,text="%s"%(data[i]['employeeName']),font=("times new roman",25,"bold")).grid(row=2,column=1,padx=20,pady=10)

                        eDOB=Label(deleteFrame,text="Date of Birth",font=("times new roman",25,"bold")).grid(row=3,column=0,pady=10,padx=20)
                        textName=Label(deleteFrame,text="%s"%(data[i]['employeeDOB']),font=("times new roman",25,"bold")).grid(row=3,column=1,padx=20,pady=10)

                        eDesignation=Label(deleteFrame,text="Designation",font=("times new roman",25,"bold")).grid(row=4,column=0,pady=10,padx=20)
                        textDOB=Label(deleteFrame,text="%s"%(data[i]['employeeDesignation']),font=("times new roman",25,"bold")).grid(row=4,column=1,padx=20,pady=10)

                        eDOJ=Label(deleteFrame,text="Date of Joining",font=("times new roman",25,"bold")).grid(row=5,column=0,pady=10,padx=20)
                        textDOB=Label(deleteFrame,text="%s"%(data[i]['employeeDOJ']),font=("times new roman",25,"bold")).grid(row=5,column=1,padx=20,pady=10)

                        ask=messagebox.askyesno("Delete","Do you really want to delete "+self.deleteID.get()+"?")
                        if ask>0:
                            data.pop(self.deleteID.get())
                            with open('Employee_Details.txt', 'w') as outfile:
                                json.dump(data, outfile)
                                
                            messagebox.showinfo("Success",f"Employee Id {self.deleteID.get()} deleted Successfully")

                        self.root.destroy()
                        import delete_profile
                        delete_profile.Delete()
                        break
                else:
                    messagebox.showerror("Error",f"Employee Id {self.deleteID.get()} not found")
                    self.deleteID.set("")
