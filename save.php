<?php
$counter = $_POST["counter"];
file_put_contents("counter.md", $counter);
?>
