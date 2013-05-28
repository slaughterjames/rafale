#!/usr/bin/python

'''
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

'''

'''
rafale.py - This is the main file of the program and is the jumping off point
into the rest of the code
'''

#python imports
import sys
import os
import subprocess

#third-party imports
import pefile

#programmer generated imports
from argparser import argparser 
from logger import logger
from fileio import fileio

'''
Usage()
Function: Display the usage parameters when called
'''
def Usage():
    print 'Usage: [required] --targetpath --sampleid --samplename --filename --filetype --filesize [optional] --passwordYorN --password --sendemail -- debug --help'
    print 'Required Arguments:'
    print '--sampleid - determined by the PHP component based on the number of entries in the Samples.txt file'
    print '--samplename - descriptive name given by the malware submitter'
    print '--filename - the actual filename of the malware sample'
    print '--filetype - type of file of the malware sample determined at upload time'
    print '--filesize - size of the malware file determined at upload time'
    print 'Optional Arguments:'
    print '--passwordYorN - checkbox in the PHP component to determine if the zipped malware archive made after the analysis is'
    print '                 completed will be password protected.'
    print '--password - actual password value entered if the above passwordYorN value is true'
    print '--sendemail - when analysis is completed on the uploaded malware sample, send an e-mail with a summary of the findings.'    
    print '--debug - prints verbose logging to the screen to troubleshoot issues with a Rafale installation.'
    print '--help - You\'re looking at it!'
    sys.exit(-1)
    
'''
MD5()
Function: - Get the MD5 sum of the uploaded sample 
'''     
def MD5():
    temp = ''
    strpos = 0
    newlogentry = ''

    newlogentry = 'MD5 hash of uploaded sample file: <strong>' + AP.filename + '</strong>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''
    subproc = subprocess.Popen('md5sum '+ LOG.temp + AP.filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)     
    for md5data in subproc.stdout.readlines():
         if  (AP.debug == True):
             print md5data
         temp = md5data
    
    strpos = temp.find(' ')

    AP.MD5 = temp[0:strpos]

    newlogentry = '<strong>' + AP.MD5 + '</strong>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''
       
    return 0    

'''
SHA256()
Function: - Get the SHA256 sum of the uploaded sample
'''
def SHA256():
    temp = ''
    strpos = 0
    newlogentry = ''

    newlogentry = 'SHA256 hash of uploaded sample file: <strong>' + AP.filename + '</strong>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''
    subproc = subprocess.Popen('sha256sum '+ LOG.temp + AP.filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for sha256data in subproc.stdout.readlines():
         if  (AP.debug == True):
             print sha256data
         temp = sha256data

    strpos = temp.find(' ')

    AP.SHA256 = temp[0:strpos]

    newlogentry = '<strong>' + AP.SHA256 + '</strong>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    return 0
    

'''
VirusTotal()
Function: - Submit the SHA256 hash to see if it's recognized on VirusTotal
'''
def VirusTotal():

    filename = LOG.logdir + 'VirusTotalReport.html'
    target = 'https://www.virustotal.com/en/file/' + AP.SHA256 + '/analysis/'
    newlogentry = ''

    if (AP.debug == True):
        print 'WGet: target: ' + target

    newlogentry = 'Attempting to gather data on uploaded sample file: <strong>' + AP.filename + '</strong> from <a href=\"https://www.virustotal.com\">https://www.virustotal.com</a>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    #WGet flags: --tries=3 Limit retries to a host connection to 3
    #            -S Show the original server headers
    #            -O output to given filename
  
    subproc = subprocess.Popen('wget --tries=3 -S -O ' + filename + ' ' + target, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for virustotal_data in subproc.stdout.readlines():
        AP.virustotal_output_data += virustotal_data
        if (AP.debug == True):
            print virustotal_data
    
    newlogentry = 'Virus Total Data has been downloaded to a file here: <a href=\"' + LOG.rafaleroot + 'samples/' + AP.sampleid + '/' + 'VirusTotalReport.html' + '\"> VirusTotal Report </a>' 
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    newlogentry = 'The live Virus Total Data can be found here: <a href=\"'  + target + '\"> VirusTotal Report </a>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''    

    return 0

'''
PEFile()
Function: - Get the particulars on the submitted sample to give a jump start 
            on reverse engineering
'''
def PEFile():
            
    newlogentry = ''
    full_dump = ''
    filename = LOG.logdir + 'FullDump.txt'

    FI = fileio()

    newlogentry = 'Sample Attribute Sections:'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    for section in PEX.sections:
       newlogentry = 'Section Name: ' + section.Name + ' Virtual Address: ' + str(hex(section.VirtualAddress)) + ' Virtual Size: ' + str(hex(section.Misc_VirtualSize)) + ' Raw Data Size: ' +  str(section.SizeOfRawData)
       LOG.WriteLog(AP.sampleid, newlogentry)
       newlogentry = ''

    newlogentry = 'Imported Symbols:'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''    

    try:
        for entry in PEX.DIRECTORY_ENTRY_IMPORT:
            newlogentry = entry.dll
            LOG.WriteLog(AP.sampleid, newlogentry)
            newlogentry = ''

            for imp in entry.imports:
                if (AP.debug == True):
                    print 'imp address and name: ' + str(hex(imp.address)) +  str(imp.name)
                newlogentry = '\t' +  ' ' + str(hex(imp.address)) +  ' ' + str(imp.name)
                LOG.WriteLog(AP.sampleid, newlogentry)
                newlogentry = ''
    except:
        newlogentry = 'Unable to process DIRECTORY_ENTRY_IMPORT object'
        LOG.WriteLog(AP.sampleid, newlogentry)
        newlogentry = ''        
  

    newlogentry = 'Exported Symbols:'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    try:
        for exp in PEX.DIRECTORY_ENTRY_EXPORT.symbols:
            if (AP.debug == True):
                print str(hex(PEX.OPTIONAL_HEADER.ImageBase + exp.address)) + ' ' + exp.name + ' ' + str(exp.ordinal)
            newlogentry = hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal
            LOG.WriteLog(AP.sampleid, newlogentry)
            newlogentry = ''
    except:
        newlogentry = 'Unable to process DIRECTORY_ENTRY_EXPORT object'
        LOG.WriteLog(AP.sampleid, newlogentry)
        newlogentry = ''

    newlogentry = 'Complete Dump:'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    try:
        FI.WriteLogFile(filename, PEX.dump_info())
        newlogentry = 'Dump file has been generated to file here: <a href=\"' + LOG.rafaleroot + 'samples/' + AP.sampleid + '/' + 'FullDump.txt' + '\"> Full Dump Report </a>'
        LOG.WriteLog(AP.sampleid, newlogentry)
        newlogentry = ''
    except:
        newlogentry = 'Unable to perform full dump against uploaded file'
        LOG.WriteLog(AP.sampleid, newlogentry)
        newlogentry = ''

    return 0

'''
Email()
Function: Send an Email summarizing the sample and alerting the admin of a new sample
'''
def Email():
    FI = fileio()
    filename = LOG.logdir + 'Msg.txt'
      
    if (AP.debug == True):
        print 'Filename: ' + filename
        print 'Email Sender: ' + AP.emailsend

    email_output_data = ''
    
    #For some strange reason, the e-mail address values simply will not be read in as strings so they need conversion
    email_output_data += 'To: ' + str(LOG.emailrecp.strip()) + '\n'
    email_output_data += 'From: ' + str(LOG.emailsend.strip()) + '\n'    
    email_output_data += 'Subject: Rafale Malware Information System - New Sample: ' + AP.filename + '\n'

    email_output_data += '\n'
    email_output_data += 'Hi,\n'
    email_output_data += '\n'
    email_output_data += 'Rafale has received a new sample. SampleID: ' + AP.sampleid + ' Filename: ' + AP.filename + '\n'
    email_output_data += '\n'
    email_output_data += 'Hash results are as follows: \n'
    email_output_data += '\n'
    email_output_data += 'MD5\n'
    email_output_data += '---------\n'
    email_output_data += AP.MD5 + '\n'
    email_output_data += ' \n'
    email_output_data += 'SHA256\n'
    email_output_data += '---------\n'
    email_output_data += AP.SHA256 + '\n'
    email_output_data += '\n'
   
    FI.WriteLogFile(filename, email_output_data)

    if (AP.debug == True):
        print email_output_data
   
    subproc = subprocess.Popen('/usr/sbin/ssmtp ' + str(LOG.emailrecp.strip()) + ' < ' + filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for email_data in subproc.stdout.readlines():
       if (AP.debug == True):
           print email_data


'''
MoveAndZip
Function: - Zips sample file, moves to appropriate directory for storage and deletes the temp file
'''
def MoveAndZip():

    newlogentry = ''

    newlogentry = 'Archiving Sample...'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    if (AP.debug==True):
        print 'zip ' + LOG.temp + AP.sampleid + '.zip ' + LOG.temp + AP.filename 
        print 'mv ' +  LOG.temp + AP.sampleid + '.zip ' + LOG.samplesdir + AP.sampleid + '/'

    #Add a password if chosen otherwise, ZIP up the file
    if (AP.passwordYorN == True):
        subproc = subprocess.Popen('zip -P ' + AP.password + ' ' + LOG.temp + AP.sampleid + '.zip ' + LOG.temp + AP.filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    else:
        subproc = subprocess.Popen('zip ' + LOG.temp + AP.sampleid + '.zip ' + LOG.temp + AP.filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    #Move the file to the correct logging directory
    subproc = subprocess.Popen('mv ' + LOG.temp + AP.sampleid + '.zip ' + LOG.samplesdir + AP.sampleid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    newlogentry = 'Sample has been saved to file here: <a href=\"' + LOG.rafaleroot + 'samples/' +  AP.sampleid + '/' + AP.sampleid + '.zip' + '\"> Download Sample </a>'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''

    #if (AP.debug==True):
    for mv_data in subproc.stdout.readlines():
        print mv_data

    #Delete the unzipped sample from the temp directory
    subproc = subprocess.Popen('rm ' +  LOG.temp + AP.filename, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    newlogentry = 'Original sample has now been removed from the temp directory.'
    LOG.WriteLog(AP.sampleid, newlogentry)
    newlogentry = ''   

    return 0

 
'''
Terminate()
Function: - Attempts to exit the program cleanly when called  
'''     
def Terminate(exitcode):
    sys.exit(exitcode)
'''
This is the mainline section of the program and makes calls to the 
various other sections of the code
'''
    
if __name__ == '__main__':
    
        ret = 0
           
        AP = argparser()
        ret = AP.Parse(sys.argv)

        if (ret == -1):
            Usage()
            Terminate(ret)         
    
        #Mix and match external classes 
        #Some duplication could be reduced in a later version                
        LOG = logger()
        ret = LOG.ConfRead(AP.debug)        

        if (ret == -1):
            print 'Logger terminated reading the configuration file...'
            Terminate(ret)
 
        LOG.logdir = LOG.samplesdirectory.strip() + AP.sampleid.strip() + '/'
        LOG.samplesdir = LOG.samplesdirectory.strip()
        LOG.temp = LOG.samplestemp.strip()

        if (AP.debug == True):
            print 'LOG variables:\n' 
            print 'logdir: ' + LOG.logdir + '\n'
            print ''       
            print 'samplesdir: ' + LOG.samplesdir + '\n'
            print ''  
            print 'temp: ' + LOG.temp + '\n'
            print ''        

        if not os.path.exists(LOG.logdir):
            os.makedirs(LOG.logdir)
        else:
            if (AP.debug == True):
                print 'SampleID: ' + AP.sampleid + ' has previously been dealt with.  Terminating program.'
            Terminate(0)

        if (LOG.LogCreate(AP.sampleid, AP.samplename, AP.filename, AP.filetype, AP.filesize)==0):
            AP.logobject = LOG.fileobject
        else:
            Terminate(-1)
                
        MD5()

        SHA256()

        VirusTotal()

        PEX = pefile.PE(LOG.temp + AP.filename)

        PEFile()

        MoveAndZip()                         
        
        if (AP.sendemail == True):
            Email()
    
        if (AP.debug==True):
	    print 'Program Complete'
        newlogentry = 'Program Complete'
        LOG.WriteLog(AP.sampleid, newlogentry)
        newlogentry = ''
        LOG.LogFooter(AP.sampleid)
        LOG.WriteSamplesFile(AP.sampleid, AP.samplename, AP.SHA256)
        Terminate(0)
