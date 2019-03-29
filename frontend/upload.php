
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
echo "<pre>$fileContent</pre>";
?>

<h2>Try running commands on the file</h2>
<h4>whoami</h4>
<?php
echo exec("whoami");
?>

<h4>mkdir results</h4>
<?php
$ok = mkdir("results");
if (!$ok)
    echo "<pre>mkdir failed.....</pre>";
?>

<h4>pwd</h4>
<?php
echo exec("pwd");
?>

<h4>mv the file</h4>
<?php
echo "mv " . $Myfile['tmp_name'] . " " . $_FILES["fileToUpload"]["name"];
$ok = exec("mv " . $Myfile['tmp_name'] . " " . $_FILES["fileToUpload"]["name"]);
if (!$ok)
    echo "<pre>mv failed</pre>"
?>

<h4>ls</h4>
<?php
$fname = $Myfile['tmp_name'];
//$res = shell_exec("ls -alh $fname");
$res = shell_exec("ls -alh .");
echo "<pre>$res</pre>";
?>
