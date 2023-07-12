import deepface
from deepface import DeepFace
import os
#path of database to be put in db_path
#path of testing images to be put in img_path
df = DeepFace.find(img_path = "atharva.jpg", db_path = "C:/Users/wasra/caps_img_db")
#path of representations_vgg_face.pkl to be put here
os.remove("C:/Users/wasra/caps_img_db/representations_vgg_face.pkl")
print(df.head(1))