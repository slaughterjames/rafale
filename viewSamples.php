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
<div style="padding-top:10px;color:#000000;">Sample File Information: </div>

<?php
//Variable Declarations
$malwareSamples = $_POST['malwareSamples'];
$samplesRoot = $_POST['samplesRoot'];
echo "Malware Sample: ".$completedJob."<br />";
$samplesDirectory = $_POST['samplesDirectory'];;
$pos=0;
$sampleID ='';
$file = '';
$path = '';

// Gathering the info and assembling the path of the sample to be viewed
//Uncomment below if troubleshooting
//echo "Samples Root: ".$samplesRoot."<br />";

$pos = strpos($malwareSamples, "Name:");

//Uncomment below if troubleshooting
//echo "POS: ".$pos."<br />";

$sampleID = substr($malwareSamples, 10, $pos-11);

//Uncomment below if troubleshooting
//echo "SampleID: ".$sampleID."<br />";

$file = $sampleID.".html";

//Uncomment below if troubleshooting
//echo "File: ".$file."<br />";

$path = $samplesRoot.$sampleID."/".$file;

//Uncomment below if troubleshooting
//echo "Path: ".$path."<br />";

//Take us to the correct sample report after it's been assembled
header("Location: ".$path);

?>

<div style="padding-top:10px;color:#000000;">Target Information: </div>

</td>
<td style="text-align:left">

</td>
</tr>
 
</table>
</div>
</form>
</div>
</body>
</html>
