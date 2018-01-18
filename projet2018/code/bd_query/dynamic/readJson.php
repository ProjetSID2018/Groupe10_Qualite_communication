<?php

include '../../utils/connexion.php';
	try {
		$conn = new PDO("mysql:host=localhost;dbname=DBIndex", $username, $password);
		# set the PDO error mode to exception
		$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		
		$jsondata = file_get_contents('./test.json',FILE_USE_INCLUDE_PATH);
		$data = json_decode($jsondata, true);
		$don = array();
		foreach ($data as $user_name => $req){
			$id = $req['id'];
			$sql = "SELECT user, action FROM Log WHERE id_u = $id";				
			$res = $conn->query($sql);
			$result = $res->fetchAll(PDO::FETCH_ASSOC);
			$row_array['user'] = $result[0]['user'];
			$row_array['action'] = $result[0]['action'];
			array_push($don, $row_array);
			#print_r($row_array);
		}
		$res_json = json_encode($don);
		#var_dump($res_json);
		$nom_fichier = "g8_test.json";
		$fichier = fopen($nom_fichier, "w+");
		if(fwrite($fichier, $res_json))
		{
			echo $nom_fichier . ' file created ';
		}
		else{
			echo 'There is some error ';
		}
		fclose($fichier);
		
		###### POST
		$url = "http://127.0.0.1:5000/f1";
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
		curl_setopt($ch, CURLOPT_POSTFIELDS, $res_json);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		curl_setopt($ch, CURLOPT_HTTPHEADER, array(
						'Content-Type: application/json',
						'Content-Length: ' . strlen($res_json))
		);
		#curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
		$reponse = curl_exec($ch);
		#var_dump($reponse);
		curl_close($ch);
				
		###### GET
		/*$curl = curl_init();
		curl_setopt_array($curl, array(
			CURLOPT_RETURNTRANSFER => TRUE,
			CURLOPT_URL => $url
		));
		$resp = curl_exec($curl);
		echo $resp;
		curl_close($curl);*/
	}
	catch(PDOException $e){
		echo  $e->getMessage();
	}
	$res = null;
	$conn = null;
?>
