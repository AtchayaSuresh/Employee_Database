from tkinter import *
from tkinter import messagebox
import os
class Read:
    def __init__(self):
        self.root=Tk()
        self.root.title("Show_Details")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 

        title=Label(self.root,text="View Student Profile",bd=10,pady=15,font=("times new roman",35,"bold")).pack(fill=X)
        showFrame=Frame(self.root,bd=15)
        showFrame.place(x=20,y=100,height=400)
        
        studentTitle=Label(showFrame,font=("times new roman",25,"bold")).grid(row=0,column=0,pady=20)

        self.showId=StringVar()
        
        eId=Label(showFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        IdDelete=Entry(showFrame,bd=7,width=25,textvariable=self.showId,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)

        buttonFrame=Frame(self.root,bd=10)
        buttonFrame.place(x=200,y=600)
        
        btnDelete=Button(buttonFrame,command=self.show_detail,text="Show Detail",font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnCancel=Button(buttonFrame,command=self.cancel,text="Back",font="arial 15 bold",bd=7,width=15).grid(row=0,column=3,padx=20,pady=20)

    def show_detail(self):
        present='no'
        if self.showId.get()=='':
            messagebox.showerror("Error","Student ID is required %s ")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.showId.get():
                        present='yes'
            if present=='no':
                messagebox.showerror("Error","File not found")
            else:
                f1=open("files/"+self.showId.get()+'.txt')
                value=[]
                for f in f1:
                    value=f.split(",")

                showFrame=Frame(self.root,bd=15)
                showFrame.place(x=20,y=100,height=400)
                
                self.showId.set(value[0])
                self.employeeName=StringVar()
                self.employeeDOB=StringVar()
                self.employeeDesignation=StringVar()
                self.employeeDOJ=StringVar()
          
                eID=Label(showFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
                textID=Entry(showFrame,bd=7,width=25,textvariable=self.showId,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
                
                eName=Label(showFrame,text="Name",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
                textContact=Entry(showFrame,bd=7,textvariable=self.employeeName,width=25,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

                eDOB=Label(showFrame,text="Date of Birth",font=("times new roman",25,"bold")).grid(row=3,column=0,pady=10,padx=20)
                textName=Entry(showFrame,bd=7,width=25,textvariable=self.employeeDOB,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)

                eDesignation=Label(showFrame,text="Designation",font=("times new roman",25,"bold")).grid(row=4,column=0,pady=10,padx=20)
                textDOB=Entry(showFrame,bd=7,width=25,textvariable=self.employeeDesignation,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

                eDOJ=Label(showFrame,text="Date of Joining",font=("times new roman",25,"bold")).grid(row=5,column=0,pady=10,padx=20)
                textDOB=Entry(showFrame,bd=7,width=25,textvariable=self.employeeDOJ,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

                self.employeeName.set(value[1])
                self.employeeDOB.set(value[2])
                self.employeeDesignation.set(value[3])
                self.employeeDOJ.set(value[4])
                
                f1.close()
                self.root.mainloop()
    def cancel(self):
        self.root.destroy()
        import main_page
