from tkinter import *
from PIL import Image, ImageTk
import cv2
import mysql.connector

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Windows")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=1, width=1400, height=50)

        img1 = Image.open(r"images\1.jpeg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimage1)
        f_lbl.place(x=0, y=52, width=800, height=660)

        img2 = Image.open(r"images\2.png")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimage2)
        f_lbl.place(x=800, y=52, width=800, height=660)

        button1 = Button(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="Blue", fg="white", command=self.face_recog)
        button1.place(x=0, y=182, width=1400, height=50)

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbour, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)

        coord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int(100 * (1 - predict / 300))

            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="8810620696Vi@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else ""  # Check if n is not None

                my_cursor.execute("select Roll from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else ""  # Check if r is not None

                my_cursor.execute("select Dep from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else ""  # Check if d is not None

                if confidence > 10:
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "unknown face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            except mysql.connector.Error as e:
                print("Error connecting to MySQL:", e)

            finally:
                if conn.is_connected():
                    conn.close()

        return coord

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                print(f"ID: {id}, Confidence: {confidence}")  # Print for debugging

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="8810620696Vi@",
                    database="face_recognizer",
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Student_Name, Roll, Dep FROM student WHERE Student_id=" + str(id))
                result = my_cursor.fetchone()

                if result:
                    student_name, roll, department = result
                    cv2.putText(img, f"Roll: {roll}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Student Name: {student_name}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Department: {department}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
