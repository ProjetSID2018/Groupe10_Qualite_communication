<?php

include '../../../utils/connexion.php';

try {
    //$conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
    $conn = new PDO("mysql:host=localhost", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "CREATE DATABASE DBIndex;";
    //$sql = "SHOW DATABASES;";
    // use exec() because no results are returned
    // $conn->exec($sql);
    echo "<h1>Database created successfully</h1>";
	$result = $conn -> query($sql);
	
	while( ( $db = $result->fetchColumn( 0 ) ) !== false )
	{
		echo $db.'<br>';
	}
	
    }
catch(PDOException $e)
    {
    echo  $e->getMessage();
    }

$conn = null;
?>