from Tkinter import *
import tkMessageBox as tm
import os


    

def secondwindow():

    def returnbook():

        def savebook():
            n=namee.get()
            a=int(agee.get())
            
            w=open(("%s.dat"%n),"w")
            k=open(("%s.dat"%n),"r")
            print k.readline()
            m=k.readline()
            b=k.readline()
            w.write("NAME : %s \nAGE : %d "%(n,a))
            w.close()
            tm.showinfo("USER","Login Name : %s \nBook Returned : %s "%(n,b))
            print b
        
        root3=Tk()
        root3.title("ADD USER")
        root3.wm_iconbitmap('favicon.ico')
        root3.configure(bg="white")
        label=Label(root3,text="Enter User Details And The Book to Take",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)
        name=Label(root3,text="Enter Your Name : ",bg="white",height=2,justify="left")
        age=Label(root3,text="Enter Your Age : ",bg="white",height=2,justify="left")
        namee=Entry(root3)
        agee=Entry(root3)
        
       
        name.grid(row=3,column=1)
        age.grid(row=4,column=1)
        addb=Button(root3,text="Save ",command=savebook)
        namee.grid(row=3,column=2)
        agee.grid(row=4,column=2)
        
        addb.grid(row=6,column=1)
        
       
        root3.mainloop()
        
    

    def takebook():

        def savebook():
            n=namee.get()
            a=int(agee.get())
            b=booke.get()
            f=open(("%s.dat"%n),"w")
            f.write("NAME : %s \nAGE : %d \n Book Taken : %s"%(n,a,b))
            f.close()
            tm.showinfo("USER","Login Name : %s \nBook Taken : %s "%(n,b))

        def searchall():
            f=open("new.txt","r")
            l=f.readlines()
            for i in l:
                 print(i)
        
        root3=Tk()
        root3.title("ADD USER")
        root3.wm_iconbitmap('favicon.ico')
        root3.configure(bg="white")
        label=Label(root3,text="Enter User Details And The Book to Take",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)
        name=Label(root3,text="Enter Your Name : ",bg="white",height=2,justify="left")
        age=Label(root3,text="Enter Your Age : ",bg="white",height=2,justify="left")
        namee=Entry(root3)
        agee=Entry(root3)
        srcha=Button(root3,text="View All Books ",command=searchall)
        book=Label(root3,text="Enter the Name Of The Book : ",bg="White",height=2)
        booke=Entry(root3)
        name.grid(row=3,column=1)
        age.grid(row=4,column=1)
        addb=Button(root3,text="Save ",command=savebook)
        namee.grid(row=3,column=2)
        agee.grid(row=4,column=2)
        book.grid(row=5,column=1)
        booke.grid(row=5,column=2)
        addb.grid(row=6,column=1)
        srcha.grid(row=6,column=2)
       
        root3.mainloop()
        
    

    def booksearch():
        
        def searchall():
            
            f=open("new.txt","r")
            l=f.readlines()

            for i in l:
                 print(i)
        
        def search():
            v=str(labe.get())
            print v
            
            f=open("new.txt","r")
            l=f.readlines()
            
            for i in l:
                if (i==v):
                    print("man")
                    
                
                
               
           
        #
        root4=Tk()
        root4.title("SEARCH BOOK")
        root4.wm_iconbitmap('favicon.ico')
        root4.configure(bg="white")
        label=Label(root4,text="Enter The Name Of The Book To Search : ",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)
        lab=Label(root4,text="Enter the name  of the book : ",bg="white",height=2)
        labe=Entry(root4)
        srch=Button(root4,text="Search",command=search)
        srcha=Button(root4,text="View All Books ",command=searchall)
        lab.grid(row=3,column=1)
        labe.grid(row=3,column=2)
        srch.grid(row=6,column=1)
        srcha.grid(row=6,column=2)
        root4.mainloop()
        
    
    #view account
    def viewacc():

        def vacc():
            n=namee.get()
            try:
                f=open(("%s.dat"%n),"r")
                l=f.readline()
                m=f.readline()
                n=f.readline()
                label1.configure(text="%s"%l)
                label2.configure(text="%s"%m)
                label3.configure(text="%s"%n)
            except:
                tm.showerror("ERROR","Account Not Found")
        
        root4=Tk()
        root4.title("View USER")
        root4.wm_iconbitmap('favicon.ico')
        root4.configure(bg="white")
        label=Label(root4,text="Enter The User Details To View",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)
       
        label1=Label(root4,bg="white",font=('Helvetica',16))
        
        label2=Label(root4,bg="white",font=('Helvetica',16))
        label3=Label(root4,bg="white",font=('Helvetica',16))
        name=Label(root4,text="Enter The Login Name : ",bg="white",height=2,justify="left")
        namee=Entry(root4)
        name.grid(row=3,column=1)  
        addb=Button(root4,text="View",command=vacc)
        namee.grid(row=3,column=2)
        addb.grid(row=6,column=2)
        label1.grid(padx=180,pady=10,columnspan=4)
        label2.grid(padx=180,pady=10,columnspan=4)
        label3.grid(padx=180,pady=10,columnspan=4)
        root4.mainloop()
        
    
    #delete user
    def deluser():

        def savedel():
            n=namee.get()
            try:
                os.remove("%s.dat"%n)
                print"Account Removed"
                tm.showinfo("USER","Account Deleted \nLogin Name : %s \n DELETED!!"%n)
            except:
                print"Account Does Not Exist"
                tm.showerror("ERROR","Account Does Not Exist")
            
        
        root4=Tk()
        root4.title("DELETE USER")
        root4.wm_iconbitmap('favicon.ico')
        root4.configure(bg="white")
        label=Label(root4,text="Enter The User Details To Delete",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)

        name=Label(root4,text="Enter Your Name : ",bg="white",height=2,justify="left")
        age=Label(root4,text="Enter Your Age : ",bg="white",height=2,justify="left")
        namee=Entry(root4)
        agee=Entry(root4)
        
        name.grid(row=3,column=1)
        age.grid(row=4,column=1)
        addb=Button(root4,text="Delete",command=savedel)
        namee.grid(row=3,column=2)
        agee.grid(row=4,column=2)
        addb.grid(row=6,column=2)
        root4.mainloop()
    
        
    #add user
    def adduser():
        
        def saveadd():
            n=namee.get()
            a=int(agee.get())
            f=open(("%s.dat"%n),"w")
            f.write("NAME : %s \nAGE : %d "%(n,a))
            f.close()
            tm.showinfo("USER","Account Created \nLogin Name : %s"%n)
        
        root3=Tk()
        root3.title("ADD USER")
        root3.wm_iconbitmap('favicon.ico')
        root3.configure(bg="white")
        label=Label(root3,text="Enter User Details",bg="white",height=2,font=('Helvetica',16))
        label.grid(padx=180,pady=10,columnspan=4)
        name=Label(root3,text="Enter Your Name : ",bg="white",height=2,justify="left")
        age=Label(root3,text="Enter Your Age : ",bg="white",height=2,justify="left")
        namee=Entry(root3)
        agee=Entry(root3)
        
        name.grid(row=3,column=1)
        age.grid(row=4,column=1)
        addb=Button(root3,text="Save",command=saveadd)
        namee.grid(row=3,column=2)
        agee.grid(row=4,column=2)
        addb.grid(row=6,column=2)
       
        root3.mainloop()

    
    #
    root2=Tk()
    root2.title("ADMINISTRATION")
    root2.geometry("600x400")
    root2.wm_iconbitmap('favicon.ico')
    root2.configure(bg="white")
    label1=Label(root2,text="ADMIN SECTION",fg="black",bg="white",height=2,font=('Helvetica',16))
    label1.grid(padx=180,pady=10,columnspan=4)
     

    #menu
    mad2=Menu(root2)
    root2.config(menu=mad2,relief=SUNKEN)
    submenu2=Menu(mad2)

    mad2.add_cascade(label="File",menu=submenu2)
    submenu2.add_command(label="New")
    submenu2.add_command(label="Copy")
    submenu2.add_separator()
    submenu2.add_command(label="Exit")

    sub2=Menu(mad2)
    mad2.add_cascade(label="edit",menu=sub2)
    sub2.add_command(label="Undo")
    sub2.add_command(label="Redo")

    #buttons
    addu=Button(root2,text="Add User",command=adduser)
    delu=Button(root2,text="Delete User",command=deluser)
    viewa=Button(root2,text="View Account",command=viewacc)
    searchb=Button(root2,text="Search Book",command=booksearch)
    takeb=Button(root2,text="Take Book",command=takebook)
    returnb=Button(root2,text="Return Book",command=returnbook)
    addu.grid(row=2,column=2,pady=4)
    delu.grid(row=3,column=2,pady=4)
    viewa.grid(row=4,column=2,pady=4)
    searchb.grid(row=5,column=2,pady=4)
    takeb.grid(row=6,column=2,pady=4)
    returnb.grid(row=7,column=2,pady=4)

   
    root2.mainloop()
def mainwindow():        
    root=Tk()    

    def logincheck():
        a=userentry.get()
        p=passwentry.get()
        if (a=="admin" and p=="admin"):
             status.configure(text="Login success")
             print"yes"
             tm.showinfo("Login Success","Welcome Admin")
             root.destroy()
             secondwindow()
             
        else:
        
             status.configure(text="Login Failed !")
             print"no"
             tm.showerror("Login Error","Try Again!")
    
    #
    root.title("LIBRARY MANAGEMENT SYSTEM")
    root.geometry("600x400")
    root.wm_iconbitmap('favicon.ico')
    root.configure(bg="white")
    label1=Label(root,text="ADMINISTRATION LOGIN",fg="black",bg="white",height=2,font=('Helvetica',16))
    label1.grid(padx=180,pady=10,columnspan=4)

    #admin portal
    user=Label(root,text="Username : ",bg="white",height=6)
    passw=Label(root,text="Password : ",bg="white",height=3)
    userentry=Entry(root,text="Enter the username")
    passwentry=Entry(root,text="Enter the password",show="*")

    user.grid(row=9)
    passw.grid(row=12)
    userentry.grid(row=9,column=1)
    passwentry.grid(row=12,column=1)
    loginbut=Button(root,text="Login",command=logincheck)
    loginbut.grid(row=14,column=1)

    #menu
    mad=Menu(root)
    root.config(menu=mad,relief=SUNKEN)
    submenu=Menu(mad)

    mad.add_cascade(label="File",menu=submenu)
    submenu.add_command(label="New")
    submenu.add_command(label="Copy")
    submenu.add_separator()
    submenu.add_command(label="Exit")

    sub1=Menu(mad)
    mad.add_cascade(label="edit",menu=sub1)
    sub1.add_command(label="Undo")
    sub1.add_command(label="Redo")


    #statusbar
    status=Label(root,text="ready..",bg="white")
    status.grid(sticky=W,row=30,column=0)


    root.mainloop()
mainwindow()
# CREATED BY ( R4V3_V )
# COPYRIGHT 
