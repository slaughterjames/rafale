<?php
/*
Rafale v0.1 - Copyright 2013 James Slaughter,
This file is part of Rafale v0.1.

Rafale v0.1 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Rafale v0.1 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Rafale v0.1.  If not, see <http://www.gnu.org/licenses/>.
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

<br/>
<br/>
<br/>
<form name="viewsamples" method="POST" action="viewSamples.php">
<div align="center">
<table style="margin-top:50px;">

<strong>View Malware Samples:</strong>
<br/>
<tr>
<?php
echo "\n";
//Variable Declarations
$samplesDirectory = "";
$uploadedSamples = "";
$samplesTemp = "";
$rafaleRoot = "";
$rafaleHome = "";
$samplesRoot = "";
$maxFileSize = "";
$config = "/etc/rafale/rafale.conf";
$configFile = fopen($config, r);

//Read in values from rafale.conf
if ($configFile){
  while(!feof($configFile)){
     $this_line = fgets($configFile);
     if  (strpos($this_line, "samplesdirectory")!==false){
        $samplesDirectory = trim(substr($this_line, 17, strlen($this_line)));
     }
     elseif (strpos($this_line, "samplesfile")!==false){
        $uploadedSamples = trim(substr($this_line, 12, strlen($this_line)));
     }
     elseif (strpos($this_line, "samplestemp")!==false){
        $samplesTemp = trim(substr($this_line, 12, strlen($this_line)));
     }
     elseif (strpos($this_line, "rafaleroot")!==false){
        $rafaleRoot = trim(substr($this_line, 11, strlen($this_line)));
     }
     elseif (strpos($this_line, "home")!==false){
        $rafaleHome = trim(substr($this_line, 5, strlen($this_line)));
     }
     elseif (strpos($this_line, "samplesroot")!==false){
        $samplesRoot = trim(substr($this_line, 11, strlen($this_line)));
     }
     elseif (strpos($this_line, "maxfilesize")!==false){
        $maxFileSize = trim(substr($this_line, 11, strlen($this_line)));
     }
     else{
        //echo "Not found\n"; 
     }
     $this_line = "";
  }
  fclose($configFile);
}
else{
   //Bail out if the conf file is un-readable
   echo "Unable to open Rafale Config file.  Please check your settings.";
}

//Open and read the text file indexing all of the previously collected samples
$samplesFile  = fopen ($uploadedSamples, "r");
$uploadedSamplesCount = 0;

//Display all of the previously collected samples
echo "<select name=\"malwareSamples\" size=\"10\">\n";
if ($samplesFile){
   while(!feof($samplesFile)){
     $this_line = fgets($samplesFile);
     echo "<option>";
     echo $this_line;
     echo "</option>";
     $uploadedSamplesCount ++;
   }
}

echo "</select>\n";

//Make sure we close our text file
fclose($samplesFile);

?>
<br/>
<!--All of the hidden values used to shuttle variable info between PHP files-->
<input type="hidden" name="samplesDirectory" id="samplesDirectory" value="<?php print $samplesDirectory ?>" >
<input type="hidden" name="samplesRoot" id="samplesRoot" value="<?php print $samplesRoot ?>" >
<input type="hidden" name="maxFileSize" id="maxFileSize" value="<?php print $maxFileSize ?>" >

<!--Button to view a selected existing sample-->
<input name="existingsample" id="existingsample" type="submit" value="View Sample Info" /><br /><br />
<td colspan="2" style="text-align:right">
</tr>

</table>
</div>
</form>
<!--Form, button and hidden values specific to creating a new sample-->
<form name="newsample" method="POST" action="newSample.php">
<input type="hidden" name="uploadedSamplesCount" id="uploadedSamplesCount" value="<?php print $uploadedSamplesCount ?>" >
<input type="hidden" name="rafaleHome" id="rafaleHome" value="<?php print $rafaleHome ?>" >
<input name="newsample" id="newsample" type="submit" value="Upload New Sample" /><br /><br />
</form>
</div>
</body>
</html>
