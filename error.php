<?php
/*
Rafale v0.2 - Copyright 2013 James Slaughter,
This file is part of Rafale v0.2.

Rafale v0.2 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Rafale v0.2 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Rafale v0.2.  If not, see <http://www.gnu.org/licenses/>.
*/

//ToDo:  Add code to enable database use and better site security
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" >
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
<title>Rafale</title>
</head>

<body style="font-family:Verdana;color:#9bbbcb;">
<div style="text-align:center">

<h2>
<div style="padding-top:50px;color:#000000;">Rafale <span style="color:#DF0101">Malware</span> Information <span style="color:#DF0101">System</span></div>
</h2>

<div style="text-align:center">
<div style="padding-top:30px;color:#000000;">Your System Information: </div>

<?php 
//System Info
system("uname -a");
?>
<div align="center">
<table style="margin-top:50px;">
<tr>
<td style="text-align:left">

<?php
//Variable Declarations
$rafaleHome = $_POST['rafaleHome'];
//Uncomment below if troubleshooting
//echo "Rafale Home: ".$rafaleHome;
?>

<div style="padding-top:50px;color:DF0101;">Error!</div>
<br/>
Something's gone wrong with the upload or analysis. 
</br>
<!--Link back to the main page-->
<br/><a href="rafale.php"> Return Home </a>

</td>
</tr>
 
</table>
</div>
</form>
</div>
</body>
</html>
