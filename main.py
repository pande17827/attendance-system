from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from swin import Student_Windows
import os
from training_data_set import train
from working_face_recognition_windows import FaceRecognition


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #first image
        img1=Image.open(r"images\1.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=0,width=500,height=130)
        
        #second image
        img2=Image.open(r"images\2.png")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #third image
        img3=Image.open(r"images\3.jpeg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=0,width=550,height=130)
        
        # bg image
        img4=Image.open(r"images\4.png")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimage4)
        bg_img.place(x=0,y=130,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Face Recognition Attendence System Software",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1250,height=45)
        
         
        #student  button
        img5=Image.open(r"buttons\student information.png")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimage5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimage5,command=self.stuents_details,cursor="hand2")
        b1.place(x=120,y=50,width=220,height=220)
        
        b1=Button(bg_img,text="Student Details",command=self.stuents_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=120,y=250,width=220,height=40)
        
        # face recognition
        img6=Image.open(r"buttons\face detector.jpeg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimage6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,command=self.face_data,image=self.photoimage6,cursor="hand2")
        b1.place(x=420,y=50,width=220,height=220)
        
        b1=Button(bg_img,command=self.face_data,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=420,y=250,width=220,height=40)
        
        
         # attendence
        img7=Image.open(r"buttons\attendance.jpeg")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimage7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimage7,cursor="hand2")
        b1.place(x=720,y=50,width=220,height=220)
        
        b1=Button(bg_img,text="Attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=720,y=250,width=220,height=40)
        
        
        # help desk
        img8=Image.open(r"buttons\help desk.png")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimage8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimage8,cursor="hand2")
        b1.place(x=1020,y=50,width=220,height=220)
        
        b1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1020,y=250,width=220,height=40)
        
        
        # train data
        img9=Image.open(r"buttons\train data.jpeg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimage9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,command=self.training_data,image=self.photoimage9,cursor="hand2")
        b1.place(x=120,y=300,width=220,height=220)
        
        b1=Button(bg_img,command=self.training_data,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=120,y=500,width=220,height=40)
        
        
        # photos
        img10=Image.open(r"buttons\photos.jpeg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimage10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimage10,command=self.open_img,cursor="hand2")
        b1.place(x=420,y=300,width=220,height=220)
        
        b1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),command=self.open_img,bg="darkblue",fg="white")
        b1.place(x=420,y=500,width=220,height=40)
        
        
         # developers
        img11=Image.open(r"buttons\developer.png")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimage11,cursor="hand2")
        b1.place(x=720,y=300,width=220,height=220)
        
        b1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=720,y=500,width=220,height=40)
        
        
        # exit 
        img12=Image.open(r"buttons\exit.jpeg")
        img12=img12.resize((220,220),Image.LANCZOS)
        self.photoimage12=ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,image=self.photoimage12,cursor="hand2")
        b1.place(x=1020,y=300,width=220,height=220)
        
        b1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1.place(x=1020,y=500,width=220,height=40)
        
        
        
    def open_img(self):
        os.startfile("data")   
        
        
        
         
        
    #======================function to link with buttons================
    def stuents_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Windows(self.new_window)
        
    #======================fucntion to link traing_data_set_button==========
    def training_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
        

        
    #======================fucntion to link recognizing_faces_button==========
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()