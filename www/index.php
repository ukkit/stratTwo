<?php
// Define the MySQL host; since Docker Compose sets up a network,
// use the service name of the MySQL container.
$host = 'mysql_container';

// Get credentials from environment variables
$user = getenv('MYSQL_USER');
$password = getenv('MYSQL_PASSWORD');
$database = getenv('MYSQL_DATABASE');

$mysqli = new mysqli($host, $user, $password, $database);

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

echo "Successfully connected to MySQL!";
?>
