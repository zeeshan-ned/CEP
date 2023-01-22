<html>
<head>
    <title>Update/Delete Database</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head>
<body>

<div class="container">
    <h1 class="text-center my-4">Update/Delete Database</h1>

    <table class="table table-bordered">
    <thead>
        <tr>
            <th>Level</th>
            <th>Question</th>
            <th>Option 1</th>
            <th>Option 2</th>
            <th>Option 3</th>
            <th>Option 4</th>
            <th>Answer</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
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

$sql = "SELECT `level`,`question`, `option 1`, `option 2`, `option 3`, `option 4`,`answer`  FROM `qa`";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "<tr>
        <td>" . $row["level"]. "</td>
        <td>" . $row["question"]. "</td>
        <td>" . $row["option 1"]. "</td>
        <td>" . $row["option 2"]. "</td>
        <td>" . $row["option 3"]. "</td>
        <td>" . $row["option 4"]. "</td>
        <td>" . $row["answer"]. "</td>
        <td><a href='update.php?id=".$row['level']."'>Update</a></td>
        <td><a href='delete.php?id=".$row['level']."'>Delete</a></td>
        <td><a href='insert.php?id=".$row['level']."'>Insert</a></td>
        </tr>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>

</table>

</body>
</html>
