from tkinter import *
from tkinter import messagebox
import os
from os import path
import json
class Read:
    def __init__(self):
        self.root=Tk()
        self.root.title("Show_Details")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 

        title=Label(self.root,text="View Employee Profile",bd=10,pady=25,font=("times new roman",35,"bold")).pack(fill=X)

        showFrame=Frame(self.root,bd=10,relief=GROOVE)
        showFrame.place(x=400,y=250,width=650,height=200)
        
        showTitle=Label(showFrame,text="View profile",font=("times new roman",25,"bold")).grid(row=0,column=0,pady=20,padx=30)

        self.showId=StringVar()
        
        eId=Label(showFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        IdDelete=Entry(showFrame,bd=7,width=25,textvariable=self.showId,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)

        buttonFrame=Frame(self.root,bd=10)
        buttonFrame.place(x=380,y=550)
        
        btnDelete=Button(buttonFrame,command=self.show_detail,text="Show Detail",font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=5,pady=20)
        btnBack=Button(buttonFrame,command=self.cancel,text="Back",font="arial 15 bold",bd=7,width=15).grid(row=0,column=1,padx=15,pady=20)
        btnNew=Button(buttonFrame,command=self.new_detail,text="View New Detail",font="arial 15 bold",bd=7,width=15).grid(row=0,column=2,padx=15,pady=20)

        self.root.mainloop()
        
    def new_detail(self):
        self.root.destroy()
        import show_details
        show_details.Read()
        
    def show_detail(self):
        if self.showId.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            if not path.exists("Employee_Details.txt"):
                messagebox.showerror("Error",f"Employee Id {self.showId.get()} not found")
                self.showId.set("")
            else:
                with open("Employee_Details.txt") as json_file:
                    data = json.load(json_file)
                    
                for i in data.keys():
                    if i==self.showId.get():
                        showFrame=Frame(self.root,bd=10,relief=GROOVE)
                        showFrame.place(x=400,y=200,width=650,height=350)
                        
                        eID=Label(showFrame,text="Employee Id",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=15,padx=20)
                        textID=Label(showFrame,text="%s"%(i),font=("times new roman",25,"bold")).grid(row=1,column=1,padx=20,pady=10)
                        
                        eName=Label(showFrame,text="Name",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
                        textContact=Label(showFrame,text="%s"%(data[i]['employeeName']),font=("times new roman",25,"bold")).grid(row=2,column=1,padx=20,pady=10)

                        eDOB=Label(showFrame,text="Date of Birth",font=("times new roman",25,"bold")).grid(row=3,column=0,pady=10,padx=20)
                        textName=Label(showFrame,text="%s"%(data[i]['employeeDOB']),font=("times new roman",25,"bold")).grid(row=3,column=1,padx=20,pady=10)

                        eDesignation=Label(showFrame,text="Designation",font=("times new roman",25,"bold")).grid(row=4,column=0,pady=10,padx=20)
                        textDOB=Label(showFrame,text="%s"%(data[i]['employeeDesignation']),font=("times new roman",25,"bold")).grid(row=4,column=1,padx=20,pady=10)

                        eDOJ=Label(showFrame,text="Date of Joining",font=("times new roman",25,"bold")).grid(row=5,column=0,pady=10,padx=20)
                        textDOB=Label(showFrame,text="%s"%(data[i]['employeeDOJ']),font=("times new roman",25,"bold")).grid(row=5,column=1,padx=20,pady=10)
                        break
                else:
                    messagebox.showerror("Error",f"Employee Id {self.showId.get()} not found")
                    self.showId.set("")
               
    def cancel(self):
        self.root.destroy()
        import main_page
        main_page.File_App()
