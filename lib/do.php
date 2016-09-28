<?php
/*
 * 下面别修改
 */
//medoo

//Define DB Table Name
$db_table['user'] = "user";

//set timezone
date_default_timezone_set('PRC');

//Using Mysqli
$dbc = new mysqli(DB_HOST,DB_USER,DB_PWD,DB_DBNAME);
$db_char = DB_CHARSET;
$dbc->query("SET NAMES utf8");
$dbc->query("SET time_zone = '+8:00'");

//$dbinfo
$dbInfo['database_type'] = DB_TYPE;
$dbInfo['database_name'] = DB_DBNAME;
$dbInfo['server'] = DB_HOST;
$dbInfo['username'] = DB_USER;
$dbInfo['password'] = DB_PWD;
$dbInfo['charset'] = DB_CHARSET;



//Define system Pat
require_once 'medoo.php';
$db = new medoo([
    // required
    'database_type' => DB_TYPE,
    'database_name' => DB_DBNAME,
    'server' => DB_HOST,
    'username' => DB_USER,
    'password' => DB_PWD,
    'charset' => DB_CHARSET,

    // optional
    'port' => 3306,
    // driver_option for connection, read more from http://www.php.net/manual/en/pdo.setattribute.php
    'option' => [
        PDO::ATTR_CASE => PDO::CASE_NATURAL
    ]
]);
