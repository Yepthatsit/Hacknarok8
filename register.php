<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $servername = "mysql.agh.edu.pl"; 
    $username = "tpotera"; 
    $password = "wTbnZbjMVJLfCAnh"; 
    $dbname = "tpotera"; 
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error) {
        $error = "Błąd połączenia z bazą danych: " . $conn->connect_error;
    }
    if (empty($error) && $_SERVER["REQUEST_METHOD"] == "POST"){
    $username = mysqli_real_escape_string($conn, $_POST['username']);
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $password = mysqli_real_escape_string($conn, $_POST['password']);
    $adres = mysqli_real_escape_string($conn, $_POST['adress']);
    $sql = "INSERT INTO users (username, password) VALUES ('$username', '$email', '$password', '$adres')";
    if ($conn->query($sql) === TRUE) {
        header("Location: login.php");
        exit();
    } else {
        $error = "Błąd podczas rejestracji: " . $conn->error;
    }
    $conn->close();
}
}
?>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zarejestruj się</title>
    <link rel="stylesheet" href="styles.css" />
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="wrapper">
    <?php if(isset($error)) echo "<p style='color: red;'>$error</p>"; ?>
        <form action="register.php" method="post">
            <h1>Zostań wikingiem!</h1>
            <h2>Nazwa Użytkownika</h2>
            <div class="input_login">
                <input type="text" id="username" name="username" placeholder="Username" required>
                <i class='bx bxs-user-circle'></i>
            </div>
            <h2>Adres e-mail</h2>
            <div class="input_login">
                <input type="text" id="email" name="email" placeholder="Email" required>
            </div>
            <h2>Hasło</h2>
            <div class="input_password">
                <input type="password" id="password" name="password" placeholder="Password" required>
                <i class='bx bxs-lock'></i>
            </div>
            <h2>Adres</h2>
            <div class="input_login">
                <input type="text" id="adress" name="adres" placeholder="Adres" required>
            </div>
            <input type="submit" value="Zrejestruj" class="btn">
        </form>
        <div class="register_link">
            <p>Należysz do społeczności wikingów?<a href="login.php"><br>Zaloguj się </a></p>
            <p>Nie chcesz zakładać konta? <a href="index.php"><br>Kontynuuj bez logowania</a>.</p>
        </div>
    </div>
</body>
</html>