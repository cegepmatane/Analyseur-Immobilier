import numpy as np
from ModelConfig import ModelConfig
from imageai.Detection import ObjectDetection
import glob
import os

# on charge le modele
model = ModelConfig.MODEL

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("src/ai/modeles/retinanet_resnet50_fpn_coco-eeacb38b.pth")
detector.loadModel()

# on charge les images de upload
image_paths = sorted(glob.glob("uploads/*.*"))

for image_path in image_paths:
    predictions = model.predict(ModelConfig.img_to_predict(image_path))
    output_path = "results/"+os.path.basename(image_path)
    detections = detector.detectObjectsFromImage(input_image=image_path, output_image_path=output_path) 
    lsit = []
    for eachObject in detections:
        lsit.append(eachObject["name"])
    # on affiche le label le plus probable
    monF = open("results.txt", "a")
    monF.write(ModelConfig.LABELS[np.argmax(predictions)] + ";" + output_path + ";" + str(lsit) + "\n")
    # on supprime l'image du dossier uploads
