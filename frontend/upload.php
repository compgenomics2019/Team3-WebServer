
<h2>The file info</h2>
<?php
//$target_dir = "uploads/";
//$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
//echo $target_file;
$Myfile = $_FILES["fileToUpload"];
echo json_encode($Myfile);
?>

<h2>The file content</h2>
<?php
$fileContent = file_get_contents($Myfile['tmp_name']);
echo $fileContent
?>
