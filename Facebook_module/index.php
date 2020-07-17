
<?php
session_start ();
require_once __DIR__ . '/Facebook/autoload.php';
require_once 'userconnect.php';
$fb = new \Facebook\Facebook ( [ 
		'app_id' => '1813494588922588',
		'app_secret' => '24e272fceb785f831e99fe8461229dd0',
		'default_graph_version' => 'v2.8' 
] );
$permissions = [ 
		'user_likes',
		'user_friends' 
]; // optional
$helper = $fb->getRedirectLoginHelper ();
$accessToken = $helper->getAccessToken ();
// session_start();

// $_SESSION['regName'] = $regValue;
if (isset ( $accessToken )) {
	
	//$url = "https://graph.facebook.com/v2.8/me?fields=id,movies{name}&access_token={$accessToken}";
	
	$url = "https://graph.facebook.com/v2.8/me?fields=id%2Cmovies%7Brelease_date%2Cname%7D&access_token={$accessToken}";
	$headers = array (
			"Content-type: application/json" 
	);
	
	$ch = curl_init ();
	curl_setopt ( $ch, CURLOPT_HTTPHEADER, $headers );
	curl_setopt ( $ch, CURLOPT_URL, $url );
	curl_setopt ( $ch, CURLOPT_FOLLOWLOCATION, 1 );
	curl_setopt ( $ch, CURLOPT_SSL_VERIFYPEER, false );
	curl_setopt ( $ch, CURLOPT_COOKIEJAR, 'cookie.txt' );
	curl_setopt ( $ch, CURLOPT_COOKIEFILE, 'cookie.txt' );
	curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );
	curl_setopt ( $ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.3) Gecko/20070309 Firefox/2.0.0.3" );
	curl_setopt ( $ch, CURLOPT_SSL_VERIFYPEER, false );
	
	$st = curl_exec ( $ch );
	$result = json_decode ( $st, TRUE );
	$_SESSION ['result11'] = $result ['id'];
	// include 'userconnect.php';
	echo "<pre>";
	var_dump ( $result );
	echo "</pre>";
	// echo "movies:".$result['movies']['data']['name'];
	
	$user = new User();
	$fbUserData = array(
			'oauth_provider'=> 'facebook',
			'oauth_uid' 	=> $result['id'],
		//	'first_name' 	=> $result['first_name'],
		//	'last_name' 	=> $result['last_name'],
		//	'email' 		=> $result['email'],
		//	'gender' 		=> $result['gender'],
		//	'locale' 		=> $result['locale'],
		//	'picture' 		=> $result['picture']['data']['url'],
		//	'link' 			=> $result['link'],
			'movies'          =>$result['movies'],
			'release_date'    =>$result['release_date']
	);
	$userData = $user->checkUser($fbUserData);
	//echo "Hellooooooooooooooooooooooooooooo\n";
	//echo $userData['id'];
	
	$_SESSION['userData'] = $userData;
	
	//Render facebook profile data
	if(!empty($userData)){
		$output = '<h1>Facebook Profile Details </h1>';
	//	$output .= '<img src="'.$userData['picture'].'">';
		$output .= '<br/>Facebook ID : ' . $userData['oauth_uid'];
	//	echo "\nhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n";
	//	echo $userData['oauth_uid'];
	//	$output .= '<br/>Name : ' . $userData['first_name'].' '.$userData['last_name'];
	//	$output .= '<br/>Email : ' . $userData['email'];
	//	$output .= '<br/>Gender : ' . $userData['gender'];
	//	$output .= '<br/>Locale : ' . $userData['locale'];
		$output .= '<br/>movies : ' . $userData['movies'];
	//	echo "\n\n hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n\n";
		echo $userData['movies'];
		$output .= '<br/>Logged in with : Facebook';
	//	$output .= '<br/><a href="'.$userData['link'].'" target="_blank">Click to Visit Facebook Page</a>';
		$output .= '<br/>Logout from <a href="logout.php">Facebook</a>';
	}else{
		$output = '<h3 style="color:red">Some problem occurred, please try again.</h3>';
	}
	
	
	$myfile = fopen("movie-fb.txt", "w") or die("Unable to open file!");
	$datefile = fopen("date-fb.txt", "w") or die("Unable to open file!");
	
	/*$txt = "John Doe\n";
	fwrite($myfile, $txt);
	$txt = "Jane Doe\n";
	fwrite($myfile, $txt);
	fclose($myfile);
	*/
	
	echo "My auth_id: " . $result ['id'];
	foreach ( $result ['movies'] ['data'] as $key => $value ) {
		$txt =$value ['name'] ;
		fwrite($myfile,$txt);
		#fwrite($myfile, "\n");
		$txt1 =$value ['release_date'];
		if($txt1!="")
			fwrite($datefile, $txt1);
		else 
			fwrite($datefile,"9999");
		//$txt2 =" .";
		//fwrite($myfile, $txt2);
		fwrite($myfile, "\n");
		fwrite($datefile, "\n");
		// echo "<center>";
		// echo "<img src=".$item['picture']['data']['url'].">";
		// echo "<p>" . $value ['name'] . "</p>";
		// echo "<p>".$item['name']."</p>";
		// echo "</center>";
	}
	fclose($myfile);
	$loginUr = $helper->getLoginUrl ( 'http://localhost/BE_Movie_Recommendation/Facebook_module/userconnect.php');
	echo '<a href="' . $loginUr . '">User Connect</a>';
} else {
	$loginUrl = $helper->getLoginUrl ( 'http://localhost/BE_Movie_Recommendation/Facebook_module/', $permissions );
	echo ' 
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
	<html>
	<img src="../data/facebook.png" width="1375" height="425" title="Logo of a company" alt="Logo of a company" align="middle" />
	</html>
	';
	echo '
	<div style="text-align: center">
	<a href="' . $loginUrl . '" align="center">Login with Facebook</a>
	</div>
	';
}
