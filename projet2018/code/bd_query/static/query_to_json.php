<?php
	include '../../utils/connexion.php';
	try 
	{
		$conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
		// set the PDO error mode to exception
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		
		//build the query
		$query = "SELECT * FROM Log ORDER BY id_u";
		$data = $conn->query($query);
		$result = $data->fetchAll(PDO::FETCH_ASSOC);
		$res_json = json_encode($result);
		echo $res_json;
	}
	catch(PDOException $e)
	{
		echo  $e->getMessage();
	}
	$conn = null;
?>
