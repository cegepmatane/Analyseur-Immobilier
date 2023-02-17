import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models

#on charge le modele
model = models.load_model("src/ai/modeles")

#on charge l'image
image_to_predict = cv2.imread("dataset/1_kitchen.jpg",cv2.IMREAD_COLOR)
plt.imshow(cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2RGB))

#on redimensionne l'image
image_to_predict = cv2.resize(image_to_predict, (200, 200))
