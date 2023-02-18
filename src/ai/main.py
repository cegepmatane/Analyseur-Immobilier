import tensorflow as tf
import cv2
from tensorflow.keras import datasets, layers, models
import glob
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical

# on utilise une fonction de Keras
batch_size = 3
img_height = 64
img_width = 64

data_dir = "dataset/"
image_paths = sorted(glob.glob(data_dir + "*_*.*"))

images = []
labels = []

for image_path in image_paths:
    # extraire le label à partir du nom de fichier
    label, extension = image_path.split("_")[-1].split(".")

    # on verifie que l'image est bien au format jpg/jpeg/png/gif
    if extension in ["jpg", "jpeg", "png", "gif"]:
        # on charge l'image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # on redimensionne l'image
        image = cv2.resize(image, (img_height, img_width))

        # on ajoute l'image et le label dans la liste
        images.append(image)
        labels.append(label)

nb_labels = len(set(labels))

print("Nombre d'images chargées: {}".format(len(images)))
print("Nombre de labels chargés: {}".format(nb_labels))

# on cree un modele
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
# on ajoute activation='softmax' pour la classification multi-classes
model.add(layers.Dense(nb_labels, activation='softmax'))

model.summary()

print("Compilation du modèle")
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# on prepare les donnees
images = np.array(images)
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)
labels = to_categorical(labels)

labels = np.array(labels) 

# on entraine le modele
print("Entrainement du modèle")
model.fit(images, labels, batch_size=batch_size, epochs=10, validation_split=0.2)

# on sauvegarde le modele avec l'extension ".h5" pour sauvegarder correctement le modèle
model.save("src/ai/modeles/modele_immo.h5")  