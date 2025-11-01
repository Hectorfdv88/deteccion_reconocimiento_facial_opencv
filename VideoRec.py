import cv2
import os


#Cargando modelo
opencv_data_path =os.path.join(cv2.__path__[0],'data')
opencv_path_model_frontalface =os.path.join(opencv_data_path,'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(opencv_path_model_frontalface)


cap = cv2.VideoCapture("video/obama_test2.mp4")
i=1
while(cap.isOpened()):
    retval, frame = cap.read()
    # Cargando el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(120, 120), maxSize=(500, 500))
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 10)
        key = cv2.waitKey(1)
        if key == ord('c'):
            face = frame[y:y + h, x:x + w]
            cv2.imwrite("rostros/obama/obama" + str(i) + ".jpg", face)
            i += 1
        cv2.putText(frame,str(i),(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow("Frame", frame)
    key2 = cv2.waitKey(1)
    if key2 == 27:
        break



cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()



#cv2.imshow("Imagen",image)
#k = cv2.waitKey(5000)