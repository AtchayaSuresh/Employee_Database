from tkinter import *
from tkinter import messagebox
import os
class Delete:
    def __init__(self):
        self.root=Tk()
        self.root.title("Delete")
        
        width= self.root.winfo_screenwidth()  
        height= self.root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height))

        title=Label(self.root,text="Delete Employee Profile",bd=10,pady=15,font=("times new roman",35,"bold")).pack(fill=X)

        deleteFrame=Frame(self.root,bd=15)
        deleteFrame.place(x=20,y=100,height=400)

        self.deleteID=StringVar()
        
        DeleteID=Label(deleteFrame,text="Employee ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        IdDelete=Entry(deleteFrame,bd=7,width=25,textvariable=self.deleteID,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)

        buttonFrame=Frame(self.root,bd=10)
        buttonFrame.place(x=200,y=600)
        
        btnDelete=Button(buttonFrame,command=self.delete_detail,text="Delete",font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnCancel=Button(buttonFrame,command=self.cancel,text="Cancel",font="arial 15 bold",bd=7,width=15).grid(row=0,column=3,padx=20,pady=20)
        
    def cancel(self):
        self.root.destroy()
        import main_page
    
    def delete_detail(self):
        present='no'
        if self.deleteID.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.deleteID.get():
                        present='yes'
            if present=='no':
                messagebox.showerror("Error","Employee ID not found")
            else:
                f1=open("files/"+self.deleteID.get()+'.txt')
                value=[]
                for f in f1:
                    value=f.split(",")

                deleteFrame=Frame(self.root,bd=15)
                deleteFrame.place(x=20,y=100,height=400)
                
                self.deleteID.set(value[0])
                self.employeeName=StringVar()
                self.employeeDOB=StringVar()
                self.employeeDesignation=StringVar()
                self.employeeDOJ=StringVar()
          
                eID=Label(deleteFrame,text="Student ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
                textID=Entry(deleteFrame,bd=7,width=25,textvariable=self.deleteID,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
                
                eName=Label(deleteFrame,text="Contact",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
                textContact=Entry(deleteFrame,bd=7,textvariable=self.employeeName,width=25,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

                eDOB=Label(deleteFrame,text="Name",font=("times new roman",25,"bold")).grid(row=3,column=0,pady=10,padx=20)
                textName=Entry(deleteFrame,bd=7,width=25,textvariable=self.employeeDOB,font="arial 15 bold").grid(row=3,column=1,padx=20,pady=10)

                eDesignation=Label(deleteFrame,text="DOB(dd/mm/yyyy)",font=("times new roman",25,"bold")).grid(row=4,column=0,pady=10,padx=20)
                textDOB=Entry(deleteFrame,bd=7,width=25,textvariable=self.employeeDesignation,font="arial 15 bold").grid(row=4,column=1,padx=20,pady=10)

                eDOJ=Label(deleteFrame,text="DOB(dd/mm/yyyy)",font=("times new roman",25,"bold")).grid(row=5,column=0,pady=10,padx=20)
                textDOB=Entry(deleteFrame,bd=7,width=25,textvariable=self.employeeDOJ,font="arial 15 bold").grid(row=5,column=1,padx=20,pady=10)

                self.employeeName.set(value[1])
                self.employeeDOB.set(value[2])
                self.employeeDesignation.set(value[3])
                self.employeeDOJ.set(value[4])
                
                f1.close()
                ask=messagebox.askyesno("Delete","Do you really want to delete "+self.deleteID.get()+"?")
                if ask>0:
                    os.remove("files/"+self.deleteID.get()+".txt")
                    messagebox.showinfo("Success","Deleted Successfully")

                self.root.destroy()
                import main_page
