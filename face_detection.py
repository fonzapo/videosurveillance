import cv2
import time

face_cascade = cv2.CascadeClassifier('C:\\Users\\raoul\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
face_side_cascade = cv2.CascadeClassifier('C:\\Users\\raoul\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_profileface.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces_front = face_cascade.detectMultiScale(gray, 1.5, 5)
    faces_profile = face_side_cascade.detectMultiScale(gray, 1.5, 5)

    for (x, y, w, h) in faces_front:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print('Face found !')
    for (x, y, w, h) in faces_profile:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print('Face found !')

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(.5)

cap.release()
