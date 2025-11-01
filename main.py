import cv2
import os


opencv_data_path =os.path.join(cv2.__path__[0],'data')
opencv_path_model_frontalface =os.path.join(opencv_data_path,'haarcascade_frontalface_default.xml')
print(opencv_path_model_frontalface)

face_cascade = cv2.CascadeClassifier(opencv_path_model_frontalface)
image = cv2.imread('mr_bean.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), maxSize=(500, 500))
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 10)

cv2.imshow("Imagen",image)
k = cv2.waitKey(10000)