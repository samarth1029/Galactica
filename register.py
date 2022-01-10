from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1230x590+0+0")
        self.root.wm_iconbitmap('face.ico')

        #Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confirmpass=StringVar()
        self.var_check=IntVar()

        img=Image.open(r"Images\dev.jpg")
        img=img.resize((1230,590),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        img1=Image.open(r"Images\kobe.jpg")
        img1=img1.resize((300,400),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        bg_img1=Label(self.root,image=self.photoimg1,bg='black')
        bg_img1.place(x=80,y=70,width=350,height=450)

        main_frame=Frame(self.root,bd=2,bg="lightblue")
        main_frame.place(x=430,y=75,width=700,height=450)

        main_label=Label(main_frame,text="REGISTER HERE",font=("times new roman",20),bd=2,bg="lightblue")
        main_label.place(x=10,y=20)

        username_lbl=Label(main_frame,text="First Name",font=("lucida handwriting",10,"bold"),bg='lightblue')
        username_lbl.place(x=20,y=90)
        self.studentuser_entry=ttk.Entry(main_frame,textvariable=self.var_fname,width=37,font=("times new roman",10,))
        self.studentuser_entry.place(x=20,y=110)

        contact_lbl=Label(main_frame,text="Contact No",font=("lucida handwriting",10,"bold"),bg='lightblue')
        contact_lbl.place(x=20,y=140)
        self.contact_entry=ttk.Entry(main_frame,textvariable=self.var_contact,width=37,font=("times new roman",10))
        self.contact_entry.place(x=20,y=160)

        search_label=Label(main_frame,text="Select Security Question",font=("lucida handwriting",10,"bold"),bg='lightblue')
        search_label.place(x=20,y=190)
        search_combo=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("times new roman",10),width=35,state="readonly")
        search_combo["values"]=("Select","Your birth place","Your girlfriend's name","Your pet's name")
        search_combo.current(0)
        search_combo.place(x=20,y=220)

        pass_lbl=Label(main_frame,text="Password",font=("lucida handwriting",10,"bold"),bg='lightblue')
        pass_lbl.place(x=20,y=250)
        self.pass_entry=ttk.Entry(main_frame,textvariable=self.var_pass,width=37,font=("times new roman",10),show='*')
        self.pass_entry.place(x=20,y=270)

        lname_lbl=Label(main_frame,text="Last Name",font=("lucida handwriting",10,"bold"),bg='lightblue')
        lname_lbl.place(x=350,y=90)
        self.luser_entry=ttk.Entry(main_frame,textvariable=self.var_lname,width=37,font=("times new roman",10,))
        self.luser_entry.place(x=350,y=110)

        email_lbl=Label(main_frame,text="Email",font=("lucida handwriting",10,"bold"),bg='lightblue')
        email_lbl.place(x=350,y=140)
        self.email_entry=ttk.Entry(main_frame,textvariable=self.var_email,width=37,font=("times new roman",10))
        self.email_entry.place(x=350,y=160)

        ans_lbl=Label(main_frame,text="Security Answer",font=("lucida handwriting",10,"bold"),bg='lightblue')
        ans_lbl.place(x=350,y=190)
        self.ans_entry=ttk.Entry(main_frame,textvariable=self.var_securityA,width=37,font=("times new roman",10))
        self.ans_entry.place(x=350,y=220)

        confirm_lbl=Label(main_frame,text="Confirm Password",font=("lucida handwriting",10,"bold"),bg='lightblue')
        confirm_lbl.place(x=350,y=250)
        self.contact_entry=ttk.Entry(main_frame,textvariable=self.var_confirmpass,width=37,font=("times new roman",10),show="*")
        self.contact_entry.place(x=350,y=270)

        checkbtn2=ttk.Checkbutton(main_frame,variable=self.var_check,offvalue=0,onvalue=1)
        checkbtn2.place(x=20,y=310)
        checkbtn2_label=Label(main_frame,text="I agree to the terms and conditions",font=("times new roman",12),bg="lightblue")
        checkbtn2_label.place(x=40,y=310)

        img2=Image.open(r"Images\reg.jpg")
        img2=img2.resize((150,30),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(main_frame,image=self.photoimg2,command=self.register,borderwidth=0,cursor="hand2",font=("times new roman",12),fg='lightblue')
        b1.place(x=40,y=350,width=150)

        img3=Image.open(r"Images\login.jpg")
        img3=img3.resize((150,30),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b3=Button(main_frame,image=self.photoimg3,borderwidth=0,cursor="hand2",command=self.return_login,font=("times new roman",12),fg='lightblue')
        b3.place(x=400,y=350,width=150)


    #Functions
    def register(self):
        if self.var_fname.get()=="" or self.var_pass.get()=="" or self.var_confirmpass.get()=="" or self.var_securityQ.get()=="Select" or self.var_securityA.get()=="":
            messagebox.showerror("Error","All fields are required.")
        elif self.var_pass.get()!=self.var_confirmpass.get():
            messagebox.showerror("Error","Passwords do not match.")
        elif self.var_check.get()!=1:
            messagebox.showerror("Error","Please agree to the terms and conditions.")
        else:
            connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
            my_cursor=connection.cursor()
            my_cursor.execute("select * from registration where email=%s",(self.var_email.get(),))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists. Please try another e-mail.")
            else:
                my_cursor.execute("Insert into registration values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                            self.var_fname.get(),
                                                                                            self.var_lname.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_contact.get(),
                                                                                            self.var_securityQ.get(),
                                                                                            self.var_securityA.get(),
                                                                                            self.var_pass.get() 
                                                                                            ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Success","User registration successful.")

    def return_login(self):
        self.root.destroy()




if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()