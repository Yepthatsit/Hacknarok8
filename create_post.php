    <?php
    session_start();
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sprawdzenie czy dane zostały przesłane
    if (empty($_POST['content'])) {
        $error = "Treść wpisu jest wymagana.";
    } else {
        // Połączenie z bazą danych
        $servername = "mysql.agh.edu.pl";
        $username = "tpotera";
        $password = "wTbnZbjMVJLfCAnh";
        $dbname = "tpotera";

        $conn = new mysqli($servername, $username, $password, $dbname);
        if ($conn->connect_error) {
            die("Błąd połączenia z bazą danych: " . $conn->connect_error);
        }

        // Przygotowanie danych do wstawienia do bazy danych
        $content = mysqli_real_escape_string($conn, $_POST['content']);
        $location = mysqli_real_escape_string($conn, $_POST['location']);


 // Obsługa przesyłania zdjęć
        $images = "";
        if(isset($_FILES['images'])) {
            $target_dir = "uploads/";
            $target_file = $target_dir . basename($_FILES["images"]["name"]);
            if (move_uploaded_file($_FILES["images"]["tmp_name"], $target_file)) {
                $images = $target_file;
            } else {
                $error = "Błąd podczas przesyłania zdjęcia.";
            }
        }


        $sql = "INSERT INTO posts (user_id, location, content, images) VALUES (1, '$location', '$content', '$images')";
        if ($conn->query($sql) === TRUE) {
            header("Location: index.php");
            exit();
        } else {
            $error = "Błąd podczas dodawania wpisu: " . $conn->error;
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
    <title>Nowy Wpis</title>
    <script src="script.js" defer></script>
</head>
<body>
<section class="post-container">
				<b>Napisz post:</b>
				<br></br>
				<form id="postForm">
					<input type="text" id="postContent" required></input>
					<div id="dropArea" 
						ondragover="event.preventDefault()"
						ondragenter="event.target.classList.add('highlight')"
						ondragleave="event.target.classList.remove('highlight')"
						ondrop="dropHandler(event)">
						Upuść obraz tutaj
					</div>
					<div id="imageContainer">
						<img id="droppedImage" src="#" alt="Wybrany obraz" style=" width: 20%; float: left" >
					</div>
					<div style="clear: both;"></div>
					<button type="submit">Opublikuj</button>
				</form>

			</section>

<script>
    function dropHandler(event) {
  event.preventDefault();

  if (event.dataTransfer.items) {
      for (var i = 0; i < event.dataTransfer.items.length; i++) {
          if (event.dataTransfer.items[i].kind === 'file') {
              var file = event.dataTransfer.items[i].getAsFile();
              var reader = new FileReader();
              reader.onload = function(event) {
                  var img = document.getElementById('droppedImage');
                  img.src = event.target.result;
                  img.style.display = 'block';
              };
              reader.readAsDataURL(file);
          }
      }
  }
}

</body>
</html>
