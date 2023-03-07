from tensorflow.keras import layers, models, optimizers
import matplotlib.pyplot as plt
import cv2


class ModelConfig:
    """
    Classe qui contient les paramètres du modèle
    """
    # on fait des constantes pour les paramètres du modèle
    IMG_HEIGHT = 64
    IMG_WIDTH = 64
    BATCH_SIZE = 32
    EPOCHS = 100
    LABELS = ["bathroom", "bedroom", "frontal", "kitchen"]
    EXTENSION = ["jpg", "jpeg", "png", "gif"]
    OPTIMIZER = optimizers.Adam(learning_rate=0.001)
    MODEL = models.load_model("src/ai/modeles/modele_immo.h5")

    @staticmethod
    def cnn_model():
        """
        Fonction qui crée et retourne un modèle CNN
        """
        m = models.Sequential()
        m.add(layers.Conv2D(32, (3, 3), activation='relu',
                            input_shape=(ModelConfig.IMG_HEIGHT, ModelConfig.IMG_WIDTH, 3)))
        m.add(layers.MaxPooling2D((2, 2)))
        m.add(layers.Conv2D(64, (3, 3), activation='relu'))
        m.add(layers.MaxPooling2D((2, 2)))
        m.add(layers.Conv2D(128, (3, 3), activation='relu'))
        m.add(layers.MaxPooling2D((2, 2)))
        m.add(layers.Conv2D(256, (3, 3), activation='relu'))
        m.add(layers.MaxPooling2D((2, 2)))
        m.add(layers.Flatten())
        m.add(layers.Dropout(0.5))
        m.add(layers.Dense(128, activation='relu'))
        m.add(layers.Dense(4, activation='softmax'))
        return m

    @staticmethod
    def img_to_predict(image_path: str):
        """
        Fonction qui charge une image et la redimensionne pour la prédiction
        """
        # on charge l'image
        image_to_predict = cv2.imread(image_path, cv2.IMREAD_COLOR)
        plt.imshow(cv2.cvtColor(image_to_predict, cv2.COLOR_BGR2RGB))

        # on redimensionne l'image
        image_to_predict = cv2.resize(image_to_predict, (ModelConfig.IMG_HEIGHT, ModelConfig.IMG_WIDTH))
        image_to_predict = image_to_predict.reshape(1, ModelConfig.IMG_HEIGHT, ModelConfig.IMG_WIDTH, 3)
        return image_to_predict
