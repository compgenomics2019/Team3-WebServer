<?php
$target_dir = "/projects/VirtualHost/predictc/html/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$fileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Actually upload the file
if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
		// echo $target_file
		// echo basename( $_FILES["fileToUpload"]["name"])
        echo "Sorry, there was an error uploading your file.";
    }
?>