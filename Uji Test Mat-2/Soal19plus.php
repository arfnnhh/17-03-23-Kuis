<?php
session_start();

if (!isset($_SESSION['email'])) {
    header('Location: Soal19.php');
    exit;
}

$email = $_SESSION['email'];

?>


<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <p>Email:<?php echo $email; ?></p>
</body>
</html>
