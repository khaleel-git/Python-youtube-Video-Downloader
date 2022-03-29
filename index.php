<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: access");
header("Access-Control-Allow-Methods: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

$url = $_GET['url'];
$itag = $_GET['itag'];

if($_SERVER['REQUEST_METHOD']==='GET'){

		if(isset($url) && !isset($itag)){
        
		$meta_basic = shell_exec("python3 /home/apkfuel/public_html/yt/meta_basic.py $url");          
        
        $meta_basic = str_replace("'", '"', $meta_basic);
        
       
		$basic_array = json_decode($meta_basic, TRUE);      
      
        $title = $basic_array['title'];
        $title = str_replace("\n", "", $title);   
        
        $meta_advance = shell_exec("python3 /home/apkfuel/public_html/yt/meta_advance.py $url");
        
        $json_location = "/home/apkfuel/public_html/yt/json/$title" . ".json";              
        $get_json = file_get_contents($json_location);
        $json_obj = json_decode($get_json, true);    

		   
        $meta_basic_array = array("status"=>true,"message"=>"Successfull", "data"=>$basic_array, "file_formats"=>$json_obj);   
        echo json_encode($meta_basic_array);    
        
		}

    	if(isset($itag) && isset($url)){
			$output = shell_exec("python3 /home/apkfuel/public_html/yt/dl.py '$url' $itag");
			// $array = array("status"=>true,"message"=>"Successfull", "response"=>$output);
        	$array = array($output);
			echo json_encode($array);
 
		}	
}


?>