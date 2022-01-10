from logging import exception
from tkinter import*
from  tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk,ImageDraw
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from mysql.connector.constants import FieldType
import numpy as np

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap('face.ico')
    
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1230,height=45)

        img1=Image.open(r"Images\dev.jpg")
        img1=img1.resize((1230,545),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=1230,height=545)

        #Frame
        main_frame=Frame(f_lbl,bd=2,bg="black")
        main_frame.place(x=804,y=80,width=410,height=200)

        img2=Image.open(r"Images\dev.png")
        img2=img2.resize((161,161),Image.ANTIALIAS)
        #height,width = img2.size
        #lum_img = Image.new('L', [height,width] , 0)
        #draw = ImageDraw.Draw(lum_img)
        #draw.pieslice([(0,0), (height,width)], 0, 360, fill = 255, outline = "black")
        #img_arr =np.array(img2)
        #lum_img_arr =np.array(lum_img)
        #final_img_arr = np.dstack((img_arr,lum_img_arr))
        #img2=Image.fromarray(final_img_arr)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(main_frame,image=self.photoimg2,bg='black')
        f_lbl.place(x=243,y=15,width=161,height=161)


        #Developer Info
        title_lbl=Label(main_frame,text="Hello,I am Samarth Mishra.",font=("lucida handwriting",10),fg='white',bg='black')
        title_lbl.place(x=0,y=20)

        title_lbl1=Label(main_frame,text="I am a B.Tech CSE student at",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=40)

        title_lbl1=Label(main_frame,text="National Institute of Technology,",font=("lucida handwriting",9),fg='white',bg="black")
        title_lbl1.place(x=0,y=60)

        title_lbl1=Label(main_frame,text="Rourkela.",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=80)

        title_lbl1=Label(main_frame,text="This is a python based project",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=100)

        title_lbl1=Label(main_frame,text="built using tkinter library for",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=120)

        title_lbl1=Label(main_frame,text="the GUI,OpenCV for face detection",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=140)

        title_lbl1=Label(main_frame,text="and MySQL to handle the database.",font=("lucida handwriting",10),fg='white',bg="black")
        title_lbl1.place(x=0,y=160)

        



if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()