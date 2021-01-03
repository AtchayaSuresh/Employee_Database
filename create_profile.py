from tkinter import *
from tkinter import messagebox
import os
import json
from os import path

class Create:
    def __init__(self):
        self.root=Tk()
        self.root.title("Create Profile")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 

        title=Label(self.root,text="Create Employee Profile",bd=10,pady=25,font=("times new roman",35,"bold")).pack(fill=X)
        createFrame=Frame(self.root,bd=15)
        createFrame.place(x=250,y=100,height=800)
        
        employeeTitle=Label(createFrame,font=("times new roman",25,"bold")).grid(row=0,column=0,pady=20)

        self.employeeId=StringVar()
        self.employeeName=StringVar()
        self.employeeDOB=StringVar()
        self.employeeDesignation=StringVar()
        self.employeeDOJ=StringVar()
  
        eID=Label(createFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        textID=Entry(createFrame,bd=7,width=25,textvariable=self.employeeId,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
        
        eName=Label(createFrame,text="Name",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
        textContact=Entry(createFrame,bd=7,textvariable=self.employeeName,width=25,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

        eName=Label(createFrame,text="Date of Birth(dd/mm/yyyy)",font=("times new roman",25,"bold")).grid(row=3,column=0,pady=10,padx=20)
        textName=Entry(createFrame,bd=7,width=25,textvariable=self.employeeDOB,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)
        
        eDesignation=Label(createFrame,text="Designation",font=("times new roman",25,"bold")).grid(row=4,column=0,pady=10,padx=20)
        textDOB=Entry(createFrame,bd=7,width=25,textvariable=self.employeeDesignation,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

        eDOJ=Label(createFrame,text="Date of Joining(dd/mm/yyyy)",font=("times new roman",25,"bold")).grid(row=5,column=0,pady=10,padx=20)
        textDOB=Entry(createFrame,bd=7,width=25,textvariable=self.employeeDOJ,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

        btnCreate=Button(createFrame,text="Create Profile",command=self.save_data,font="arial 17 bold",bd=7,width=15).place(x=200,y=450)
        btnCancel=Button(createFrame,command=self.cancel,text="Back",font="arial 17 bold",bd=7,width=15).place(x=470,y=450)

        self.root.mainloop()
        
    def save_data(self):
        if self.employeeId.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            if self.employeeName.get()=='':
                messagebox.showerror("Error","Employee Name is required")
            else:
                if self.employeeDOB.get()=='':
                    messagebox.showerror("Error","Employee Date of Birth is required")
                else:
                    if self.employeeDesignation.get()=='':
                        messagebox.showerror("Error","Employee Desgination is required")
                    else:
                        if self.employeeDOJ.get()=='':
                            messagebox.showerror("Error","Employee Date of Joining is required")
                        else:
                            present='no'
                            if path.exists("Employee_Details.txt"):
                                with open("Employee_Details.txt") as json_file:
                                    data = json.load(json_file)
                                for i in data:
                                    if i==self.employeeId.get():
                                        present='yes'
                                        break
                            else:
                                data={}
                            if present=='yes':
                                messagebox.showerror("Error",f"Employee Id {self.employeeId.get()} already exists")
                                self.employeeId.set("")
                            else:
                                data[self.employeeId.get()] = {
                                        'employeeName': self.employeeName.get(),
                                        'employeeDOB': self.employeeDOB.get(),
                                        'employeeDesignation': self.employeeDesignation.get(),
                                        'employeeDOJ':self.employeeDOJ.get()
                                    }

                                with open('Employee_Details.txt', 'w') as outfile:
                                    json.dump(data, outfile)
                                        
                                messagebox.showinfo("Success","Record has been saved")
                                    
                                self.employeeId.set("")
                                self.employeeName.set("")
                                self.employeeDOB.set("")
                                self.employeeDesignation.set("")
                                self.employeeDOJ.set("")
                    
    def cancel(self):
        self.root.destroy()
        import main_page
        main_page.File_App()
