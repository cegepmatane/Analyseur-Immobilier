<?php
declare(strict_types=1);
require_once("src/web/classes/Loader.php");

Loader::header();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    /*$address = $_POST['address'];
    $surface = $_POST['surface'];
    $rooms = $_POST['rooms'];
    $floor = $_POST['floor'];
    $parking = $_POST['parking'];
    $balcony = $_POST['balcony'];
    $terrace = $_POST['terrace'];*/

    //on uplaod les images dans le dossier uploads
    $targetDir = "uploads/"; 
    $error=array();
    $files = $_FILES['files'];
    $allowed = array('png', 'jpg', 'gif','jpeg');
    foreach($_FILES["files"]["tmp_name"] as $key=>$tmp_name) {
        $file_name=$_FILES["files"]["name"][$key];
        $file_tmp=$_FILES["files"]["tmp_name"][$key];
        $filename = uniqid();
        $ext=pathinfo($file_name,PATHINFO_EXTENSION);
    
        if(in_array($ext,$allowed)) {
            move_uploaded_file($file_tmp=$_FILES["files"]["tmp_name"][$key], $targetDir.$filename.".".$ext);
        }
        else {
            array_push($error,"$file_name, ");
        }
    }

    echo "<h1>Votre estimation</h1>";

    //si dossier uploads n'est pas vide
    if (count(glob("uploads/*")) > 0) {
        //on trouve l'executabe de python
        $exec = "C:/Python/Python310/python.exe";
        //on utilise le script python
        $command = escapeshellcmd("$exec src/ai/analyse.py");
        echo shell_exec($command);

        $prix = 0.0;
    
        echo "<p>Votre bien est estimé à : $prix €</p>";
    }else{
        echo "Aucune image n'a été uploadée";
    }
    
}else{

    //les formulaires
    //on commence a charger des images
    echo <<<HTML
        <h1>Votre projet</h1>
        <p>Choisissez des images</p>
        <p>Format: .jpeg, .jpg, .png, .gif</p>
        <form action="index.php" method="post" enctype="multipart/form-data">
            <input type="file" name="files[]" multiple>

            
            <br><br>
            <input type="submit" value="Estimer">
        </form>
    HTML;

    /*
    <h1>Quelle est l'adresse du bien à estimer ?</h1>
            <p>(Facultatif)</p>
            <input type="text" name="address" placeholder="Quelle est l’adresse du bien dont vous souhaitez estimer le loyer ?">
                

            <h1>Détails</h1>
            <p>(Facultatif)</p>
            <input type="text" name="surface" placeholder="Quelle est la surface du bien ?"><br>
            <input type="text" name="rooms" placeholder="Combien de pièces ?"><br>
            <input type="text" name="floor" placeholder="Quel étage ?"><br>

            <h1>Annexes</h1>
            <p>(Facultatif)</p>
            <input type="text" name="parking" placeholder="Quel type de parking ?"><br>
            <input type="text" name="balcony" placeholder="Quel type de balcon ?"><br>
            <input type="text" name="terrace" placeholder="Quel type de terrasse ?"><br>

            <h1>Etat</h1>
            <p>(Facultatif)</p>
            <select name="" id="">
                <option value="1">Neuf</option>
                <option value="2">Bon</option>
                <option value="3">Moyen</option>
                <option value="4">Mauvais</option>
            </select>
     */
}


?>