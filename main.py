from tkinter import*
from  tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import os
from attend import Attend
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attend import Attend
from developer import Developer
from help import Help
from chatbot import ChatBot

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap('face.ico')

        img1=Image.open(r"Images\TLL.jpg")
        img1=img1.resize((410,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=410,height=130)

        img2=Image.open(r"Images\TC.jpg")
        img2=img2.resize((410,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=410,y=0,width=410,height=130)

        img3=Image.open(r"Images\TR.jpg")
        img3=img3.resize((410,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=820,y=0,width=410,height=130)

        img4=Image.open(r"Images\dev.jpg")
        img4=img4.resize((1230,590),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,relwidth=1,relheight=1)

        #title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SOFTWARE",font=("times new roman",35,"bold"),fg="white",bg="black")
        #title_lbl.place(x=0,y=50,width=1230,height=45)

        #Buttons
        img5=Image.open(r"Images\StudentDetails.jpg")
        img5=img5.resize((140,110),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=180,y=120,width=140,height=100)
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=180,y=220,width=140,height=40)

        img6=Image.open(r"Images\FD.jpg")
        img6=img6.resize((140,110),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=120,width=140,height=100)
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=400,y=220,width=140,height=40)

        img7=Image.open(r"Images\Attendance.png")
        img7=img7.resize((140,110),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attend)
        b1.place(x=620,y=120,width=140,height=100)
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attend,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=620,y=220,width=140,height=40)

        img8=Image.open(r"Images\Help.jpg")
        img8=img8.resize((140,110),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help)
        b1.place(x=840,y=120,width=140,height=100)
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=840,y=220,width=140,height=40)

        img9=Image.open(r"Images\Train.jpg")
        img9=img9.resize((140,110),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
        b1.place(x=180,y=310,width=140,height=100)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=180,y=410,width=140,height=40)

        img10=Image.open(r"Images\Photos.jpg")
        img10=img10.resize((140,110),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.chatbot)
        b1.place(x=400,y=310,width=140,height=100)
        b1_1=Button(bg_img,text="Chat Bot",cursor="hand2",command=self.chatbot,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=400,y=410,width=140,height=40)

        img11=Image.open(r"Images\Developer.jpg")
        img11=img11.resize((140,110),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.develop)
        b1.place(x=620,y=310,width=140,height=100)
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.develop,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=620,y=410,width=140,height=40)

        img12=Image.open(r"Images\exit.jpg")
        img12=img12.resize((140,110),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit)
        b1.place(x=840,y=310,width=140,height=100)
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("lucida handwriting",10),bg="black",fg="white")
        b1_1.place(x=840,y=410,width=140,height=40)


    #def open_img(self):
    #    os.startfile("data")

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Exit","Are you sure you want to exit?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return


    #Functions

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attend(self.new_window)
    
    def develop(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)
    
    

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

