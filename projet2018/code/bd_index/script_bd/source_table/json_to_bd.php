<?php

include '../../../utils/connexion.php';

	try {
		$conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
		# set the PDO error mode to exception
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		
		$jsondata = file_get_contents('./fichiertest.json',FILE_USE_INCLUDE_PATH);
		$data = json_decode($jsondata, true);
		#echo $data['1']['datelog'];
		
		foreach ($data as $user_name => $req){
			#echo $un['use_case'];
			$id = $req['id'];
			$date = $req['datelog'];
			$user = $req['user'];
			$use_case = $req['use_case'];
			$action = $req['action'];
			#  Insert into mysql table
			$sql = "INSERT INTO Log(id_u,datelog,user,use_case,action)
			VALUES('$id', '$date', '$user', '$use_case', '$action')";
		
			$conn->exec($sql);
			echo"<h2> Row inserted </h2>";
		}
	}
	catch(PDOException $e)
	{
		echo  $e->getMessage();
	}
	$conn = null;
?>
