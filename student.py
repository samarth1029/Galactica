from logging import exception
from tkinter import*
from  tkinter import ttk
from tkinter import font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1230x590+0+0")
        self.root.title("Student Details")
        self.root.wm_iconbitmap('face.ico')

        #Variables
        self.var_dep=StringVar()  
        self.var_course=StringVar() 
        self.var_year=StringVar() 
        self.var_semester=StringVar() 
        self.var_std_id=StringVar() 
        self.var_std_name=StringVar() 
        self.var_gender=StringVar() 
        self.var_email=StringVar() 
        self.var_phone=StringVar() 
        self.var_teacher=StringVar() 


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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1230,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1200,height=390)

        #label frames
        #left
        left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",bg="black",fg="white",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=570,height=360)

        current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=5,width=560,height=120)
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12))
        dep_label.grid(row=0,column=0,padx=10)
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),state="readonly")
        dep_combo["values"]=["Select Department","Computer Science and Engineering","Electronics and Communication Engineering","Civil Engineering","Mechanical Engineering","Ceramic Engineering","Chemical Engineering"]
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        course_label=Label(current_course_frame,text="Course",font=("times new roman",12))
        course_label.grid(row=0,column=2,padx=5,sticky=W)
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),state="readonly")
        course_combo["values"]=["Select Course","A","B","C","D","E","F"]
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        year_label=Label(current_course_frame,text="Year",font=("times new roman",12),fg='white',bg='black')
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),state="readonly")
        year_combo["values"]=["Select Year","2020-21","2021-22","2022-23","2023-24"]
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12),fg='white',bg='black')
        semester_label.grid(row=1,column=2,padx=5,sticky=W)
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12),state="readonly")
        semester_combo["values"]=["Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8"]
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Info",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=130,width=560,height=205)

        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",12))
        studentID_label.grid(row=0,column=0,padx=5,sticky=W)
        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)

        studentName_label=Label(class_student_frame,text="Student Name",font=("times new roman",12))
        studentName_label.grid(row=0,column=2,padx=5,sticky=W)
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12))
        studentName_entry.grid(row=0,column=3,padx=10,sticky=W)

        studentGender_label=Label(class_student_frame,text="Gender",font=("times new roman",12),fg='white',bg='black')
        studentGender_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        studentGender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12),state="readonly")
        studentGender_combo["values"]=["Male","Female","Other"]
        studentGender_combo.current(0)
        studentGender_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        studentTeacher_label=Label(class_student_frame,text="Teacher",font=("times new roman",12),fg='white',bg='black')
        studentTeacher_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        studentTeacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12))
        studentTeacher_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        studentEmail_label=Label(class_student_frame,text="E-Mail",font=("times new roman",12))
        studentEmail_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        studentEmail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12))
        studentEmail_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        studentPhone_label=Label(class_student_frame,text="Phone No.",font=("times new roman",12))
        studentPhone_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        studentPhone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12))
        studentPhone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Radio
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=3,column=0)
        radiobtn1_label=Label(class_student_frame,text="Take Photo Sample",font=("times new roman",12))
        radiobtn1_label.place(x=50,y=92)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,value="No")
        radiobtn2.grid(row=3,column=2)
        radiobtn2_label=Label(class_student_frame,text="No Photo Sample",font=("times new roman",12))
        radiobtn2_label.place(x=340,y=92)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=115,width=555,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=14,font=("times new roman",13),bg="darkblue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",13),bg="darkblue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=14,font=("times new roman",13),bg="darkblue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13),bg="darkblue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(btn_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=30,width=555,height=70)

        take_photo_btn=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=28,font=("times new roman",13),bg="darkgreen",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=32,font=("times new roman",13),bg="darkgreen",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #Right
        right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="black",fg="white")
        right_frame.place(x=600,y=10,width=570,height=360)

        img=Image.open(r"Images\helloo.jpg")
        img=img.resize((410,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=620,y=220,width=550,height=100)

        search_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=5,y=105,width=550,height=63)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12))
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12),state="readonly")
        search_combo["values"]=("Select","Roll Number","Phone Number")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        search_btn=Button(search_frame,text="Search",width=6,font=("times new roman",13),bg="darkblue",fg="white")
        search_btn.grid(row=0,column=3)
        showAll_btn=Button(search_frame,text="Show All",width=7,font=("times new roman",13),bg="darkblue",fg="white")
        showAll_btn.grid(row=0,column=4)

        #table frame
        table_frame=LabelFrame(right_frame,bd=2,relief=RIDGE,text="Table Frame",font=("times new roman",13,"bold"))
        table_frame.place(x=5,y=172,width=550,height=160)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Semester","StudentID","StudentName","Gender","Teacher","E-mail","PhoneNo","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("StudentID",text="StudentID")
        self.student_table.heading("StudentName",text="StudentName")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("E-mail",text="E-mail")
        self.student_table.heading("PhoneNo",text="PhoneNo")
        self.student_table.heading("PhotoSample",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("Dep",width=200)
        self.student_table.column("Course",width=60)
        self.student_table.column("Year",width=80)
        self.student_table.column("Semester",width=80)
        self.student_table.column("StudentID",width=80)
        self.student_table.column("StudentName",width=120)
        self.student_table.column("Gender",width=60)
        self.student_table.column("Teacher",width=60)
        self.student_table.column("E-mail",width=120)
        self.student_table.column("PhoneNo",width=80)
        self.student_table.column("PhotoSample",width=80)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #Functions

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
            #messagebox.showinfo("Success","Welcome.")
            try:
                connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
                my_cursor=connection.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_teacher.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_radio1.get()
                                                                                                ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success","Student Details have been added successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

    #fetch data
    def fetch_data(self):
        connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
        my_cursor=connection.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            connection.commit()
        connection.close()

    #get cursor function
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_teacher.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_radio1.set(data[10])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student's details?",parent=self.root)
                if Update>0:
                    connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
                    my_cursor=connection.cursor()
                    my_cursor.execute("update student set `Dep`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`StudentName`=%s,`Gender`=%s,`Teacher`=%s,`E-mail`=%s,`PhoneNo`=%s,`PhotoSample`=%s where `StudentID`=%s",(   
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get(),
                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student Details Updated successfully.",parent=self.root)
                connection.commit()
                self.fetch_data()
                connection.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    
    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to delete the Student's details?",parent=self.root)
                if delete>0:
                    connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
                    my_cursor=connection.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
               
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success","Student Details Deleted successfully.",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



    #Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_gender.set("Male")
        self.var_teacher.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    #Generate dataset or Take Photo Sample

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required.",parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host='localhost',database='face_recogniser',user='root',password='samarth29rps123456')
                my_cursor=connection.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set `Dep`=%s,`Course`=%s,`Year`=%s,`Semester`=%s,`StudentName`=%s,`Gender`=%s,`Teacher`=%s,`E-mail`=%s,`PhoneNo`=%s,`PhotoSample`=%s where `StudentID`=%s",(   
                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                self.var_std_id.get()==id+1
                                                                                                                                                                ))
                connection.commit()
                self.fetch_data()
                self.reset_data()
                connection.close()

                #Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    #Minimum Neighbours=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed.")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()