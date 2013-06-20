'''
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
'''

'''
logger.py - This file is responsible for providing a mechanism to write 
log files to the hard drive and read in the rafale.conf file


logger
Class: This class is responsible for providing a mechanism to write
       log files to the hard drive and read in the rafale.conf file
       - Uncomment commented lines in the event troubleshooting is required
        
'''

#python imports
import datetime
#programmer generated imports
from fileio import fileio

class logger:
    
    '''
    Constructor
    '''
    def __init__(self):
        
        self.fileobject = 0
        self.logheader = ''
        self.logdir = ''
        self.startdatetime = ''
        self.targetbase = ''
        self.samplesdirectory = ''
        self.samplesdir = ''
        self.samplesroot = ''
        self.samplesrepo = ''
        self.temp = ''
        self.home = ''
        self.rafaleroot = ''
        self.signaturedb = ''
        self.emailsend = ''
        self.emailrecp = ''
        self.confname = '/etc/rafale/rafale.conf'
    '''
    ConfRead()
    Function: - Reads in the pyrecon.conf config file

    '''
    def ConfRead(self, debug):
        
        ret = 0
        FConf = fileio()
        ret = FConf.ReadFile(self.confname)
        if (ret==0):
            for line in FConf.fileobject:
                if (debug == True):
                    print line
                intLen = len(line)
                if (line.find('targetbase') != -1):
                    self.logdir = line[11:intLen]
                elif (line.find('samplesdirectory') != -1):
                    self.samplesdirectory = line[17:intLen]           
                elif (line.find('samplesroot') != -1):
                    self.samplesroot = line[12:intLen]
                elif (line.find('samplesrepo') != -1):
                    self.samplesrepo = line[12:intLen]
                elif (line.find('home') != -1):
                    self.home = line[5:intLen]
                elif (line.find('rafaleroot') != -1):
                    self.rafaleroot = line[11:intLen]
                elif (line.find('signaturedb') != -1):
                    self.signaturedb = line[12:intLen]
                elif (line.find('emailsend') != -1):
                    self.emailsend = line[10:intLen]
                elif (line.find('emailrecp') != -1):
                    self.emailrecp = line[10:intLen]
                else:
                    if (debug == True):
                        print ''

            if (debug == True):
                print 'Finished configuration.'
                print ''
            
            return 0
        else:
            return -1


    '''
    LogCreate()
    Function: - Creates a new log based on the FuzzID
              - Adds a header to the log 
              -  
    '''     
    def LogCreate(self, sampleid, samplename, filename, filetype, filesize):  
        FLog = fileio()
        self.startdatetime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        filename = self.logdir + sampleid + '.html'
        data = '<html>\n'
        data += '<a href=\"' + self.home + '\"> Return Home </a><br/>\n'
        data += '\n--------------------------------------------------------------------------------'
        data += '---------------------------------------<br/>'
        data += '<head>\n<title>' + sampleid + '</title>\n'
        data += '\n<strong>Starting Analysis On: </strong><br/>\n' + '\n' + '<strong>SampleID: </strong>' + sampleid + ' <strong>Sample: </strong>' + samplename
        data += ' <strong>Date/Time: </strong>' + self.startdatetime + '<br/>\n'
        data += ' <strong>Filename: </strong>' + filename + ' <strong>Filetype: </strong>' + filetype + ' <strong>Filesize: </strong>' + filesize + '<br/>'
        data += '--------------------------------------------------------------------------------'
        data += '---------------------------------------<br/>\n</head>\n<body>\n'
        FLog.WriteNewLogFile(filename, data)
           
        return 0   
    
    '''
    LogFooter()
    Function: - Adds a footer to close out the log file created in the function above
              - 
              -  
    '''     
    def LogFooter(self, sampleid):  
        FLog = fileio()
        self.startdatetime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        filename = self.logdir + sampleid + '.html'        
        data = '<strong>END OF FILE</strong><br/>'
        data += '--------------------------------------------------------------------------------'
        data += '---------------------------------------\n<br/>'
        data += '<a href=\"' + self.home + '\"> Return Home </a>\n</body>\n</html>\n'
        #print 'Home: ' + self.home + '/n'
        FLog.WriteLogFile(filename, data)
           
        return 0       
        
    '''    
    WriteLog()
    Function: - Writes to the current log file            
              - Returns to the caller
    '''    
    def WriteLog(self, sampleid, newlogline):  
        FLog = fileio()
        nowdatetime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        filename = self.logdir + sampleid + '.html'
        data = nowdatetime + ' ' + newlogline + '\n<br/>'
        FLog.WriteLogFile(filename, data)
           
        return 0 
    
    '''    
    WriteSamplesFile()
    Function: - Writes to the samples text file with a summary of the run            
              - Returns to the caller
    '''    
    def WriteSamplesFile(self, sampleid, samplename, SHA256):  
        FLog = fileio()
        nowdatetime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        #print 'Writing Samples.txt\n'
        filename = self.samplesdir.strip() + 'Samples.txt'
        data = 'SampleID: ' + sampleid + ' Name: ' + samplename +  ' SHA256: ' + SHA256 + ' Date/Time: ' + nowdatetime + '\n'
        FLog.WriteLogFile(filename, data)
           
        return 0 
        
