<?php
//引入配置文件
require_once './lib/config.php';
$num  = $_POST['code_num'];
$uid  = $_POST['uid'];

if( $num == null || strlen($num) >33 || strlen($num) <10  ){
    echo ' <script>alert("充值码错误!")</script> ';
    exit();
}


echo ' <script>alert("'.  $num  .   $uid   .'添加成功!")</script> ';
