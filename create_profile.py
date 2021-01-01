from tkinter import *
from tkinter import messagebox
import os
class Create:
    def __init__(self):
        self.root=Tk()
        self.root.title("Create")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 

        title=Label(self.root,text="Create Employee Profile",bd=10,pady=15,font=("times new roman",35,"bold")).pack(fill=X)
        createFrame=Frame(self.root,bd=15)
        createFrame.place(x=20,y=100,height=400)
        
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

        btnFrame=Frame(self.root,bd=10)
        btnFrame.place(x=10,y=600)

        btnCreate=Button(btnFrame,text="Create Profile",command=self.save_data,font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnCancel=Button(btnFrame,command=self.cancel,text="Back",font="arial 15 bold",bd=7,width=15).grid(row=0,column=3,padx=20,pady=20)

        self.root.mainloop()
    def save_data(self):
         if self.employeeId.get()=='':
            messagebox.showerror("Error","Employee ID is required")
         else:
            present='no'
            f=os.listdir("files/")
            for i in f:
                    if i.split(".")[0]==self.employeeId.get():
                        present='yes'
            if present=='yes':
                messagebox.showerror("Error","Employee Id already exists")
            else:
                f=open("files/"+self.employeeId.get()+".txt","w")
                f.write(str(self.employeeId.get())+","+
                        str(self.employeeName.get())+","+
                        str(self.employeeDOB.get())+","+
                        str(self.employeeDesignation.get())+","+
                        str(self.employeeDOJ.get())
                        )
                f.close()
                messagebox.showinfo("Success","Record has been saved")
    def cancel(self):
        self.root.destroy()
        import main_page
