from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Windows")
        
        title_lbl=Label(self.root,text="Photo Sample Training",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=1,width=1400,height=50)
        
        #first image
        img1=Image.open(r"images\1.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=52,width=500,height=130)
        
        #second image
        img2=Image.open(r"images\2.png")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=500,y=52,width=500,height=130)
        
        #third image
        img3=Image.open(r"images\3.jpeg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        f_lbl=Label(self.root,image=self.photoimage3)
        f_lbl.place(x=1000,y=52,width=550,height=130)
        
        
        button1=Button(self.root,text="Train Data",command=self.train_classifier,font=("times new roman",35,"bold"),bg="Blue",fg="white")
        button1.place(x=0,y=182,width=1400,height=50)
        
        img4=Image.open(r"images\4.png")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimage4)
        bg_img.place(x=0,y=233,width=1530,height=710)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert("L") #shortcut to convert image into gray color
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split(".")[1])
            
            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)

        #=======================train the clasifier================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","training dataset completed!!!!")






        
        
if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()