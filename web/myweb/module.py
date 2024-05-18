
import numpy as np
import os
from tensorflow import keras
import cv2
from keras.models import load_model

IMAGE_SIZE = 150


def load_image(image_path: str):
    img_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img_array, (IMAGE_SIZE, IMAGE_SIZE))
    img = img.reshape(-1, 150, 150)
    normalized_img = img/255.0
    normalized_img = normalized_img.reshape(-1, 150, 150, 1)
    return normalized_img


def prediction_1(img):
    model = load_model('ModelAI/model/BrainTumor.h5')
    res = model.predict(img)
    result = res.argmax()
    if result == 0:
        return "glioma"
    elif result == 1:
        return "meningioma"
    elif result == 2:
        return "no tumor"
    else:
        return "pituiraty"

def prediction_2(img1, img2):
    return "coming soon"

def main():
    image = load_image('myweb/static/userdata/test.jpg')
    print(prediction(image))


if __name__ == "__main__":
    main()