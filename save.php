<?php
$counter = $_POST["counter"];
file_put_contents("README.md", $counter);
?>
