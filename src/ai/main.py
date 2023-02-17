import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models
import glob
import numpy as np

def combine_house_images(house_paths):
	# initialize our list of input images along with the output image
	# after *combining* the four input images
	input_images = []
	output_image = np.zeros((64, 64, 3), dtype="uint8")

	# loop over the input house paths
	for house_path in house_paths:
		# load the input image, resize it to be 32 32, and then
		# update the list of input images
		image = cv2.imread(house_path)
		image = cv2.resize(image, (32, 32))
		input_images.append(image)

	# tile the four input images in the output image such the first
	# image goes in the top-right corner, the second image in the
	# top-left corner, the third image in the bottom-right corner,
	# and the final image in the bottom-left corner
	output_image[0:32, 0:32] = input_images[0]
	output_image[0:32, 32:64] = input_images[1]
	output_image[32:64, 32:64] = input_images[2]
	output_image[32:64, 0:32] = input_images[3]

	# return the combined image
	return output_image

#on utilise une fonction de Keras
batch_size = 3
img_height = 200
img_width = 200

data_dir = "dataset/"
image_paths = sorted(glob.glob(data_dir + "*_*.*"))

images = []
labels = ["bathroom", "bedroom", "kitchen", "frontal"]

for image_path in image_paths:
    # extraire le label à partir du nom de fichier
    label = image_path.split("_")[-1].split(".")[0]

    # collecter les quatre images pour cette maison
    house_paths = glob.glob(image_path.split("_")[0] + "_*.jpg")

    # combiner les images
    combined_image = combine_house_images(house_paths)

    # ajouter l'image et le label à leurs listes respectives
    images.append(combined_image)
    #on ajoute le label si il n'est pas deja dans la liste
    if label not in labels:
        labels.append(label)
  

nb_labels = len(labels)

print("Nombre d'images chargées: {}".format(len(images)))
print("Nombre de labels chargés: {}".format(nb_labels))

#on cree un modele
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(nb_labels))

model.summary()

print("Compilation du modèle")
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#on prepare les donnees
images = np.array(images)
labels = np.array(labels)

#on entraine le modele
print("Entrainement du modèle")
model.fit(images, labels, epochs=10)

#on sauvegarde le modele
model.save("src/ai/modeles")