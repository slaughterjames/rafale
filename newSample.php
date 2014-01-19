<?php
/*
Rafale v0.3 - Copyright 2013 James Slaughter,
This file is part of Rafale v0.3.

Rafale v0.2 is free software: you can redistribute it and/or modify
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
<div style="padding-top:50px;color:#000000;">Rafale <span style="color:#DF0101">Malware</span> Information <span style="color:#DF0101">System</span></div>
</h2>

<form enctype="multipart/form-data" action="executeRun.php" method="POST">

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
<div style="padding-top:10px;color:#000000;">Sample ID: </div>
<?php
//Variable Declarations
$sampleid = $_POST['uploadedSamplesCount'];
$sampleid = $sampleid;
$rafaleHome = $_POST['rafaleHome'];
$programDirectory = $_POST['programDirectory'];
$maxFileSize = $_POST['maxFileSize'];
?>
<!--Form data used to describe and create a new sameple-->
<input type="text" name="sampleid" readonly="readonly" value="<?php print $sampleid ?>" >
<input type="hidden" name="rafaleHome" id="rafaleHome" value="<?php print $rafaleHome ?>" >
<div style="padding-top:10px;color:#000000;">Sample Information: </div>
<br/>
Sample Name (give this a descriptive name): <input type="text" name="samplename" size="30" maxlength="30">
</br>
E-mail: Send e-mail upon completion of analyis: <input type="checkbox" name="sendemail">
<br/>
Zip Archive Password: Lock sample zip file with a password? <input type="checkbox" name="passwordYorN"> Password: <input type="password" name="password" size="30" maxlength="30">
</br>

<!--Maximum file size - set in the rafale.conf file maxfilesize option-->
<input type="hidden" name="maxFileSize" id="maxFileSize" value="<?php print $maxFileSize ?>" >
<input type="hidden" name="programDirectory" id="programDirectory" value="<?php print $programDirectory ?>" >
Choose a file to upload: <input name="uploadedsample" type="file" /><br />

</td>
<td style="text-align:left">

</td>
</tr>
<tr>
<!--Submit Button to execute the operation of adding a new sample-->
<td colspan="2" style="text-align:left">
<div style="padding-top:10px;color:#000000;">Click to upload malware sample and execute analysis session: </div>
<input name="executerun" id="executerun" type="submit" value="Execute Run >>" /><br/><br/>

</td>
</tr>
 
</table>
</div>
</form>
</div>
</body>
</html>
