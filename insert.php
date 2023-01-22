
<!DOCTYPE html>
<html>
<head>
    <title>Insert Quiz Question</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
</head>
<body>
    <div class="container">
        <h1 class="text-center">Insert Quiz Question</h1>
        <form action="insert_query.php" method="post" class="form-group" name="quizForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="level">Level:</label>
                <input type="text" id="level" name="level" class="form-control">
            </div>
            <div class="form-group">
                <label for="question">Question:</label>
                <input type="text" id="question" name="question" class="form-control">
            </div>
            <div class="form-group">
                <label for="option1">Option 1:</label>
                <input type="text" id="option1" name="option1" class="form-control">
            </div>
            <div class="form-group">
                <label for="option2">Option 2:</label>
                <input type="text" id="option2" name="option2" class="form-control">
            </div>
            <div class="form-group">
                <label for="option3">Option 3:</label>
                <input type="text" id="option3" name="option3" class="form-control">
            </div>
            <div class="form-group">
                <label for="option4">Option 4:</label>
                <input type="text" id="option4" name="option4" class="form-control">
            </div>
            <div class="form-group">
                <label for="answer">Answer:</label>
                <input type="text" id="answer" name="answer" class="form-control">
            </div>
            <div class="form-group text-center">
                <input type="submit" value="Insert" class="btn btn-primary">
            </div>
        </form>
    </div>
    <script>
<script>
    function validateForm() {
        var level = document.forms["quizForm"]["level"].value;
        var question = document.forms["quizForm"]["question"].value;
        var option1 = document.forms["quizForm"]["option1"].value;
        var option2 = document.forms["quizForm"]["option2"].value;
        var option3 = document.forms["quizForm"]["option3"].value;
        var option4 = document.forms["quizForm"]["option4"].value;
        var answer = document.forms["quizForm"]["answer"].value;

        if (level == "" || question == "" || option1 == "" || option2 == "" || option3 == "" || option4 == "" || answer == "") {
            alert("Please fill all input fields.");
            return false;
        }
    }
</script>

 </script>
</body>
</html>
