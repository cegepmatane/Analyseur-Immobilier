<?php
declare(strict_types=1);
class Loader{
    public static function header(){
        echo file_get_contents("src/web/template/header");
    }

    public static function footer(){
        echo file_get_contents("src/web/template/footer");
    }

    public static function contact(){
        echo file_get_contents("src/web/template/contact");
    }
    
}