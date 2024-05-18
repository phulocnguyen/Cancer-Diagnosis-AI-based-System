import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib as mpl
from config import build_unet, dice_coef, precision, sensitivity, specificity
import tensorflow

def get_predictions(t1ce_path, flair_path, slice_to_plot):
    
    t1_ce = nib.load(t1ce_path).get_fdata()
    flair = nib.load(flair_path).get_fdata()

    X = np.empty((75, 128, 128, 2))
    for j in range(75):
        X[j, :, :, 0] = cv2.resize(flair[:,:,j + 60], (128, 128))
        X[j, :, :, 1] = cv2.resize(t1_ce[:,:,j + 60], (128, 128))

    IMG_SIZE = 128
    input_layer = Input((IMG_SIZE, IMG_SIZE, 2))

    best_saved_model = build_unet(input_layer, 'he_normal', 0.2)

    best_saved_model.compile(loss="categorical_crossentropy", optimizer=tensorflow.keras.optimizers.Adam(learning_rate=0.001), metrics = ['accuracy',tensorflow.keras.metrics.MeanIoU(num_classes=4), dice_coef, precision, sensitivity, specificity] )

    best_saved_model.load_weights('model_.29-0.032847.weights.h5')
    
    
    predicted_seg = best_saved_model.predict(X/np.max(X), verbose=1)
    cmap_predict = mpl.colors.ListedColormap(['#440054', '#3b528b', '#18b880', '#e6d74f'])
    norm = mpl.colors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap_predict.N)  

    my_pred = np.argmax(predicted_seg, axis=3)
    my_pred = my_pred[slice_to_plot, :, :]

    my_pred = my_pred.astype(float)
    my_pred[my_pred == 0] = np.nan
    

    fig, axs = plt.subplots(1, 3, figsize=(15, 10))
    axs[0].imshow(t1_ce[:, :,100], cmap="gray")
    axs[0].set_title('T1_CE')
    axs[1].imshow(flair[:, :,100], cmap="gray")
    axs[1].set_title('flair')
    axs[2].imshow(my_pred, cmap_predict, norm)
    axs[2].set_title('Predicton')

    plt.subplots_adjust(wspace=0.8)
    plt.show()
