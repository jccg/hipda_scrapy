<?php

class Reg {

    private $db;

    private $table = "tlist";

    function __construct(){
        global $db;
        $this->db = $db;
    }

    function GetLastPort(){
        $datas = $this->db->select($this->table,"*",[
            "ORDER" => "uid DESC",
            "LIMIT" => 1
        ]);
        return $datas['0']['port'];
    }

    function Reg($tid ,$head,$uid ,$uname  ,$repcnt ,$readcnt,$ctime  ,$rtime){
        echo "aaaaaaaa";
        $this->db->insert($this->table,[
           "tid" => $tid,
            "head" => $head,
            "uid" => $uid,
            "uname" =>  $uname,
            "repcnt" => $repcnt,
            "readcnt" => $readcnt,
            "ctime" => $ctime,
            "rtime" => $rtime,
            "sptime" => time()
        ]);
    }

}