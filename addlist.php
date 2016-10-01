<?php
//引入配置文件
require_once './lib/config.php';
$tid  = $_POST['tid'];
$head  = $_POST['head'];
$uid  = $_POST['uid'];
$uname  = $_POST['uname'];
$repcnt  = $_POST['repcnt'];
$readcnt  = $_POST['readcnt'];
$ctime  = $_POST['ctime'];
$rtime  = $_POST['rtime'];




$c = new \Reg();

$c->Reg($tid ,$head,$uid ,$uname  ,$repcnt ,$readcnt,$ctime  ,$rtime);

#if( $num == null || strlen($num) >33 || strlen($num) <10  ){
#    echo ' <script>alert("充值码错误!")</script> ';
#    exit();
#}


echo ' <script>alert("'.  $num  .   $uid   .'添加成功!")</script> ';
