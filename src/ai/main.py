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
nb_classes = len(labels)

for image_path in image_paths:
    # extraire le label à partir du nom de fichier
    label = image_path.split("_")[-1].split(".")[0]

    # collecter les quatre images pour cette maison
    house_paths = glob.glob(image_path.split("_")[0] + "_*.jpg")

    # combiner les images
    combined_image = combine_house_images(house_paths)

    # ajouter l'image et le label à leurs listes respectives
    images.append(combined_image)
    labels.append(label)

print("Nombre d'images chargées: {}".format(len(images)))
model = models.Sequential([
    layers.experimental.preprocessing.Rescaling(1./255),
    layers.Conv2D(128,4, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64,4, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(32,4, activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(16,4, activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(nb_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

"""
model.fit( 
    train_data,
  	validation_data=val_data,
  	epochs=2
)"""
