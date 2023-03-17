<?php 
require 'Soal16.php';

$data = mysqli_query($con,"select * from barang");

while ($r = mysqli_fetch_array($data)) {
    $a = $r['barang1'];
    $b = $r['barang2'];
    $c = $r['barang3'];

    echo "<br>";
    echo $a;
    echo "<br>";
    echo $b;
    echo "<br>";
    echo $c;

    echo "<a href='Soal18.php'>Hapus</a>";
}

?>