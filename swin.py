from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np


class Student_Windows:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Windows")
        
        #=================vairable============
        self.var_dep =StringVar()
        self.var_course =StringVar()
        self.var_year =StringVar()
        self.var_semester =StringVar()
        self.var_std_id =StringVar()
        self.var_std_name =StringVar()
        self.var_div =StringVar()
        self.var_roll =StringVar()
        self.var_gender =StringVar()
        self.var_dob =StringVar()
        self.var_email =StringVar()
        self.var_phone =StringVar()
        self.var_address =StringVar()
        self.var_teacher =StringVar()
        
        
        # bg image
        img4=Image.open(r"images\4.png")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimage4)
        bg_img.place(x=0,y=0,width=1530,height=710)
        
        title_lbl=Label(bg_img,text="Stuent Management System",font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1400,height=50)
        
        #creating frame over background image
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=105,width=1480,height=580)
        
        #creating frame over background image
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=105,width=1480,height=580)
        
        #creating left  frame
        Left_Frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        Left_Frame.place(x=0,y=50,width=660,height=580)
        
        #current course information
        current_course_Frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",15,"bold"))
        current_course_Frame.place(x=0,y=150,width=660,height=120)
        
        #department(under current course information )
        dep_label=Label(current_course_Frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0)
        
        dep_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_dep,font=("times new roman",15,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,pady=10)
        
        #courses(under current course information)
        courses_label=Label(current_course_Frame,text="Courses",font=("times new roman",15,"bold"),bg="white")
        courses_label.grid(row=0,column=2)
        
        courses_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly")
        courses_combo["values"]=("Select Courses","FE","SE","TE","BE")
        courses_combo.current(0)
        courses_combo.grid(row=0,column=3,pady=10)
        
        #year(under current course information)
        year_label=Label(current_course_Frame,text="Yeaer",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=0)
        
        year_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_year,font=("times new roman",15,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,pady=10)
        
        #semester(under current course information)
        semester_label=Label(current_course_Frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        semester_label.grid(row=1,column=2)
        
        semester_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_semester,font=("times new roman",15,"bold"),state="readonly")
        semester_combo["values"]=("Select Year","Semester-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,pady=10)
        
        #class student information label
        class_student_information_Frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Class Student Iformation ",font=("times new roman",15,"bold"))
        class_student_information_Frame.place(x=0,y=290,width=660,height=500)
        
        #student id (under class student information label )
        student_id_label=Label(class_student_information_Frame,text="Student Id",font=("times new roman",15,"bold"),bg="white")
        student_id_label.grid(row=0,column=0)
        
        student_id_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_std_id,font=("times new roman",15,"bold"))
        student_id_entry.grid(row=0,column=1,pady=10)
        
         #student name (under class student information label )
        student_name_label=Label(class_student_information_Frame,text="Student Name",font=("times new roman",15,"bold"),bg="white")
        student_name_label.grid(row=0,column=2)
        
        student_name_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_std_name,font=("times new roman",15,"bold"))
        student_name_entry.grid(row=0,column=3,pady=10)
        
        #class division (under class student information label )
        class_division_label=Label(class_student_information_Frame,text="Class Division",font=("times new roman",15,"bold"),bg="white")
        class_division_label.grid(row=1,column=0)
        
        """ class_division_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_div,font=("times new roman",15,"bold"))
        class_division_entry.grid(row=1,column=1,pady=10) """
        
        division_combo=ttk.Combobox(class_student_information_Frame,textvariable=self.var_div,font=("times new roman",15,"bold"),state="readonly")
        division_combo["values"]=("A","B","C")
        division_combo.current(0)
        division_combo.grid(row=1,column=1,pady=10)
        
        
        
        #roll_number (under class student information label )
        roll_number_label=Label(class_student_information_Frame,text="Roll No.",font=("times new roman",15,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2)
        
        roll_number_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_roll,font=("times new roman",15,"bold"))
        roll_number_entry.grid(row=1,column=3,pady=10)
        
        #class gender (under class student information label )
        gender_label=Label(class_student_information_Frame,text="Gender",font=("times new roman",15,"bold"),bg="white")
        gender_label.grid(row=2,column=0)
        
        """ gender_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_gender,font=("times new roman",15,"bold"))
        gender_entry.grid(row=2,column=1,pady=10) """
        
        gender_combo=ttk.Combobox(class_student_information_Frame,textvariable=self.var_gender,font=("times new roman",15,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,pady=10)
        
        #dob (under class student information label )
        dob_label=Label(class_student_information_Frame,text="DOB",font=("times new roman",15,"bold"),bg="white")
        dob_label.grid(row=2,column=2)
        
        dob_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_dob,font=("times new roman",15,"bold"))
        dob_entry.grid(row=2,column=3,pady=13)
        
        #Email (under class student information label )
        Email_label=Label(class_student_information_Frame,text="Email",font=("times new roman",15,"bold"),bg="white")
        Email_label.grid(row=3,column=0)
        
        Email_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        Email_entry.grid(row=3,column=1,pady=13)
        
        #phone_no (under class student information label )
        phone_no_label=Label(class_student_information_Frame,text="Phone No.",font=("times new roman",15,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2)
        
        phone_no_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_phone,font=("times new roman",15,"bold"))
        phone_no_entry.grid(row=3,column=3,pady=13)
        
        
        #addres (under class student information label )
        addres_label=Label(class_student_information_Frame,text="Address",font=("times new roman",15,"bold"),bg="white")
        addres_label.grid(row=4,column=0)
        
        addres_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_address,font=("times new roman",15,"bold"))
        addres_entry.grid(row=4,column=1,pady=13)
        
        #teacher_name (under class student information label )
        teacher_name_label=Label(class_student_information_Frame,text="Teacher Name",font=("times new roman",15,"bold"),bg="white")
        teacher_name_label.grid(row=4,column=2)
        
        teacher_name_entry=ttk.Entry(class_student_information_Frame,textvariable=self.var_teacher,font=("times new roman",15,"bold"))
        teacher_name_entry.grid(row=4,column=3,pady=13)
        
        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_information_Frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0) 
        
        
        radiobtn2=ttk.Radiobutton(class_student_information_Frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1) 
        
        #buttons area
        btn_frame=LabelFrame(class_student_information_Frame,bd=2,bg="white",relief=RIDGE,text="Buttons Area",font=("times new roman",15,"bold"))
        btn_frame.place(x=0,y=290,width=660,height=120)
        
        #save_buttons
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=13,font=("times new roman",15,"bold"),bg="blue")
        save_btn.grid(row=0,column=0)
        
        #update_btn
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=13,font=("times new roman",15,"bold"),bg="blue")
        update_btn.grid(row=0,column=1)
        
        #delete_btn
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font=("times new roman",15,"bold"),bg="blue")
        delete_btn.grid(row=0,column=2)
        
         #reset_bt3
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=13,font=("times new roman",15,"bold"),bg="blue")
        reset_btn.grid(row=0,column=3)
        
        btn_fframe1=Frame(class_student_information_Frame,bd=2,relief=RIDGE,bg="white")
        btn_fframe1.place(x=0,y=350,width=715,height=35)
        
        take_photo_btn=Button(btn_fframe1,text="Take Photo Sample",command=self.generate_dataset,width=25,font=("times new roman",15,"bold"),bg="blue")
        take_photo_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_fframe1,text="Upload Photo Sample",width=30,font=("times new roman",15,"bold"),bg="blue")
        update_btn.grid(row=0,column=1)

        
        
        
        
        
        
        
        
        
        
        
        
        
        #creating Right frame
        #creating Right frame
        right_Frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="login corner",font=("times new roman",15,"bold"))
        right_Frame.place(x=655,y=50,width=660,height=650)
        
         #==========Search system
        Search_frame=LabelFrame(right_Frame,bd=2,bg="white",relief=RIDGE,text="search frame",font=("times new roman",15,"bold"))
        Search_frame.place(x=0,y=75,width=660,height=120)
        
        search_label=Label(Search_frame,text="Search by",font=("times new roman",15,"bold"),bg="red")
        search_label.grid(row=0,column=0)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",15,"bold"),state="readonly")
        search_combo["values"]=("Select ","Roll NO","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,pady=10)
        
        search_entry=ttk.Entry(Search_frame,font=("times new roman",15,"bold"))
        search_entry.grid(row=0,column=1,pady=13,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=13,font=("times new roman",15,"bold"),bg="blue")
        search_btn.grid(row=0,column=3)
        
        show_all_btn=Button(Search_frame,text="Show All",width=13,font=("times new roman",15,"bold"),bg="blue")
        show_all_btn.grid(row=0,column=4)
        
        
        #============Table frame=========
        Table_frame = LabelFrame(right_Frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 15, "bold"))
        Table_frame.place(x=0, y=150, width=617, height=455)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, column=("dep", "course", "year","sem", "id", "name", "div", "roll","dob", "gender","email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        
        self.student_table["show"]="headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
   
   
   
        
    #================function declaration(add data)================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","All fileds are required",parent=self.root)
        else:
            try:
                """ messagebox.showinfo("success","welcome to the codepie") """
                conn=mysql.connector.Connect(host="localhost",username="root",password="8810620696Vi@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                                    
                    
                ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student detail has been adeed successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
                
    #===================fetch data===================
    def fetch_data(self):
        conn=mysql.connector.Connect(host="localhost",username="root",password="8810620696Vi@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
                
            conn.commit()
        conn.close()
        
    
    #========================get update cursor===========
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #====================update function==================
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this student details", parent=self.root
                )
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="8810620696Vi@",
                        database="face_recognizer",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone_No=%s, Address=%s, Teacher=%s, Photo_sample=%s where Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get(),
                        ),
                    )

                    messagebox.showinfo(
                        "Success", "Student details updated successfully", parent=self.root
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()

                else:
                    if not Update:
                        return

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


                
    
    #=================delete function========================
    def delete_data(self):
        if self.var_std_id.get=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                     conn=mysql.connector.Connect(host="localhost",username="root",password="8810620696Vi@",database="face_recognizer")
                     my_cursor=conn.cursor()
                     sql="delete from student where Student_id=%s"
                     val=(self.var_std_id.get(),)
                     my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                
                messagebox.showinfo("Delete","Successfully delted student details",parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Erro",f"Due to :{str(es)}",parent=self.root)
                
                
                
    #====================reset function=====================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
        
        
    
    #=====================Generate data set or Take photo sample======================
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.var_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="8810620696Vi@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                record_count = 0
                for x in myresult:
                    record_count += 1

                my_cursor.execute(
                    "UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone_No=%s, Address=%s, Teacher=%s, Photo_sample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        record_count + 1,
                        self.var_std_id.get(),
                    ),
                )

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ===================Load predefined data on face frontals from OpenCV==============
                face_classifier = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    if len(faces) > 0:
                        (x, y, w, h) = faces[0]  # Use the first detected face
                        face_cropped = img[y : y + h, x : x + w]
                        return face_cropped
                    else:
                        return None

                cap = cv2.VideoCapture(0)
                image_id = 0
                while True:
                    ret, my_frame = cap.read()
                    face = face_cropped(my_frame)
                    if face is not None:
                        image_id += 1

                        face = cv2.resize(face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(record_count + 1) + "." + str(image_id) + ".jpg"
                        cv2.imwrite(file_name_path, face.astype(np.uint8))
                        cv2.putText(
                            my_frame,
                            str(image_id),
                            (50, 50),  # Position of the text
                            cv2.FONT_HERSHEY_SIMPLEX,
                            2,
                            (0, 255, 0),
                            3,  # Thickness
                            cv2.LINE_AA,
                        )
                        cv2.imshow("Cropped Face", my_frame)

                    if cv2.waitKey(1) == 13 or image_id == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)





                
                    
                
                    
                    
        
    
                
                    
                    
                    
        
        
                  
        
    
            
            
        
        
        
        
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student_Windows(root)
    root.mainloop()