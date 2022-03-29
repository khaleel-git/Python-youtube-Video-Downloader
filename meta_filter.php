<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: access");
header("Access-Control-Allow-Methods: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$url = $_GET['url'];
$itag = $_GET['itag'];

if($_SERVER['REQUEST_METHOD']==='GET'){

		if(isset($url)){
		$output = shell_exec("python3 /home/apkfuel/public_html/yt/meta_filter.py $url");
		$array = array("status"=>true,"message"=>"Successfull", "response"=>$output);
		echo json_encode($array);
		}

    	if(isset($itag) && isset($url)){
			$output = shell_exec("python3 /home/apkfuel/public_html/yt/dl.py '$url' $itag");
			$array = array("status"=>true,"message"=>"Successfull", "response"=>$output);
			echo json_encode($array);
 
		}	
}


?>