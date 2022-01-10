from logging import exception
from tkinter import*
from  tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from mysql.connector.constants import FieldType
import numpy as np

mydata=[]
class Attend:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Attendance")
        self.root.wm_iconbitmap('face.ico')

        #variables
        self.var_att_id=StringVar()
        self.var_att_name=StringVar()
        self.var_att_dep=StringVar()
        self.var_att_date=StringVar()
        self.var_att_time=StringVar()
        self.var_att_status=StringVar()


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

        img4=Image.open(r"Images\download.jpg")
        img4=img4.resize((1230,460),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1230,height=460)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1230,height=45)

        #Frames
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1200,height=390)

        #label frames
        #left
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",bg="black",fg="white",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=570,height=360)

        img=Image.open(r"Images\clock.jpg")
        img=img.resize((550,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=35,y=220,width=550,height=100)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y=105,width=550,height=225)

        #Labels & Entries
        attendanceID_label=Label(left_inside_frame,text="AttendanceID: ",font=("times new roman",12))
        attendanceID_label.grid(row=0,column=0,padx=5,sticky=W)
        attendanceID_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_att_id,font=("times new roman",12))
        attendanceID_entry.grid(row=0,column=1,padx=10,sticky=W)

        roll_label=Label(left_inside_frame,text="Roll:             ",font=("times new roman",12))
        roll_label.grid(row=0,column=2,sticky=W)
        roll_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_id,font=("times new roman",12))
        roll_entry.grid(row=0,column=3,padx=10,sticky=W)

        name_label=Label(left_inside_frame,text="Name:             ",font=("times new roman",12),fg='white',bg='black')
        name_label.grid(row=1,column=0,padx=5,sticky=W)
        name_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_att_name,font=("times new roman",12))
        name_entry.grid(row=1,column=1,padx=10,sticky=W)

        department_label=Label(left_inside_frame,text="Department: ",font=("times new roman",12),fg='white',bg='black')
        department_label.grid(row=1,column=2,sticky=W)
        department_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_dep,font=("times new roman",12))
        department_entry.grid(row=1,column=3,padx=10,sticky=W)

        time_label=Label(left_inside_frame,text="Time:               ",font=("times new roman",12))
        time_label.grid(row=2,column=0,padx=5,sticky=W)
        time_entry=ttk.Entry(left_inside_frame,width=15,textvariable=self.var_att_time,font=("times new roman",12))
        time_entry.grid(row=2,column=1,padx=10,sticky=W)

        date_label=Label(left_inside_frame,text="Date:            ",font=("times new roman",12))
        date_label.grid(row=2,column=2,sticky=W)
        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_att_date,font=("times new roman",12))
        date_entry.grid(row=2,column=3,padx=10,sticky=W)

        attendanceStatus_label=Label(left_inside_frame,text="Attendance Status: ",font=("times new roman",12),fg='white',bg='black')
        attendanceStatus_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        self.attendanceStatus_combo=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_att_status,font=("times new roman",12),state="readonly")
        self.attendanceStatus_combo["values"]=["Satus","Present","Absent"]
        self.attendanceStatus_combo.current(0)
        self.attendanceStatus_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #buttons
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=185,width=555,height=70)

        save_btn=Button(btn_frame,text="Import CSV",width=14,command=self.import_csv,font=("times new roman",13),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",width=14,command=self.export_csv,font=("times new roman",13),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",width=14,font=("times new roman",13),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=14,command=self.reset_data,font=("times new roman",13),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

        #Right Frame
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="black",fg="white")
        right_frame.place(x=600,y=10,width=570,height=360)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=555,height=325)

        #table and scroll bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("ID","Name","Department","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="StudentID")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance Status")
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.column("ID",width=80)
        self.AttendanceReportTable.column("Name",width=150)
        self.AttendanceReportTable.column("Department",width=240)
        self.AttendanceReportTable.column("Time",width=150)
        self.AttendanceReportTable.column("Date",width=150)
        self.AttendanceReportTable.column("Attendance",width=130)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    #fetch data

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    #import csv
    def import_csv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #export csv
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export.",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode='w',newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your data has been successfully exported to "+os.path.basename(fln))
        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_att_id.set(rows[0])
        self.var_att_name.set(rows[1])
        self.var_att_dep.set(rows[2])
        self.var_att_time.set(rows[3])
        self.var_att_date.set(rows[4])
        self.var_att_status.set(rows[5])

    def reset_data(self):
        self.var_att_id.set("")
        self.var_att_name.set("")
        self.var_att_dep.set("")
        self.var_att_time.set("")
        self.var_att_date.set("")
        self.var_att_status.set("Status")





if __name__=="__main__":
    root=Tk()
    obj=Attend(root)
    root.mainloop()