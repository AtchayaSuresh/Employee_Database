from tkinter import *
class Display:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Database Management System")
        
        width= root.winfo_screenwidth()  
        height= root.winfo_screenheight() 
        self.root.geometry("%dx%d" % (width, height)) 

        displayFrame=Frame(self.root,bd=10)
        displayFrame.place(x=150,y=200,height=500)

        title=Label(displayFrame,text="Employee Database Management System",font=("times new roman",50,"bold")).grid(row=0,column=0,pady=20,padx=20)
        author=Label(displayFrame,text="By Atchaya Suresh",font=("times new roman",50,"bold")).grid(row=1,column=0,pady=20,padx=20)

        buttonlogin=Button(displayFrame,text='Get Details',bd=7,font='arial 25 bold',width=17,command=self.login_action).place(x=400,y=280)

    def login_action(self):
        self.root.destroy()
        import login_page
        login_page.Login()


root=Tk()
ob=Display(root)
root.mainloop()
                       
