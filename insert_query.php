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
if (empty($level) || empty($question) || empty($option1) || empty($option2) || empty($option3) || empty($option4) || empty($answer)) {
    echo "Please fill all input fields.";
} else {
    $sql = "INSERT INTO `qa` (`level`, `question`, `option 1`, `option 2`, `option 3`, `option 4`, `answer`)
VALUES ('$level', '$question', '$option1', '$option2', '$option3', '$option4', '$answer')";

if (mysqli_query($conn, $sql)) {
echo "New record created successfully";
} else {
echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
    // Insert data into database or do other form processing here
}



mysqli_close($conn);
?>

