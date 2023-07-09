#Patel, S., Kumar, P., Garg, S. and Kumar, R., 2018.
#Face Recognition based smart attendance system using IOT.
#International Journal of Computer Sciences and Engineering,
#6(5), pp.871-877.

#You are expected to ethically cite the above article

import cv2
import csv 

x = input("enter student name ")
y = input("enter parent mail id")

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = x+".png"
        cv2.imwrite(img_name, frame)
        #print(img_name".png")
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
myData = [x,img_name,y]

 
myFile = open('admin.csv', 'a')
with myFile:
    writer = csv.writer(myFile)
    writer.writerow(myData)
     
print("Writing complete")

myData2 = [[x]]
 
myFile2 = open('database.csv', 'a')
with myFile2:
    writer = csv.writer(myFile2)
    writer.writerows(myData2)
     
print("Writing complete")




'''
with open('admin.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row[x], row[x+".png"])
with open('database.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
         print(row[x])
'''

#with open('example.csv', newline='') as File:  
#    reader = csv.reader(File)
#    for row in reader:
#        print(x)
	
