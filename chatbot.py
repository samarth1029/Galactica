from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title('ChatBot')
        self.root.geometry('530x435+350+85')
        self.root.config(bg='powder blue')
        self.root.bind('<Return>',self.enter)
        self.root.wm_iconbitmap('face.ico')

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=530)
        main_frame.pack()

        img=Image.open(r"Images\chatbot.jpg")
        img=img.resize((150,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        title_lbl=Label(main_frame,image=self.photoimg,bd=3,relief=RIDGE,anchor='nw',width=530,compound=LEFT,text="         CHAT++",font=("lucida handwriting",20,'bold'),fg='green')
        title_lbl.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=95,height=17,bd=3,bg='black',fg='white',relief=RIDGE,font=('arial',9),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command=self.text.yview)
        self.text.pack()

        btn_frame=Frame(self.root,bd=0,bg='powder blue',width=530)
        btn_frame.pack()

        label=Label(btn_frame,text="Type something",font=("times new roman",14),fg='green',bg='powder blue')
        label.grid(row=0,column=0,padx=5,sticky='W')

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=35,font=("times new roman",12))
        self.entry1.grid(row=0,column=1,padx=5,sticky='W')

        self.send=Button(btn_frame,text="Send⏩",command=self.send,font=("times new roman",14),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5, sticky='W')

        self.clear=Button(btn_frame,text="Clear🪥",command=self.clear,font=("times new roman",14),width=8,bg='red')
        self.clear.grid(row=1,column=0,padx=5, sticky='W')

        self.msg=''
        self.label1=Label(btn_frame,text=self.msg,font=("times new roman",14),fg='green',bg='powder blue')
        self.label1.grid(row=1,column=1,padx=5,sticky='W')


    def enter(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label1.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label1.config(text=self.msg,fg='red')

        if(self.entry.get().lower()=='hello' or self.entry.get().lower()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        
        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine, what about you?')
        
        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice')
        
        elif(self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Master Samarth did,using python')
        
        elif(self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot: Kaido')

        elif(self.entry.get()=='What is this project about?'):
            self.text.insert(END,'\n\n'+'Bot: This is a face recognition project that creates an excel file computing the attendance of the recognized students.')

        elif(self.entry.get()=='What is is Machine Learning?'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch of artificial intelligence (AI) and computer science which focuses on the use of data and algorithms to imitate the way that humans learn, gradually improving its accuracy.')


        elif(self.entry.get()=='What is is Python programming?'):
            self.text.insert(END,'\n\n'+'Bot: Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.')


        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for your time')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry,I couldn't get you")
        

if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()