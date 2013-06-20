Rafale v0.2 - Copyright 2013 James Slaughter, This file is part of Rafale v0.1.

Rafale v0.2 is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, 
or (at your option) any later version.

Rafale v0.2 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General 
Public License for more details.

You should have received a copy of the GNU General Public License along with Rafale v0.2. If not, see http://www.gnu.org/licenses/.

Changes v0.2:
- Better flowing logs
- Added strings functionality
- Removed the temp directory and made the upload directory the permenant repository
- Added PEiD signature functionality

Further instructions can be found here: http://www.slaughterjames.com/blog/2013/5/29/introducing-the-rafale-malware-information-system-part-1-set-1.html

Setup: I'll assume everyone reading is also familliar with both installing Linux and running most of the basic commands for it. At some point down the road, I'll create a bash script to automate this. 
For now, just follow these steps.

A few pre-requisites exist before we can install Rafale. You will need a Linux machine, preferably deep behind a secure firewall running the latest version of Python 2.X. Also, you will need to have Apache
installed with PHP enabled (setting up a standard LAMP server using Ubuntu server is the way I went about it).

You will need to make a few new directories. I'm going to suggest you use the following as a template since this is the way I set mine up (I'll show you how to change things later):

/etc/rafale/ - This will be the location for the Python component of Rafale.
/var/www/rafale/ - This will be the location for the PHP component of Rafale.
/var/www/rafale/samples/ - Once a sample has been uploaded and analyzed, it will be stored here in a separate directory.
/var/www/rafale/samples/repo/ - This is the initial upload location for samples.  They will then be zipped and kept here as a repository.

Once those are created, copy the Python files (*.py) to /etc/rafale/ and copy the PHP files to /var/www/rafale/. You will need to copy rafale.conf to /etc/rafale/ as well - it will contain all of the 
configurable options for the application. There is one additional file, Samples.txt which will contain the catelogue of all of your uploaded samples (as a fast and dirty substitute for a database). 
Place it in /var/www/rafale/samples/

You will then likely need to set permissions for the "www-data" user to be able to read and write from these directories. I set mine to maximum allow with no password (the no password part is important), 
however, you may wish to dial those permissions down. on your system for security reasons.

You will need to download the pefile module from https://code.google.com/p/pefile/. You will either need to make it a part of the Python library path or as in my case, I just copied it to the same location 
as the rest of the Rafale Python components, /etc/rafale/.

If you're running this on Ubuntu Server, you'll need to install the binutils package to use the strings command, "sudo apt-get install binutils".

If you're going to make use of the PEiD signatures, you'll need to download a database.  There's a key to edit for its location in the rafale.conf file.  
Two good ones exist here: http://www.sysreveal.com/a-polished-peid-signature-database/ 
and here: https://code.google.com/p/reverse-engineering-scripts/downloads/detail?name=UserDB.TXT

In order to archive and add a bit of safety, I have the code compress the samples before they're moved to their final resting place. To make it easy to download them 
again for dynamic testing in a Windows environment, I use Zip and Unzip. You'll need to install these (in Ubuntu, "sudo apt-get install zip" and "sudo apt-get install 
unzip").

In the event you want to have an email sent to yourself when a new sample is uploaded, you'll need to install and configure sSMTP 
(in Ubuntu, "sudo apt-get install ssmtp").

Now that the basic items are out of the way, we can look at setting the values in the rafale.conf file. The rafale.conf file allows you to customize somewhat where 
malware samples go and where the system is located as well. The conf file will look like the following when you download it:

###Rafale v0.2 Configuration File

#Rafale Program Directory for the Python portion of the app
pythonbase /etc/rafale/

#Rafale Target Base Directory for the Web portion of the app
targetbase /var/www/rafale/

#Rafale Local Samples Directory
samplesdirectory /var/www/rafale/samples/

#Rafale Local Samples File Location
samplesfile /var/www/rafale/samples/Samples.txt

#PEiD Signature Database
signaturedb <signature db>

#Rafale Samples Repo Directory
samplesrepo /var/www/rafale/samples/repo/

#Rafale Home Page
home http://<insert your IP here>/rafale/rafale.php

#Rafale Root Site
rafaleroot http://<insert your IP here>/rafale/

#Rafale Samples Root Site
samplesroot http://<insert your IP here>/rafale/samples/

#Rafale Max File Upload Size
maxfilesize 1000000

#Email Sender - The individual account emails will appear to come from
emailsend <insert your email sender address (i.e example@example.com)>

#Email Recipient - The individual account emails will go to 
emailrecp <insert your email sender address (i.e example@example.com)>

The purpose of each option is explained in the comments above and is geared toward the defaults mentioned in Step #2 above. If staying with the defaults, you'll need to 
add in your IP or host name to home, rafaleroot and samplesroot. Also, if you're going to be sending e-mails then you'll need to add in the addresses for emailsend and 
emailrecp. If you're going to be changing any of the paths, make sure to maintain the trailing "/" and you add they reflect whatever you did in Step #2. The option 
maxfilesize is in bytes and should it be exceeded, will prevent your file from being uploaded to the system.
