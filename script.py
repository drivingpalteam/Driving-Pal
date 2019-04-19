import io
import winsound
import cv2
import numpy as np
import time
import socket
import getopt
from sys import argv




def get_irises_location(frame_gray):


    eye_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(frame_gray, 1.3, 10)  # if not empty - eyes detected
    irises = []

    for (ex, ey, ew, eh) in eyes:
        iris_w = int(ex + float(ew / 2))
        iris_h = int(ey + float(eh / 2))
        irises.append([np.float32(iris_w), np.float32(iris_h)])

    return np.array(irises)



def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#print(argv[1])


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Hostip = socket.gethostname()
print(Hostip)
server_address = (Hostip, 10000)
sock.connect(server_address)

print("ready")
data = b''
while True:
    buf = sock.recv(1)
    if data == b'start':
        print("data received")
        print(data)
        break
    else:
        print(data)
        data += buf

cam = cv2.VideoCapture(0)
print("Camera is opened:", cam.isOpened())
sleepcounter = 0
carcounterR = 0
carcounterL = 0
startTimeRight = time.time()
startTimeLeft = time.time()
elapsedRight = 0
elapsedLeft = 0
lastTimeBuzzRight = time.time()
lastTimeBuzzLeft = time.time()
starttimeeyes = time.time()
elapsedeyes = 0
lastTimeeyeBuzz = time.time()
while True:
    # Loading the image to be tested
    success, test_image = cam.read()

    if not success:
        continue
    test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    haar_cascade_face = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_default.xml')

    haar_cascade_eyes = cv2.CascadeClassifier('data/haarcascades/haarcascade_eye.xml')

    faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor=1.6, minNeighbors=5)

    carcascades4 = cv2.CascadeClassifier('data/haarcascades/cas4.xml')


    height, width, channels = test_image.shape

    print('Faces found: ', len(faces_rects))
    for (x, y, w, h) in faces_rects:
        cv2.rectangle(test_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_gray = test_image_gray[y:y + h, x:x + w]
        roi_color = test_image[y: y + h, x:x + w]
        eyes = haar_cascade_eyes.detectMultiScale(roi_gray)

        if len(get_irises_location(roi_gray)) == 0 and len(eyes) > 0 and sleepcounter == 0:
            starttimeeyes = time.time()
            elapsedeyes = time.time() - starttimeeyes
            sleepcounter += 1
        elif len(get_irises_location(roi_gray)) == 0 and len(eyes) > 0 and sleepcounter != 0:
            elapsedeyes = time.time() - starttimeeyes
            sleepcounter += 1
        elif len(get_irises_location(roi_gray)) > 1:
            sleepcounter = 0
            elapsedeyes = 0

        print("Irises:", len(get_irises_location(roi_gray)))
        print("Eyes: ", len(eyes))

        if elapsedeyes > 2:
            print("Asleep: " + str(sleepcounter) + ": " + str(elapsedeyes))
            if time.time() - lastTimeeyeBuzz >= 1:
                winsound.Beep(3500, 1000)
                time.sleep(1)
                lastTimeeyeBuzz = time.time()

        else:

            print("Normal: " + str(sleepcounter) + "; " + str(elapsedeyes))




        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    winname2 = "Driving Pal"

    cv2.namedWindow(winname2)
    cv2.moveWindow(winname2, 0, 0)
    cv2.imshow(winname2, test_image)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        cv2.destroyAllWindows()
        cam.release()
        break