from logging import exception
from tkinter import*
from  tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Train Dataset")
        self.root.wm_iconbitmap('face.ico')

        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="lightblue",fg="black")
        title_lbl.place(x=0,y=0,width=1230,height=45)

        img1=Image.open(r"Images\topL.jpg")
        img1=img1.resize((410,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=45,width=410,height=130)

        img2=Image.open(r"Images\topC.jpg")
        img2=img2.resize((410,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=410,y=45,width=410,height=130)

        img3=Image.open(r"Images\topR.jpg")
        img3=img3.resize((410,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=820,y=45,width=410,height=130)  

        

        img4=Image.open(r"Images\down.jpg")
        img4=img4.resize((1230,590),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #Button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="white")
        b1_1.place(x=500,y=250,width=300,height=60)

    
    def train_classifier(self):
        data_dir=("data")
        path= [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #Gray Scale Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            #data\user.3.1.jpg
            #0                                                  1
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #Train the classifier
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training dataset completed.")



        








if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()