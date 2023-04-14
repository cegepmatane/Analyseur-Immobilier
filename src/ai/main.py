import cv2
import glob
import numpy as np
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from ModelConfig import ModelConfig

# on charge les images du dataset
data_dir = "dataset/"
image_paths = sorted(glob.glob(data_dir + "*_*.*"))

images = []
labels = []

for image_path in image_paths:
    # on extrait le label à partir du nom de fichier
    label, extension = image_path.split("_")[-1].split(".")

    # on vérifie que l'image est bien au format jpg/jpeg/png/gif
    if extension in ModelConfig.EXTENSION:
        # on charge l'image
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # on redimensionne l'image
        image = cv2.resize(image, (ModelConfig.IMG_HEIGHT, ModelConfig.IMG_WIDTH))

        # on ajoute l'image et le label dans la liste
        images.append(image)
        labels.append(label)

nb_labels = len(labels)

print("Nombre d'images chargées: {}".format(len(images)))
print("Nombre de labels chargés: {}".format(nb_labels))

# on cree un modèle
model = ModelConfig.cnn_model()

model.summary()

print("Compilation du modèle")
# on compile le modèle avec un learning rate adaptatif
model.compile(optimizer=ModelConfig.OPTIMIZER,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# on prépare les donnees
images = np.array(images)
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(labels)
labels = to_categorical(labels)
labels = np.array(labels)

split = train_test_split(labels, images, test_size=0.25, random_state=42)
(trainAttrX, testAttrX, trainImagesX, testImagesX) = split

# on fait de l'augmentation de données pour augmenter la quantité de données d'apprentissage,
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
train_generator = datagen.flow(trainImagesX, trainAttrX, batch_size=ModelConfig.BATCH_SIZE)

# on entraine le modele
print("Entrainement du modèle")
history = model.fit(trainImagesX, trainAttrX, epochs=ModelConfig.EPOCHS, validation_data=(testImagesX, testAttrX))

# on teste l'accuarcy du modele
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')   

test_loss, test_acc = model.evaluate(images, labels, verbose=2)
print(test_acc)

# on sauvegarde le modèle avec l'extension ".h5" pour sauvegarder correctement le modèle
model.save("src/ai/modeles/modele_immo.h5")
