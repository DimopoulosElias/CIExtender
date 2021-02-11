<?php
echo "CAUTION: THIS IS THE MEDIUM CHALLENGE WITH CSRF TOKEN ENABLED! THE ORIGINAL HAS BEEN SAVED AT vulnerabilities/exec/source/impossible.php.original";
if( isset( $_POST[ 'Submit' ]  ) ) {
	// Check Anti-CSRF token
	checkToken( $_REQUEST[ 'user_token' ], $_SESSION[ 'session_token' ], 'index.php' );

	// Get input
	$target = $_REQUEST[ 'ip' ];

	// Set blacklist
	$substitutions = array(
		'&&' => '',
		';'  => '',
	);

	// Remove any of the charactars in the array (blacklist).
	$target = str_replace( array_keys( $substitutions ), $substitutions, $target );

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 4 ' . $target );
	}

	// Feedback for the end user
	$html .= "<p>CAUTION: THIS IS THE MEDIUM CHALLENGE WITH CSRF TOKEN ENABLED! THE ORIGINAL HAS BEEN SAVED AT vulnerabilities/exec/source/impossible.php.original
</p><pre>{$cmd}</pre>";


}

// Generate Anti-CSRF token
generateSessionToken();

?>
