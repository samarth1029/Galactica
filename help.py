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

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Help Desk")
        self.root.wm_iconbitmap('face.ico')
    
        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1230,height=45)

        img1=Image.open(r"Images\dev.jpg")
        img1=img1.resize((1230,545),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=1230,height=545)

        title_lbl=Label(f_lbl,text="Email: samarthmishra291@gmail.com",font=("lucida handwriting",10),bg='white',fg='black')
        title_lbl.place(x=500,y=270)







if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()