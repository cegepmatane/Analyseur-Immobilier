import tensorflow as tf


# Convert the model
path = "src/ai/modeles/modele_immo.h5"
converter = tf.lite.TFLiteConverter.from_keras_model(tf.keras.models.load_model(path))
tflite_model = converter.convert()

# Save the model.
with open('src/ai/modeles/modele_immo.tflite', 'wb') as f:
    f.write(tflite_model)
