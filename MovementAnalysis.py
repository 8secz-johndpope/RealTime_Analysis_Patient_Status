import os

import cv2
import boto3
from threading import Timer


f=0


changingCenter=0


flatValueX=0
flatValuey=0

#variabile di supporto per il primo valore da confrontare del BoundingBox
support=0
supportX=0
supportY=0


count=0

#variabile usata in locale nella funzione hello per poi effettuare un controllo nel main  e settare a 0 la variabile changingCenter
movementBool=0

def instant():

    if changingCenter>0 : # Se ci sono stati più di 4 movimenti nell'intervallo di tempo stabilito allora changinChange vale 1 allora si va a verificare l'espressione facciale

        print('************************** CHANGE MOVEMENT **********************')

        global movementBool
        movementBool = 1

        global f
        f=1

    else:
        startTimer()


def startTimer():
  print(changingCenter)
  t = Timer(20.0, instant)
  t.start()  # after 20 seconds, "hello, world" will be printed


# Setup
scale_factor = .15
green = (0, 255, 0)
red = (0, 0, 255)
frame_thickness = 2
cap = cv2.VideoCapture(0)
rekognition = boto3.client('rekognition')

startTimer()


while (f==0):

    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, channels = frame.shape

    # Convert frame to jpg
    small = cv2.resize(frame, (int(width * scale_factor), int(height * scale_factor)))
    ret, buf = cv2.imencode('.jpg', small)

    # Detect faces in jpg
    faces = rekognition.detect_faces(Image={'Bytes': buf.tobytes()}, Attributes=['ALL'])

    faces = rekognition.detect_faces(Image={'Bytes': buf.tobytes()}, Attributes=['ALL'])


    # Draw rectangle around faces
    for face in faces['FaceDetails']:
        smile = face['Emotions']
        cv2.rectangle(frame,
                      (int(face['BoundingBox']['Left'] * width),
                       int(face['BoundingBox']['Top'] * height)),
                      (int((face['BoundingBox']['Left'] + face['BoundingBox']['Width']) * width),
                       int((face['BoundingBox']['Top'] + face['BoundingBox']['Height']) * height)),
                      red, frame_thickness)

        x = face['BoundingBox']['Left']
        y = face['BoundingBox']['Top']
        width = face['BoundingBox']['Width']
        height = face['BoundingBox']['Height']

        centerX = (x + (width / 2))
        centerY = (y + (height / 2))
        print(centerX)
        print(centerY)

        if support == 0:
            supportX = centerX
            supportY = centerY
            support = 1


        if (  ((supportX-centerX)>0.15) or ((supportX-centerX)< -0.15)  or ((supportY-centerY)>0.15) or ((supportY-centerY)<-0.15) ):
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  SHIFT >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            count=count+1
            if count>3 : changingCenter=1




