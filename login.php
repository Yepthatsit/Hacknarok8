<?php
session_start();
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $servername = "mysql.agh.edu.pl";
    $username = "tpotera";
    $password = "wTbnZbjMVJLfCAnh";
    $dbname = "tpotera";
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        $error = "Błąd połączenia z bazą danych!";
    }
    if (empty($error) && $_SERVER["REQUEST_METHOD"] == "POST") {
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);
    $sql = "SELECT id FROM users WHERE username='$username' AND password='$password'";
    $result = $conn->query($sql);
    if ($result->num_rows == 1) {
        $_SESSION['username'] = $username;
        header("Location: index.php");
        exit();
    } else {
        $error = "Błędne dane logowania!";
    }
    $conn->close();
}
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="styles.css" />
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="wrapper">
        <form action="login.php" method="post">
        <?php if(isset($error)) echo "<p style='color: red;'>$error</p>"; ?>
        <h1>Zaloguj się</h1>
        <h2>Login</h2>
            <div class="input_login">
                <input type="text" id="username" name="username" placeholder="Username" required>
                <i class='bx bxs-user-circle'></i>
            </div>
            <h2>Hasło</h2>
            <div class="input_password">
                <input type="password" id="password" name="password" placeholder="Password" required>
                <i class='bx bxs-lock'></i>
            </div>  
            <input type="submit" value="Zaloguj" class="btn">
        </form>
        <div class="register_link">
            <p>Nie należysz do społeczności wikingów?<a href="register.php"><br>Zarejestruj się </a></p>
            <p>Nie chcesz zakładać konta? <a href="index.php"><br>Kontynuuj bez logowania</a>.</p>
        </div>
    </div>

</body>
</html>