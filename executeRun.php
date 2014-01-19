<?php
/*
Rafale v0.3 - Copyright 2013 James Slaughter,
This file is part of Rafale v0.3.

Rafale v0.3 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Rafale v0.3 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Rafale v0.3.  If not, see <http://www.gnu.org/licenses/>.
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
<div style="padding-top:50px;color:#000000;">Rafale <span style="color:#DF0101">Malware</span> Information System</div>
</h2>


<div style="text-align:center">
<div style="padding-top:30px;color:#000000;">Your System Information: </div>
<?php 
//System Info
system("uname -a");
?>

<div align="center">
<table style="margin-top:50px;color:#000000;">
<tr>
<td style="text-align:left">

<?php
//Variable Declarations Containing Any Values Being POSTed From Another PHP file
$sampleid = $_POST['sampleid']; 
$samplename = $_POST['samplename'];
$sendemail = $_POST['sendemail'];
$passwordYorN = $_POST['passwordYorN'];
$password = $_POST['password'];
$maxfilesize = $_POST['MAX_FILE_SIZE'];
$rafaleHome = $_POST['rafaleHome'];
$programDirectory = $_POST['programDirectory'];
?>

<!--Pull in the link to the home page so it can be used-->
<input type="hidden" name="rafaleHome" id="rafaleHome" value="<?php print $rafaleHome ?>" >

<?php
//Variable declarations for the arg string of Rafale's Python component
$targetpath = "samples/repo/";

$filetype = '';
$filesize = '';
$filename = '';

$targetpath = $targetpath.basename($_FILES['uploadedsample']['name']); 
$filetype = $_FILES['uploadedsample']['type'];
$filesize = $_FILES['uploadedsample']['size'];
$filename = $_FILES['uploadedsample']['name'];

//Determine if our sample file has been uploaded
if (move_uploaded_file($_FILES['uploadedsample']['tmp_name'], $targetpath))
{   
    //Uncomment below if troubleshooting the upload 
    //echo "The file ".$_FILES['uploadedsample']['name']." has been uploaded. ";
}
else
{
    //Go to an error page if there has been an issue with the upload
    header("Location: error.php");
}

//Start compiling the arg string of the Rafale Python component
$exec = $programDirectory."rafale.py --filename ".$filename." --sampleid ".$sampleid." --samplename ".$samplename." --filetype ".$filetype." --filesize ".$filesize;

if ($sendemail != '')
{
   $exec.=" --sendemail";
}

if ($passwordYorN != '')
{
   $exec.=" --passwordYorN";
   if ($password != '')
   {
       $exec.=" --password ".$password;
   }
}

$exec.=' 2>&1';

//Uncomment two lines below if troubleshooting the Python execution string
//echo "</br>";
//echo $exec."\n";

//Execute!
$last_line = system($exec, $retval);

//Return Home when complete
//Comment below line if troubleshooting the Python execution string
header("Location: ".$rafaleHome);
?>

</td>
</tr>

</table>
</div>
</form>
</div>
</body>
</html>
