from tensorflow.keras import models
import numpy as np
from ModelConfig import ModelConfig

# on charge le modele
model = models.load_model("src/ai/modeles/modele_immo.h5")

# on charge l'image
path = "dataset/92_bathroom.jpg"
# path = "dataset/312_kitchen.jpg"
# path = "dataset/58_bedroom.jpg"
# path = "dataset/8_frontal.jpg"
# path = "dataset/6_frontal.jpg"
# path = "dataset/83_bedroom.jpg"

image_to_predict = ModelConfig.img_to_predict(path)
predictions = model.predict(image_to_predict)
print(predictions)
# on affiche le label le plus probable
print(ModelConfig.LABELS[np.argmax(predictions)])
