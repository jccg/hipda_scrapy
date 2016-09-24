<?php
//定义流量
$tokb = 1024;
$tomb = 1024*1024;
$togb = $tomb*1024;
//Define DB Connection  数据库信息
define('DB_HOST','localhost');
define('DB_USER','xxxxxxxxxx');
define('DB_PWD','xxxxxxxxx');
define('DB_DBNAME','sp_hipda');
define('DB_CHARSET','utf8');
define('DB_TYPE','mysql'); 
/*
 * 下面的东西根据需求修改
 */

//name
$site_name = "";
$site_url  = "https://panel.com/";

//
require_once 'do.php';
