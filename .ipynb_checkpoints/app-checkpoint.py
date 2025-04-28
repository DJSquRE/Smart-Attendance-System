import cv2
import os
import face_recognition

path='known_faces'
student_names=[]
images=[]

mylist=os.listdir(path)

for cl in mylist:
    curimg=cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    student_names.append(os.path.splitext(cl)[0])


def findencodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encode = encodings[0]
            encodelist.append(encode)
        else:
            print("No face found in the image.")
    return encodelist




                      
                      
