<?php

include '../../../utils/connexion.php';

try {
    $conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "CREATE TABLE IF NOT EXISTS Log(id_u INT,
	datelog DATE, 
	user TEXT,
	use_case TEXT, 
	action TEXT,
	PRIMARY KEY(id_u,datelog))";
    // use exec() because no results are returned
    $conn->exec($sql);
    echo "<h2>Table created successfully</h2>";
    }
catch(PDOException $e)
    {
    echo  $e->getMessage();
    }
$conn = null;
?>