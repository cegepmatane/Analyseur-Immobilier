import numpy as np
from ModelConfig import ModelConfig
from imageai.Detection import ObjectDetection
import glob
import os

# on charge le modele
#model = ModelConfig.MODEL

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath("src/ai/modeles/retinanet_resnet50_fpn_coco-eeacb38b.pth")
detector.loadModel()

"""
Ce modèle possède 80 objets détectables :
    person,   bicycle,   car,   motorcycle,   airplane,
    bus,   train,   truck,   boat,   traffic light,   fire hydrant,   stop_sign,
    parking meter,   bench,   bird,   cat,   dog,   horse,   sheep,   cow,   elephant,   bear,   zebra,
    giraffe,   backpack,   umbrella,   handbag,   tie,   suitcase,   frisbee,   skis,   snowboard,
    sports ball,   kite,   baseball bat,   baseball glove,   skateboard,   surfboard,   tennis racket,
    bottle,   wine glass,   cup,   fork,   knife,   spoon,   bowl,   banana,   apple,   sandwich,   orange,
    broccoli,   carrot,   hot dog,   pizza,   donot,   cake,   chair,   couch,   potted plant,   bed,
    dining table,   toilet,   tv,   laptop,   mouse,   remote,   keyboard,   cell phone,   microwave,
    oven,   toaster,   sink,   refrigerator,   book,   clock,   vase,   scissors,   teddy bear,   hair dryer,
    toothbrush.
"""

# on charge les images de upload
image_paths = sorted(glob.glob("uploads/*.*"))

for image_path in image_paths:
    # on prédit l'image
    #predictions = model.predict(ModelConfig.img_to_predict(image_path))
    #on utilise le modèle lite
    interpreter = ModelConfig.LITE_MODEL
    # on récupère les entrées et sorties du modèle
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    input_shape = input_details[0]['shape']
    input_data = ModelConfig.img_to_predict(image_path)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_path = "results/"+os.path.basename(image_path)
    detections = detector.detectObjectsFromImage(input_image=image_path, output_image_path=output_path, minimum_percentage_probability=20) 
    objects = ""
    for eachObject in detections:
        objects += eachObject["name"] + ", "
    objects = objects[:-2]
    # on affiche le label le plus probable
    monF = open("results.txt", "a")
    monF.write(ModelConfig.LABELS[np.argmax(predictions)] + ";" + output_path + ";" + objects + "\n")
    # on supprime l'image du dossier uploads
