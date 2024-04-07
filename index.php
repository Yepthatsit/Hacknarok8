<?php
session_start();
$username = $_SESSION['username'];
?>

<!DOCTYPE html>
<html lang="pl">
<head>

    <meta charset="utf-8">
    <title>Wiking Wędkarz</title>
    <meta name="description" content="Witaj Wikingu spragniony wędkarski przygód!">
    <meta name="keywords" content="wiking, wędki, ryby, przerębel">
    
    
    <meta http-equiv="X-Ua-Compatible" content="IE=edge,chrome=1">
    
    <link rel="stylesheet" type="text/css" href="styles_main.css">
	<link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <link href="https://fonts.googleapis.com/css2?family=Lato&family=Raleway:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
	<script src="script.js" defer></script>
</head>

<body>
    <header>
        <h1 class="logo">Witaj Wikingu, w świecie łowisk</h1>
    </header>
	<!---<script>
            function submitForm() {
                const formData = new FormData(document.getElementById('myForm'));
                fetch('http://localhost:5000/submit', {  // Change this to your Flask server URL
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
					console.log(data)
                    //alert(data['rating']);
					// fetch('',
					// {
					// 	method: "POST",
					// 	body: data
					// }).then(response => response.json()).then(data => {
					// })})
				});}
    </script> -->

    <div id="content">
        

        
        <article id="home" data-tab-content>
			<form id="myForm">
				<input type="text" id="szukaj" name="szukaj" placeholder="Szukaj" autocomplete="off">
				<button type="button" onclick="submitForm()">Szukaj</button>
			</form>
			<section class="opis">
				<b>Zdjęcia łowiska</b>
                <iframe width=100%></iframe>
			</section>
			<section class="opis1" id = 'pogoda'>
				<b>Pogoda</b>
                <iframe width=100%></iframe>
			</section>
			<div style="clear: both;"></div>
			<section class="opis" id = 'opinie'>
				<b>Opinie</b>
                <iframe width=100%></iframe>
			</section>
			<section class="opis1" width=100% height="300px">
			<span id = 'pogoda1'> </span>
			</section>
			<div style="clear: both;"></div>
		</article>

		<article id="tutorials" data-tab-content>

<form id="myForm1">
    <input type="text" id="zapytaj" name="zapytaj1" placeholder="zapytaj" autocomplete="off">
    <button type="button" onclick="askgjepete()" id="zapytajguzik" style="position: relative;
	border-radius: 10px;
	width: 30%;
	padding-top: 5px;
	padding-bottom: 5px;
	padding-left:5px;
	">Zapytaj</button>
</form>
<script>
    function askgjepete() {
        const formData = new FormData(document.getElementById('myForm1'));
		alert("Proszę zaczekać na odpowiedź")
        fetch('http://localhost:5000/chatask', {  // Change this to your Flask server URL
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById('response').innerHTML = "Rada: " + data['response']; // Corrected concatenation
        })
        .catch(error => {
            console.error('Błąd:', error);
        });
    }
</script>
				</form>	
			<section class="tutorials-container" style="color: black;" id="response">
				- Czemu łowisz ryby na ser, a nie na robaki? - pyta Franek Kowalskiego.<br></br>
				- Bo jak ryba weźmie, mam na kolację rybę, a jak nie weźmie, to mam ser.
			</section>
		</article>

		<article id="posts" data-tab-content>
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
	

</section>


			</section>
		</article>

		<article id="profile" data-tab-content>
			
			<section class="profile-container">
				<b>Twój profil</b>
				<img src="logouser.png" alt="Profile Picture" class="profile-picture">
				<h1 class="profile-name">Kasia z Bolta</h1>
				<ul class="profile-details">
				<li><strong>E-mail:</strong> kasiazbolta.bolt.pl</li>
				<li><strong>Miejsce zamieszkania:</strong> Kraków, Polska</li>
				<li><strong>Data dołączenia:</strong> January 1, 2020</li>
				</ul>
			</section>
		</article>

		<nav>
			Menu
			<button data-tab-target="#home" type="button" class="start_button">Home
				<i class='bx bxs-home'></i>
			</button>
			
			<button data-tab-target="#tutorials" type="button" value="tutorial_button">Poradniki
				<i class='bx bx-book-reader'></i>
			</button>

			<?php if(!isset($_SESSION['username'])) { ?>
                <a href="login.php"><button type="button">Zaloguj się<i class='bx bxs-user-circle'></i></button></a>
            <?php } else {?>
                <a href="logout.php"><button type="button">Wyloguj się<i class='bx bxs-user-circle'></i></button></a>
            <?php } ?>
			<?php if(isset($_SESSION['username'])) { ?>
			<button data-tab-target="#posts" type="button" class="post_button">Utwórz
				<i class='bx bxs-message-alt-add'></i>
			</button>

			<button data-tab-target="#profile" type="button" class="profile_button">Profil
				<i class='bx bxs-user-account'></i>
			</button>
			<?php } ?>
		</nav>

		<div style="clear: both;"></div>

	</div>

	<footer>
		<div>
			Wszelkie prawa zastrzeżone &copy; 2024 Dziękujęmy za wizytę!
		</div>
	</footer>



</body>
<script>
            function submitForm() {
                const formData = new FormData(document.getElementById('myForm'));
                fetch('http://localhost:5000/submit', {  // Change this to your Flask server URL
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
					console.log(data)
					document.getElementById('pogoda1').innerHTML ="ocena: " +data['rating'] +"/5 " + "na podstawie " + data['total'] +" opinii";
					document.getElementById('opinie').innerHTML = "Opinie:\ " + data['reviews'][0]['text'];
					document.getElementById('pogoda').innerHTML = "Pogoda:\ " + 
					' Ciśnienie: ' + data['weatherinfo']['pressure'] + 
					" Kierunek wiatru: " + data['weatherinfo']['winddir'] + 
					" Prędkość wiatru(km/h) " + data['weatherinfo']['windkmph'] +
					" Temperatura: " + data['weatherinfo']['temp'] + 
					" St. zachmurzenia" + data['weatherinfo']['clouds'] 
					
			});
			}
    </script>
</html>