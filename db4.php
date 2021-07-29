<?php
    //open connection to mysql db
    $connection = mysqli_connect("localhost","root","root","todolist") or die("Error " . mysqli_error($connection));

    //fetch table rows from mysql db
    $sql = "select * from todotable";
    $result = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));

    //create an array
    $resarray = array();
    while($row =mysqli_fetch_assoc($result))
    {
        $resarray[] = $row;
    }
    echo json_encode($resarray);
	
	$obj = json_decode($resarray);
	echo $obj;
	//vararray=json_encode($resarray);
	///echo vararray[0];
//var_dump(json_decode($resarray, true));

    //close the db connection
    mysqli_close($connection);
?>
<!DOCTYPE html>
<html>
<body>

<h2>Make a table based on JSON data.</h2>

<p id="demo"></p>



</body>
</html>
