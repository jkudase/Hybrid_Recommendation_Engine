<?php

if(isset($_POST['search']))
{
	$valueToSearch = $_POST['valueToSearch'];
	// search in all table columns
	// using concat mysql function
	$query = "SELECT * FROM `movies` WHERE `title` LIKE '%".$valueToSearch."%'";
	echo "hello";
	$search_result = filterTable($query);

}
else {
	$query = "SELECT * FROM `movies`";
	$search_result = filterTable($query);
}

// function to connect and execute the query
function filterTable($query)
{
	$connect = mysqli_connect("localhost", "root", "", "movielens");
	$filter_Result = mysqli_query($connect, $query);
	return $filter_Result;
}

?>

<!DOCTYPE html>
<html>
    <head>
        <title>PHP HTML TABLE DATA SEARCH</title>
        <style>
            table,tr,th,td
            {
                border: 1px solid black;
            }
        </style>
    </head>
    <body>
        
        <form action="php_html_table_data_filter.php" method="post">
            <input type="text" name="valueToSearch" placeholder="Value To Search"><br><br>
            <input type="submit" name="search" value="Filter"><br><br>
            
            <table>
                <tr>
                    <th>Id</th>
                    <th>Title</th>
                </tr>

      <!-- populate table from mysql database -->
                <?php while($row = mysqli_fetch_array($search_result)):?>
                <tr>
                    <td><?php echo $row['id'];?></td>
                    <td><?php echo $row['title'];?></td>
                </tr>
                <?php endwhile;?>
            </table>
        </form>
        
    </body>
</html>
