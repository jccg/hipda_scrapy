<?php
//引入配置文件
require_once './lib/config.php';
//$tid  = $_POST['tid'];
$spid = $_POST['spid'];
$page = $_POST['page'];


$c = new \Reg();

$c->uppage($spid, $page);

#if( $num == null || strlen($num) >33 || strlen($num) <10  ){
#    echo ' <script>alert("充值码错误!")</script> ';
#    exit();
#}


echo ' <script>alert("'.   $page   .'添加成功!")</script> ';
