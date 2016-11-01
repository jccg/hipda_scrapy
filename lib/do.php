<?php
/*
 * 下面别修改
 */
//medoo

//Define DB Table Name
$db_table['user'] = "user";

//set timezone
date_default_timezone_set('PRC');

$db_host = getenv('MYSQL_PORT_3306_TCP_ADDR');
$db_user_name = getenv('MYSQL_USERNAME');
$db_pass = getenv('MYSQL_PASSWORD');
$db_name = getenv('MYSQL_INSTANCE_NAME');
$db_port = getenv('MYSQL_PORT_3306_TCP_PORT');


//Using Mysqli
$dbc = new mysqli($db_host,$db_user_name,$db_pass,$db_name);
$db_char = 'utf8';
$dbc->query("SET NAMES utf8");
$dbc->query("SET time_zone = '+8:00'");

//$dbinfo
$dbInfo['database_type'] = 'mysql';
$dbInfo['database_name'] = $db_name;
$dbInfo['server'] = $db_host;
$dbInfo['username'] = $db_user_name;
$dbInfo['password'] = $db_pass;
$dbInfo['charset'] = 'utf8';

//Define system Path
$ss_path = __DIR__;
$ss_path = substr($ss_path,0,strlen($ss_path)-4);
define('SS_PATH',$ss_path);
//autoload class
spl_autoload_register('autoload');
function autoload($class){
    require_once SS_PATH.'/lib/'.str_replace('\\','/',$class).'.php';
}

//Define system Pat
require_once 'medoo.php';
$db = new medoo([
    // required
    'database_type' => 'mysql',
    'database_name' => $db_name,
    'server' => $db_host,
    'username' => $db_user_name,
    'password' => $db_pass,
    'charset' => 'utf8',

    // optional
    'port' => $db_port,
    // driver_option for connection, read more from http://www.php.net/manual/en/pdo.setattribute.php
    'option' => [
        PDO::ATTR_CASE => PDO::CASE_NATURAL
    ]
]);
