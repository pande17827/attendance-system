from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os

class face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Windows")
        
        title_lbl=Label(self.root,text="Face Recognition ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=1,width=1400,height=50)
        
#first image
        img1=Image.open(r"images\1.jpeg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=0,y=52,width=800,height=660)
        
        #second image
        img2=Image.open(r"images\2.png")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=800,y=52,width=800,height=660)
        
        
        
        button1=Button(self.root,text="Face Recognition`",command=self.face_recog,font=("times new roman",35,"bold"),bg="Blue",fg="white")
        button1.place(x=0,y=182,width=1400,height=50)
        
        
    #========================face recognition==============================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMutltiScale(gray_image,scaleFactor,minNeighbours)
            
            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+h])
                confidence=int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="8810620696Vi@",
                        database="face_recognizer",
                    )
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Student_Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                
                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                
                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                else:
                    cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unkown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]
            return coord

        def recognise(img,clf,faceCasCade):
            coor=draw_boundary(img,faceCasCade,1.1,10,(255,255,255),"Face",clf)
            return img

        faceCasCade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)
        while True:
            ret,img=video_cap.read()
            img=recognise(img,clf,faceCasCade)
            cv2.imshow("welcome to face recognition",img)
            
            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()
                    
                
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()