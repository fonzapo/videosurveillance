import cv2
import time
import ftplib
from datetime import date
import random
import string

# Set video capture resolution in px
vid = cv2.VideoCapture(0)
vid.set(3, 853)
vid.set(4, 480)

counter = 0
foundFaces = False

path = "C:\\Users\\raoul\\Documents\\PROJETS\\python_video_capture\\capture\\"

# Server credentials
FTP_HOST = ""
FTP_USER = ""
FTP_PW = ""

# Connect to server
ftp = ftplib.FTP_TLS(FTP_HOST, FTP_USER, FTP_PW)
ftp.encoding = "utf-8"

# Create a folder name with current date + random number
numbers = string.digits
dirName = date.today().strftime('%d-%m-%Y') + '_' + \
    ''.join(random.choice(numbers) for i in range(4))

# Make a folder with current date on the server
ftp.mkd(dirName)
print("Created folder '{}'".format(dirName))

# Move to created folder
ftp.cwd(dirName)

# Path to cascade detection xml files for front and profile faces
face_cascade = cv2.CascadeClassifier(
    'C:\\Users\\raoul\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
face_side_cascade = cv2.CascadeClassifier(
    'C:\\Users\\raoul\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\cv2\\data\\haarcascade_profileface.xml')

# Create function to draw rectangle on found face, and upload to server
def foundMatchUpload(face_type, color1, color2, color3):
    for (x, y, w, h) in face_type:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (color1, color2, color3), 2)
        print('Face found in Image {} !'.format(counter))
        with open(imgFullPath, "rb") as file:
            ftp.storbinary("STOR {}".format(img), file)
            print('Image {} uploaded'.format(counter))
            file.close()

while(True):
    ret, frame = vid.read()
    img = 'rec' + str(counter) + '.jpg'
    imgFullPath = str(path) + img

    # Face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_front = face_cascade.detectMultiScale(gray, 1.5, 5)
    faces_profile = face_side_cascade.detectMultiScale(gray, 1.5, 5)

    cv2.imwrite(imgFullPath, frame)

    foundMatchUpload(faces_front, 255, 0, 0)
    foundMatchUpload(faces_profile, 0, 255, 0)

    #cv2.imshow('frame', frame)

    counter += 1

    # Quit on key press : 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    time.sleep(.5)

vid.release()
cv2.destroyAllWindows()

