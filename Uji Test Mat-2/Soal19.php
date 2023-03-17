<?php
session_start();

if (isset($_SESSION['email'])) {
    header('Location: Soal19plus.php');
    exit;
}

if (isset($_POST['submit'])) {
    $email = $_POST['email'];

    if ($email === 'arpan@gmail.com' && $pass === 'arpan123') {
        header('Location: Soal19plus.php');
        exit;
    }
}
?>

<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <form method="post">
        <label>Username</label>
        <input type="text" name="email"><br>
        <label>Password</label>
        <input type="password" name="pass"><br>
        <input type="submit" name="submit" value="Login">
    </form>
</body>
</html>
