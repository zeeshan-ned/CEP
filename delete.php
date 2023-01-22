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

$level = $_GET['id'];

$sql = "DELETE FROM `qa` WHERE `level` ='".$level."'";

if (mysqli_query($conn, $sql)) {
    echo "Record deleted successfully";
} else {
    echo "Error deleting record: " . mysqli_error($conn);
}

mysqli_close($conn);
?>
