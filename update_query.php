<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "quiz game";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$level = $_POST['level'];
$question = $_POST['question'];
$option1 = $_POST['option1'];
$option2 = $_POST['option2'];
$option3 = $_POST['option3'];
$option4 = $_POST['option4'];
$answer = $_POST['answer'];

$sql = "UPDATE `qa` SET `question`='$question',`option 1`='$option1',`option 2`='$option2',`option 3`='$option3',`option 4`='$option4',`answer`='$answer' WHERE `level`='$level'";

if (mysqli_query($conn, $sql)) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . mysqli_error($conn);
}

mysqli_close($conn);
