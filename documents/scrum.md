# `17/02/2023 :` 

# Objectif fixé lors de la précedente scrum : <br><br>

Trouver un dataset d'image pour commencer à entrainer un modèle d'ia

## Ce qui a pu être fait et les obstacles :

Utilisation du dataset : https://github.com/emanhamed/Houses-dataset

En tensorflow, on utilise généralement la methode image_dataset_from_directory() pour charger un dataset depuis un repertoire.
Mais il demande à ce que le répertoire soit déjà trié : il doit contenir des sous-répertoires représenant des labels 
et qui contiennent les images correspondantes. Le dataset qu'on utilise utilise les labels directement dans le nom de l'image.

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

## Problème : 
On peut charger le dataset mais lors de la création du modèle : 
```
2023-02-17 15:15:03.322420: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network
Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
```
et le modèle ne s'entraine pas :

```
Traceback (most recent call last):
  File "c:\wamp64\www\projets-specialises-2023-zhishengtrieu\src\ai\main.py", line 91, in <module>
    model.fit(images, labels, epochs=10)
  File "C:\Python\Python310\lib\site-packages\keras\utils\traceback_utils.py", line 70, in error_handler
    raise e.with_traceback(filtered_tb) from None
  File "C:\Python\Python310\lib\site-packages\keras\engine\data_adapter.py", line 1848, in _check_data_cardinality
    raise ValueError(msg)
ValueError: Data cardinality is ambiguous:
  x sizes: 2140
  y sizes: 4
Make sure all arrays contain the same number of samples.
```