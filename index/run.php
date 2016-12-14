<?php 
$pw = $_GET['pw'];
$id = $_GET['id'];
print passthru('python Ecust_PingJiao.py '.$id.'x'.$pw);
?>