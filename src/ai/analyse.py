from tensorflow.keras import models
import numpy as np
from ModelParam import ModelParam
import glob
import os

# on charge le modele
model = models.load_model("src/ai/modeles/modele_immo.h5")

# on charge les images de upload
image_paths = sorted(glob.glob("upload/*.*"))

for image_path in image_paths:
    predictions = model.predict(ModelParam.img_to_predict(image_path))
    print(predictions)
    # on affiche le label le plus probable
    print(ModelParam.LABELS[np.argmax(predictions)] + " for " + image_path)
    # on supprime l'image du dossier upload
    os.remove(image_path)


