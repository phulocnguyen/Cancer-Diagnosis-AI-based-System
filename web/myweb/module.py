
import numpy as np
import os
from tensorflow import keras
import cv2
from keras.models import load_model
from . import configmodel

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
        return "Glioma"
    elif result == 1:
        return "Meningioma"
    elif result == 2:
        return "No tumor"
    else:
        return "Pituiraty"

def prediction_2():
    t1ce_path = 'myweb/static/userdata/t1ce.nii'
    flair_path = 'myweb/static/userdata/flair.nii'
    slice_to_plot = 50

    result_image = configmodel.get_predictions(t1ce_path, flair_path, slice_to_plot)

    # Xóa tệp cũ nếu tồn tại
    if os.path.exists('myweb/static/userdata/prediction_result.png'):
        os.remove('myweb/static/userdata/prediction_result.png')

    # Lưu hình ảnh mới
    result_image.save('myweb/static/userdata/prediction_result.png')
    
    return "Location of tumor"
