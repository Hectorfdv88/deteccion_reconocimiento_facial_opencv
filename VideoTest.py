import cv2
import os


#Cargando modelo
opencv_data_path =os.path.join(cv2.__path__[0],'data')
opencv_path_model_frontalface =os.path.join(opencv_data_path,'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(opencv_path_model_frontalface)

personas = ['duque','obama']

eigen = cv2.face.EigenFaceRecognizer_create()
eigen.read('eigenface.xml')

cap = cv2.VideoCapture("video/obama_test2.mp4")
i=1
while(cap.isOpened()):
    retval, frame = cap.read()
    # Cargando el frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(50, 50), maxSize=(600, 600))
    print(faces)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 10)
        rostro = gray[y:y + h, x:x + w]
        img_fix = cv2.resize(rostro, dsize=(150, 150))
        predict = eigen.predict(img_fix)
        print(predict)

        if predict[1]<3000:
            cv2.putText(frame,personas[predict[0]],(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        else:
            cv2.putText(frame, 'Desconocido', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Frame", frame)
    key2 = cv2.waitKey(1)
    if key2 == 27:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

#5945.469446404538


#cv2.imshow("Imagen",image)
#k = cv2.waitKey(5000)