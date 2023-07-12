import deepface
from deepface import DeepFace
import os
metrics = ["cosine", "euclidean"]
models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
#path of database to be put in db_path
#path of testing images to be put in img_path
#face recognition
df = DeepFace.find(img_path = "ath1.jpg", db_path = "/home/pi/Desktop/caps_img", model_name = models[7], distance_metric = metrics[1])
#path of representations_vgg_face.pkl to be put here
os.remove("/home/pi/Desktop/caps_img/representations_dlib.pkl")
print(df.head(1))