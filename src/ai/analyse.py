from tensorflow.keras import models
import numpy as np
from ModelConfig import ModelConfig
import glob
import os

# on charge le modele
model = models.load_model("src/ai/modeles/modele_immo.h5")

# on charge les images de upload
image_paths = sorted(glob.glob("uploads/*.*"))

for image_path in image_paths:
    predictions = model.predict(ModelConfig.img_to_predict(image_path))
    # on affiche le label le plus probable
    print(ModelConfig.LABELS[np.argmax(predictions)] + " for " + image_path)
    # on supprime l'image du dossier uploads
    os.remove(image_path)
