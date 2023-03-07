import numpy as np
from ModelConfig import ModelConfig
import glob
import os

# on charge le modele
model = ModelConfig.MODEL

# on charge les images de upload
image_paths = sorted(glob.glob("uploads/*.*"))

for image_path in image_paths:
    predictions = model.predict(ModelConfig.img_to_predict(image_path))
    # on affiche le label le plus probable
    monF = open("results.txt", "a")
    monF.write(ModelConfig.LABELS[np.argmax(predictions)] + ";" + image_path +"\n")
    # on supprime l'image du dossier uploads
