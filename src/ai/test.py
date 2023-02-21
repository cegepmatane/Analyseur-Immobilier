import cv2
import matplotlib.pyplot as plt
from tensorflow.keras import models

# on charge le modele
model = models.load_model("src/ai/modeles/modele_immo.h5")

# on charge l'image
image_to_predict = cv2.imread("dataset/1_kitchen.jpg", cv2.IMREAD_COLOR)
plt.imshow(cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2RGB))

# on redimensionne l'image
image_to_predict = cv2.resize(image_to_predict, (64, 64))

# on teste le modele
predictions = model.predict(image_to_predict.reshape(1, 64, 64, 3))
print(predictions)