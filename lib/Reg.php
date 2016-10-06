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

    //根据用户名返回UID
    function get_info_by_tid($tid){
     $datas = $this->db->select($this->table,"*", [
             "tid" => $tid
     ]);
     return $datas[0];
    }
    
    function Reg($tid ,$head,$uid ,$uname  ,$repcnt ,$readcnt,$ctime  ,$rtime, $page){
        #    insert
        $this->db->rinsert($this->table,[
           "tid" => $tid,
            "head" => $head,
            "uid" => $uid,
            "uname" =>  $uname,
            "repcnt" => $repcnt,
            "readcnt" => $readcnt,
            "ctime" => $ctime,
            "rtime" => $rtime,
            "sptime" => time(),
            "page" => $page
        ]);
    }
    
       
    function uppage($page){
        #    insert
        $this->db->update("nowproc",[
           "procvalue" => $page
        ],
        ["prockey"=> "page"]);
    }

}