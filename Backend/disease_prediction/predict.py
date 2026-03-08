import numpy as np
import cv2
import json
from tensorflow.keras.models import load_model

model = load_model("final_model/disease_model.h5")

with open("final_model/class_indices.json") as f:
    class_indices = json.load(f)

labels = {v:k for k,v in class_indices.items()}


def predict_disease(img_path):

    img = cv2.imread(img_path)

    img = cv2.resize(img,(128,128))

    img = img/255.0

    img = np.expand_dims(img,axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    return labels[index]