<?php
 $servername = "mysql.agh.edu.pl";
 $username = "tpotera";
 $password = "wTbnZbjMVJLfCAnh";
 $dbname = "tpotera";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Błąd połączenia z bazą danych: " . $conn->connect_error);
}

$sql = "SELECT * FROM posts";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "<div class='post'>";
        echo "<p><strong>ID:</strong> " . $row["id"]. "</p>";
        echo "<p><strong>User ID:</strong> " . $row["user_id"]. "</p>";
        echo "<p><strong>Treść:</strong> " . $row["content"]. "</p>";
        echo "</div>";
    }
} else {
    echo "Brak postów do wyświetlenia.";
}

$conn->close();
?>
