import cv2
import boto3
from threading import Timer

f=0

changingEmotions=0    # SAD=1   ANGRY=2  CONFUSED=3  FEAR=5

flatValueX=0
flatValuey=0

#variabile di supporto per il primo valore da confrontare del BoundingBox
support=0
supportX=0
supportY=0

count=0

#variabile usata in locale nella funzione hello per poi effettuare un controllo nel main  e settare a 0 la variabile changingCenter
emotionBool=0





def instant():
        print("partito ______--")
        if (changingEmotions>0) :
            print ('************************** CHANGE EMOTION **********************')
            global emotionBool
            emotionBool = 1

            global f
            f=1

        else :
             startTimer()



def startTimer():

  t = Timer(20.0, instant)
  t.start()  # after 20 seconds, "hello, world" will be printed



scale_factor = .15
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
                for instance in face['Emotions']:
                    conf = instance['Confidence']
                    confidence = int(conf)

                    if confidence > 50:
                        print(instance['Type'])
                        emotion=instance['Type']


                        if((emotion=='SAD') or (emotion=='ANGRY') or (emotion=='CONFUSED') or (emotion=='FEAR') ):
                            changingEmotions=1


                        print(confidence)

                        print()
                        print()

