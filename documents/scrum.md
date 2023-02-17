#17/02/2023 : 

    ###objectif fixé lors de la precedente scrum :
        trouver un dataset d'image pour commencer à entrainer un modele d'ia

    ce qui a pu etre fait et les obstacles :
        utilisation du dataset : 
            https://github.com/emanhamed/Houses-dataset

        En tensorflow on utilise généralement la methode image_dataset_from_directory() pour charger un dataset depuis un repertoire.
        Mais il demande a ce que le repertoire soit déja trié : il doit contenir des sous-repertoires represenant des labels 
        et contient les images correspondantes. Le dataset qu'on utilise met les labels directement dans le nom de l'image
        on doit donc trouver un autre moyen de charger le dataset ou modifier le repertoire.

    ###objectif actuel : 
        finir de charger un dataset et créer un premier modèle CNN


        probleme : 
            on peut charger le dataset mais lors de la creation du modele : 
            ```
            2023-02-17 15:15:03.322420: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network
            Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
            To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
            ```