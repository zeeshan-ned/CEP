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

$sql = "SELECT `level`,`question`, `option 1`, `option 2`, `option 3`, `option 4`,`answer`  FROM `qa` WHERE `level` ='".$level."' ";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        $question = $row["question"];
        $option1 = $row["option 1"];
        $option2 = $row["option 2"];
        $option3 = $row["option 3"];
        $option4 = $row["option 4"];
        $answer = $row["answer"];
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>

<html>
<head>
<title>Update Database</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>

<div class="container">
  <h1 class="text-center">Update Database</h1>

  <form action="update_query.php" method="post" class="form-group">
    <input type="hidden" name="level" value="<?php echo $level; ?>">
    <div class="form-group">
      <label for="question">Question:</label>
      <input type="text" id="question" name="question" value="<?php echo $question; ?>" class="form-control">
    </div>
    <div class="form-group">
      <label for="option1">Option 1:</label>
      <input type="text" id="option1" name="option1" value="<?php echo $option1; ?>" class="form-control">
    </div>
    <div class="form-group">
      <label for="option2">Option 2:</label>
      <input type="text" id="option2" name="option2" value="<?php echo $option2; ?>" class="form-control">
    </div>
    <div class="form-group">
    
      <label for="option3">Option 3:</label>
      <input type="text" id="option3" name="option3" value="<?php echo $option3; ?>" class="form-control">
    </div>
    <div class="form-group">
      <label for="option4">Option 4:</label>
      <input type="text" id="option4" name="option4" value="<?php echo $option4; ?>" class="form-control">
    </div>
    <div class="form-group">
      <label for="answer">Answer:</label>
      <input type="text" id="answer" name="answer" value="<?php echo $answer; ?>" class="form-control">
    </div>
    <div class="form-group text-center">
      <input type="submit" value="Update" class="btn btn-primary">
    </div>
  </form>
</div>


<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
