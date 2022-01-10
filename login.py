from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
from register import Register
from main import Face_Recognition_System


class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1230x590+0+0")
        self.root.wm_iconbitmap('face.ico')

        self.txtuser=StringVar()
        self.txtpass=StringVar()
        self.combo_securityQ=StringVar()
        self.combo_securityA=StringVar()
        self.new_pass=StringVar()


        img=Image.open(r"Images\dev.jpg")
        img=img.resize((1230,590),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)


        self.root2=Frame(self.root,bd=2,bg="black")
        self.root2.place(x=484,y=115,width=270,height=332)

        img1=Image.open(r"Images\user-modified.png")
        img1=img1.resize((79,74),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1,bg='black',borderwidth=0)
        f_lbl.place(x=579,y=125,width=79,height=74)

        get_str=Label(self.root2,text="Get Started",font=("lucida handwriting",12,"bold"),fg='white',bg="black")
        get_str.place(x=80,y=85)

        username_lbl=Label(self.root2,text="Username",font=("lucida handwriting",10),fg='white',bg="black")
        username_lbl.place(x=20,y=125)

        self.studentuser_entry=ttk.Entry(self.root2,textvariable=self.txtuser,width=37,font=("times new roman",10))
        self.studentuser_entry.place(x=20,y=145)

        pass_lbl=Label(self.root2,text="Password",font=("lucida handwriting",10),fg='white',bg="black")
        pass_lbl.place(x=20,y=175)

        self.pass_entry=ttk.Entry(self.root2,textvariable=self.txtpass,width=37,font=("times new roman",10),show='*')
        self.pass_entry.place(x=20,y=195)

        login_btn=Button(self.root2,text="Login",command=self.login,width=14,font=("times new roman",13),bg="red",fg="white",activeforeground='white',activebackground='red')
        login_btn.place(x=70,y=230)

        signup_btn=Button(self.root2,text="Sign Up",command=self.register_window,borderwidth=0,font=("times new roman",10),bg="black",fg="lightgreen",activeforeground='white',activebackground='black')
        signup_btn.place(x=65,y=280)

        login_btn=Button(self.root2,text="Forgot Password",command=self.forgot_pass,borderwidth=0,font=("times new roman",10),bg="black",fg="lightblue",activeforeground='white',activebackground='black')
        login_btn.place(x=113,y=280)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def reset(self):
        if self.combo_securityQ.get()=="Select":
            messagebox.showerror("Error","Select a security question.",parent=self.root2)
        elif self.combo_securityA.get()=="":
            messagebox.showerror("Error","Please enter the answer.",parent=self.root2)
        elif self.new_pass.get()=="":
            messagebox.showerror("Error","Please enter a new password.",parent=self.root2)
        else:
            connection=mysql.connector.connect(host='localhost',user='root',password='samarth29rps123456',database='face_recogniser')
            my_cursor=connection.cursor()
            my_cursor.execute("select * from registration where email=%s and securityQ=%s and securityA=%s",(self.txtuser.get(),self.combo_securityQ.get(),self.combo_securityA.get()))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer.",parent=self.root2)
            else:
                my_cursor.execute("update registration set password=%s where email=%s",(self.new_pass.get(),self.txtuser.get()))
                connection.commit()
                connection.close()
                messagebox.showinfo("Info","Your password has been reset. Please login with new password.",parent=self.root2)
                self.root2.destroy()

    
    def forgot_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the e-mail address to reset password.")
        else:
            connection=mysql.connector.connect(host='localhost',user='root',password='samarth29rps123456',database='face_recogniser')
            my_cursor=connection.cursor()
            my_cursor.execute("select * from registration where email=%s",(self.txtuser.get(),))
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Error","Please enter a valid email id.")
            else:
                connection.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+410+100")

                self.root2.config(bg='black')

                l=Label(self.root2,text="FORGOT PASSWORD",font=("times new roman",15,"bold"),bg="black",fg="orange")
                l.place(x=0,y=10,relwidth=1)

                search_label=Label(self.root2,text="Select Security Question",font=("lucida handwriting",10),bg='black',fg='white')
                search_label.place(x=50,y=70)
                search_combo=ttk.Combobox(self.root2,textvariable=self.combo_securityQ,font=("times new roman",10),width=35,state="readonly")
                search_combo["values"]=("Select","Your birth place","Your girlfriend's name","Your pet's name")
                search_combo.current(0)
                search_combo.place(x=50,y=100)

                ans_lbl=Label(self.root2,text="Security Answer",font=("lucida handwriting",10),bg='black',fg='white')
                ans_lbl.place(x=50,y=130)
                self.ans_entry=ttk.Entry(self.root2,textvariable=self.combo_securityA,width=37,font=("times new roman",10))
                self.ans_entry.place(x=50,y=160)

                pass_lbl=Label(self.root2,text="New Password",font=("lucida handwriting",10),bg='black',fg='white')
                pass_lbl.place(x=50,y=190)
                self.pass_entry=ttk.Entry(self.root2,textvariable=self.new_pass,width=37,font=("times new roman",10))
                self.pass_entry.place(x=50,y=220)

                reset_btn=Button(self.root2,text="Reset",command=self.reset,width=15,font=("times new roman",13),bg="green",fg="white")
                reset_btn.place(x=100,y=250)
            


    
    def login(self):
        if self.studentuser_entry.get=="" or self.pass_entry.get()=="":
            messagebox.showerror("Error","All fields required.")
        elif self.studentuser_entry.get()=="samarth291" and self.pass_entry.get()=="samarth123":
            messagebox.showinfo("Success","Welcome to the Face Recognition Attendance System Project.")
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
        else:
            connection=mysql.connector.connect(host='localhost',user='root',password='samarth29rps123456',database='face_recogniser')
            my_cursor=connection.cursor()
            my_cursor.execute("select * from registration where email=%s and password=%s",(
                                                                                            self.txtuser.get(),
                                                                                            self.txtpass.get()
                                                                                            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password.")
            else:
                open_main=messagebox.askyesno("Query","Access only admin?")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            connection.commit()
            connection.close()




if __name__=="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()