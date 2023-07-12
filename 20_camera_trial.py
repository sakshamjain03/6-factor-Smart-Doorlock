
import deepface
from deepface import DeepFace
import os
#!/bin/bash fswebcam -r 1280*960 /home/pi/Desktop/saved_pic/$test.jpg
import cv2

cam = cv2.VideoCapture(0)


ret, image = cam.read()
cv2.imshow('Imagetest',image)
	
cv2.imwrite('/home/pi/Desktop/saved_pic/test.jpg', image)
cam.release()
cv2.destroyAllWindows()
metrics = ["cosine", "euclidean","euclidean_l2"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
#path of database to be put in db_path
#path of testing images to be put in img_path
#face recognition
try:
    df = DeepFace.find(img_path = "/home/pi/Desktop/saved_pic/test.jpg", db_path = "/home/pi/Desktop/caps_img", model_name = models[7], distance_metric = metrics[1])
#path of representations_vgg_face.pkl to be put here
    #/home/pi/Desktop/saved_pic/test.jpg
    os.remove("/home/pi/Desktop/caps_img/representations_dlib.pkl")
    #os.remove("/home/pi/Desktop/saved_pic/test.jpg")
#print(df.head(1))

    if(df['Dlib_euclidean'][0]<0.5):
        print(df['identity'][0])
    
    else:
        print("Unknown picture")

except:
  print("No face detected")