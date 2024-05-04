import cv2 
#Face Detection In Picture 
img = cv2.imread('photo1.jpeg') 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
haar_cascade = cv2.CascadeClassifier('Haarcascade_frontalface_default.xml') 
faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9) 
for (x, y, w, h) in faces_rect: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2) 
cv2.imshow('Detected faces', img) 
cv2.waitKey(0) 

#Face Detection In Video
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('video2.mp4')
if not cap.isOpened():
    print("Error: Unable to open video file or capture device.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Face Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #Press 'q' in order to exit face detection.
        break
cap.release()
cv2.destroyAllWindows()
