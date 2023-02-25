import cv2
from tensorflow.keras import layers, models, optimizers
import glob
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 2
img_height = 64
img_width = 64

# on charge les images du dataset
data_dir = "dataset/"
image_paths = sorted(glob.glob(data_dir + "*_*.*"))

images = []
labels = []

for image_path in image_paths:
    # on extrait le label à partir du nom de fichier
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

nb_labels = len(labels)

print("Nombre d'images chargées: {}".format(len(images)))
print("Nombre de labels chargés: {}".format(nb_labels))

# on cree un modele
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dropout(0.5))
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(4, activation='softmax'))

model.summary()

print("Compilation du modèle")
# on compile le modele avec un learning rate adaptatif
opt = optimizers.Adam(learning_rate=0.001)
model.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# on prepare les donnees
images = np.array(images)
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)
labels = to_categorical(labels)
labels = np.array(labels)

split = train_test_split(labels, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split

# on fait de l'augmentation de données pour augmenter la quantité de données d'apprentissage
# on définit les transformations à appliquer
datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    horizontal_flip=True,
    fill_mode="nearest")

# on applique les transformations sur les images
train_generator = datagen.flow(trainImagesX, trainAttrX, batch_size=batch_size)

# on entraine le modele
print("Entrainement du modèle")
history = model.fit(trainImagesX, trainAttrX, epochs=1000, validation_data=(testImagesX, testAttrX))

# on teste l'accuarcy du modele
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(images,  labels, verbose=2)
print(test_acc)

# on sauvegarde le modele avec l'extension ".h5" pour sauvegarder correctement le modèle
model.save("src/ai/modeles/modele_immo.h5")