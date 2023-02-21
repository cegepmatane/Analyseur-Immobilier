# `17/02/2023 :`

# Objectif fixé lors de la précédente scrum : <br><br>

Trouver un dataset d'image pour commencer à entrainer un modèle d'ia

## Ce qui a pu être fait et les obstacles :

Utilisation du dataset : https://github.com/emanhamed/Houses-dataset

En tensorflow, on utilise généralement la methode image_dataset_from_directory() pour charger un dataset depuis un
répertoire.
Mais il demande à ce que le répertoire soit déjà trié : il doit contenir des sous-répertoires représentant des labels
et qui contiennent les images correspondantes. Le dataset qu'on utilise utilise les labels directement dans le nom de l'
image.

On doit donc trouver un autre moyen de charger le dataset ou modifier le repertoire.

## Objectif actuel :

Finir de charger le dataset et créer un premier modèle CNN

## Le modèle :

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 198, 198, 32)      896

 max_pooling2d (MaxPooling2D  (None, 99, 99, 32)       0
 )

 conv2d_1 (Conv2D)           (None, 97, 97, 64)        18496

 max_pooling2d_1 (MaxPooling  (None, 48, 48, 64)       0
 2D)

 conv2d_2 (Conv2D)           (None, 46, 46, 64)        36928

 flatten (Flatten)           (None, 135424)            0

 dense (Dense)               (None, 64)                8667200

 dense_1 (Dense)             (None, 4)                 260

=================================================================
Total params: 8,723,780
Trainable params: 8,723,780
Non-trainable params: 0
_________________________________________________________________
```

## Problèmes :

On peut charger le dataset mais lors de la création du modèle et le modèle ne s'entraine pas :

```
Nombre d'images chargées: 2140
Nombre de labels chargés: 4
2023-02-18 00:14:45.553937: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network
 Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #
=================================================================
 conv2d (Conv2D)             (None, 62, 62, 32)        896

 max_pooling2d (MaxPooling2D  (None, 31, 31, 32)       0
 )

 conv2d_1 (Conv2D)           (None, 29, 29, 64)        18496

 max_pooling2d_1 (MaxPooling  (None, 14, 14, 64)       0
 2D)

 conv2d_2 (Conv2D)           (None, 12, 12, 64)        36928

 flatten (Flatten)           (None, 9216)              0

 dense (Dense)               (None, 64)                589888

 dense_1 (Dense)             (None, 4)                 260

=================================================================
Total params: 646,468
Trainable params: 646,468
Non-trainable params: 0
_________________________________________________________________
Compilation du modèle
Entrainement du modèle
Epoch 1/10
Traceback (most recent call last):
  File "c:\wamp64\www\projets-specialises-2023-zhishengtrieu\src\ai\main.py", line 70, in <module>
    model.fit(images, labels, batch_size=batch_size, epochs=10, validation_split=0.2)
  File "C:\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Python\Python310\lib\site-packages\tensorflow\python\eager\execute.py", line 52, in quick_execute
    tensors = pywrap_tfe.TFE_Py_Execute(ctx._handle, device_name, op_name,
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits' defined at (most recent c
all last):
    File "c:\wamp64\www\projets-specialises-2023-zhishengtrieu\src\ai\main.py", line 70, in <module>
      model.fit(images, labels, batch_size=batch_size, epochs=10, validation_split=0.2)
    File "C:\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 65, in error_handler
      return fn(*args, **kwargs)
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1650, in fit
      tmp_logs = self.train_function(iterator)
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1249, in train_function
      return step_function(self, iterator)
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1233, in step_function
      outputs = model.distribute_strategy.run(run_step, args=(data,))
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1222, in run_step
      outputs = model.train_step(data)
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1024, in train_step
      loss = self.compute_loss(x, y, y_pred, sample_weight)
    File "C:\Python\Python310\lib\site-packages\keras\engine\training.py", line 1082, in compute_loss
      return self.compiled_loss(
    File "C:\Python\Python310\lib\site-packages\keras\engine\compile_utils.py", line 265, in __call__
      loss_value = loss_obj(y_t, y_p, sample_weight=sw)
    File "C:\Python\Python310\lib\site-packages\keras\losses.py", line 152, in __call__
      losses = call_fn(y_true, y_pred)
    File "C:\Python\Python310\lib\site-packages\keras\losses.py", line 284, in call
      return ag_fn(y_true, y_pred, **self._fn_kwargs)
    File "C:\Python\Python310\lib\site-packages\keras\losses.py", line 2098, in sparse_categorical_crossentropy
      return backend.sparse_categorical_crossentropy(
    File "C:\Python\Python310\lib\site-packages\keras\backend.py", line 5633, in sparse_categorical_crossentropy
      res = tf.nn.sparse_softmax_cross_entropy_with_logits(
Node: 'sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits'
logits and labels must have the same first dimension, got logits shape [3,4] and labels shape [12]
         [[{{node sparse_categorical_crossentropy/SparseSoftmaxCrossEntropyWithLogits/SparseSoftmaxCrossEntropyWithLogits}}]] [Op:__inference_train_
function_1448]
```

# `21/02/2023 :`

## Objectif actuel :

- Entrainer le modèle sans erreurs
- Faire une prédiction avec le modèle

## Ce qui a été fait :

- Le modèle s'entraine sans erreurs :
  Il suffisait de remplacer `sparse_categorical_crossentropy` par `mean_absolute_percentage_error` dans :
  ```python
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])
  ```

  Cela donne :
  ```
  Nombre d'images chargées: 2140
  Nombre de labels chargés: 4
  2023-02-21 08:30:24.477992: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Libra
  ry (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
  To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
  Model: "sequential"
  _________________________________________________________________
  Layer (type)                Output Shape              Param #
  =================================================================
  conv2d (Conv2D)             (None, 62, 62, 32)        896
  
  max_pooling2d (MaxPooling2D  (None, 31, 31, 32)       0
  )
  
  conv2d_1 (Conv2D)           (None, 29, 29, 64)        18496
  
  max_pooling2d_1 (MaxPooling  (None, 14, 14, 64)       0
  2D)
  
  conv2d_2 (Conv2D)           (None, 12, 12, 64)        36928
  
  flatten (Flatten)           (None, 9216)              0
  
  dense (Dense)               (None, 64)                589888
  
  dense_1 (Dense)             (None, 4)                 260
  
  =================================================================
  Total params: 646,468
  Trainable params: 646,468
  Non-trainable params: 0
  _________________________________________________________________
  Compilation du modèle
  Entrainement du modèle
  Epoch 1/10
  571/571 [==============================] - 12s 20ms/step - loss: 187500032.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 2/10
  571/571 [==============================] - 11s 20ms/step - loss: 187500064.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 3/10
  571/571 [==============================] - 11s 20ms/step - loss: 187500064.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 4/10
  571/571 [==============================] - 11s 20ms/step - loss: 187500096.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 5/10
  571/571 [==============================] - 12s 21ms/step - loss: 187500048.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 6/10
  571/571 [==============================] - 12s 21ms/step - loss: 187500160.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 7/10
  571/571 [==============================] - 13s 23ms/step - loss: 187500176.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 8/10
  571/571 [==============================] - 15s 26ms/step - loss: 187500016.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 9/10
  571/571 [==============================] - 12s 20ms/step - loss: 187500192.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  Epoch 10/10
  571/571 [==============================] - 12s 21ms/step - loss: 187500080.0000 - accuracy: 0.2500 - val_loss: 187499968.0000 - val_accuracy: 0.2500
  ```

## Problèmes :
- Le modèle fait la même prédiction à chaque fois, quelque soit l'image :
  ```
  2023-02-21 08:55:17.935481: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Libra
  ry (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
  To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
  1/1 [==============================] - 0s 114ms/step
  [[0. 0. 1. 0.]]
  ```