<?php
declare(strict_types=1);
require_once("classes/Loader.php");

Loader::header();

$prix = 0.0;

//les formulaires
//on commence a charger des images
echo <<<HTML
<h1>Votre projet</h1>
<p>Choisissez des images</p>
<p>Format: .jpeg, .jpg, .png, .gif</p>
<form action="index.php" method="post" enctype="multipart/form-data">
    <input type="file" name="files" multiple>
    <input type="submit" value="Suivant">
</form>

<h1>Quelle est l'adresse du bien à estimer ?</h1>
<p>(Facultatif)</p>
<form action="index.php" method="post">
    <input type="text" name="address" placeholder="Quelle est l’adresse du bien dont vous souhaitez estimer le loyer ?">
    <input type="submit" value="Suivant">
</form>

<h1>Détails</h1>
<p>(Facultatif)</p>
<form action="index.php" method="post">
    <input type="text" name="surface" placeholder="Quelle est la surface du bien ?">
    <input type="text" name="rooms" placeholder="Combien de pièces ?">
    <input type="text" name="floor" placeholder="Quel étage ?">
    <input type="submit" value="Suivant">
</form>

<h1>Annexes</h1>
<p>(Facultatif)</p>
<form action="index.php" method="post">
    <input type="text" name="parking" placeholder="Quel type de parking ?">
    <input type="text" name="balcony" placeholder="Quel type de balcon ?">
    <input type="text" name="terrace" placeholder="Quel type de terrasse ?">
    <input type="submit" value="Suivant">
</form>

<h1>Etat</h1>
<p>(Facultatif)</p>
<form action="index.php" method="post">
    <select name="" id="">
        <option value="1">Neuf</option>
        <option value="2">Bon</option>
        <option value="3">Moyen</option>
        <option value="4">Mauvais</option>
    </select>
    <input type="submit" value="Suivant">
</form>

<h1>Votre estimation</h1>
<p>Votre bien est estimé à : $prix €</p>

HTML;

?>