import cv2
import os
import numpy as np

personas = ['duque','obama']
y =[]
X = []

for persona in personas:
    rostros = os.listdir('rostros/'+persona)
    for rostro in rostros:
        print(rostro)
        img = cv2.imread('rostros/'+persona+'/'+rostro)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_fix = cv2.resize(gray,dsize=(150,150))
        if rostro.startswith('duque'):
            y.append(0)
        else:
            y.append(1)
        X.append(img_fix)

print(y)

eigen = cv2.face.EigenFaceRecognizer_create()
eigen.train(X,np.array(y))
eigen.write('eigenface.xml')