<?php 
$pw = (string)($_GET['pw'] ?? '');
$id = (string)($_GET['id'] ?? '');
if (!ctype_digit($id) || strlen($id) !== 8 || !ctype_digit($pw) || strlen($pw) !== 6) {
 exit;
}
print passthru('python Ecust_PingJiao.py '.$id.'x'.$pw);
?>
