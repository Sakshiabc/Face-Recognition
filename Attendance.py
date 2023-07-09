#Patel, S., Kumar, P., Garg, S. and Kumar, R., 2018.
#Face Recognition based smart attendance system using IOT.
#International Journal of Computer Sciences and Engineering,
#6(5), pp.871-877.

#You are expected to ethically cite the above article

import face_recognition
import cv2
import csv
import pandas as pd
import datetime
import smtplib

a =[]
image = []
face_encoding = []
sir_face_encoding = []
b =[]
x = 0
c=[]
video_capture = cv2.VideoCapture(0)
with open('admin.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        a.append(row["Student Name"])
        b.append(row["image of student"])
        c.append(row["email_id"])
        x = x+1
for i in range(0,x):
        image.append(face_recognition.load_image_file(b[i]))
        sir_face_encoding.append(face_recognition.face_encodings(image[i])[0])
        #face_encoding.append(sir_face_encoding[i])
'''
my_image = face_recognition.load_image_file("abc.jpg")
my_face_encoding = face_recognitin.face_encodings(my_image)[0]
'''
known_face_encodings =sir_face_encoding

known_face_names = a

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
x =[]
while True:

    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                #face_names.append(name)
            #else:
                #name = "Unkown"
                #face_names.append(name)

            face_names.append(name)
            if name not in x:
                x.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()
print(x)
print(a)
for i in x :
    print (i)
    t = ((a.index(i))+1)

now=datetime.datetime.now()
q= now.strftime("%m %d")

df = pd.read_csv("database.csv")
'''
for j in a:
    print(j)
    for i in x :
'''
l=[]
for i in range(0,len(a)):
                if a[i] in x:
                    print("yes")
                    l.append("P")
                    
                else :
                    l.append("A")
                    sender = "______________@gmail.com"
                    receiver = c[i]
                    password = "***************"
                    smtpObj = smtplib.SMTP("smtp.gmail.com",587)
                    smtpObj.starttls()
                    smtpObj.login(sender,password)
                    smtpObj.sendmail(sender,receiver,"Absent")
                    
print(l)                  
df[q]=l                    
                    
                    
df.to_csv("database.csv")
                    
                               

