import tensorflow as tf
from keras.models import Model
import cv2
import matplotlib.pyplot as plt


#on utilise une fonction de Keras
batch_size = 3
img_height = 200
img_width = 200

data_dir = "C:\wamp64\www\projets-specialises-2023-zhishengtrieu\dataset"

train_data = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=42,
  image_size=(img_height, img_width),
  batch_size=batch_size,
  )

val_data = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=42,
  image_size=(img_height, img_width),
  batch_size=batch_size)

class_names = val_data.class_names
