'''
Rafale v0.3 - Copyright 2014 James Slaughter,
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
'''

'''
argparser.py - This file is responsible for the parsing of input data from the command line
               from a user and then populating the appropriate values for use elsewhere in 
               the code
'''

#No python imports

#programmer generated imports
from logger import logger

'''
argparser
Class: This class is responsible for the parsing of input data from the command line
from a user and then populating the appropriate values for use elsewhere in the code
'''
class argparser:
    '''
    Constructor
    '''
    def __init__(self):

        self.sampleid = ''
        self.samplename = ''
        self.filename = ''
        self.filetype = ''
        self.filesize = ''
        self.passwordYorN = False
        self.password = ''
        self.sendemail = False
        self.emailsend = ''
        self.emailrecp = ''
        self.debug = False
        self.MD5 = ''
        self.SHA256 = ''
        self.live_virus_total = ''
        self.virustotal_output_data = ''
        self.strings_output_data = ''
        self.logobject = 0

        
    '''       
    Parse()
    Function: - Determines if all required arguments are present
              - Populates the required variables and determines the protocol if not specified
              - returns to calling fuzzer 
              - Uncomment print items to aid in troubleshooting
    '''    
    def Parse(self, args):        
        option = ''
        
        if len(args) < 3:        
            print ''
            return -1

        #Debug print statements are commented out here because in this instance, the --debug flag
        #hasn't ben read yet.               
        #print 'Arguments: '
        for i in range(len(args)):
            if args[i].startswith('--'):
                option = args[i][2:]
                
                if option == 'help':
                    return -1                

                if option == 'sampleid':
                    self.sampleid = args[i+1] 
                    #print option + ': ' + self.sampleid                   

                if option == 'samplename':
                    self.samplename = args[i+1] 
                    #print option + ': ' +self.samplename

                if option == 'filename':
                    self.filename = args[i+1]
                    #print option + ': ' + self.filename
                     
                if option == 'filetype':
                    self.filetype = args[i+1]
                    #print option + ': ' + self.filetype
                     
                if option == 'filesize':
                    self.filesize = args[i+1]
                    #print option + ': ' + self.filesize
                     
                if option == 'passwordYorN':
                    self.passwordYorN = True 
                    #print option + ': passwordYorN = True'
                                         
                if option == 'password':
                    self.password = args[i+1] 
                    #print option + ': ' + self.password                  
                    
                if option == 'sendemail':
                    self.sendemail =  True
                    #print option + ': sendemail = True'
                
                if option == 'debug':
                    self.debug = True
                    #print option + ': ' + str(self.debug)
               
                                                 
        if (self.debug==True):
            print ''
            
        if len(self.sampleid) < 1:
            if (self.debug==True):
	        print 'sampleid is a required argument'            
        	print ''
            return -1
            
        if len(self.filename) < 3:
            if (self.debug==True):
                print 'filename is a required argument'           
                print ''
            return -1

        if len(self.filetype) < 3:
            if (self.debug==True):
                print 'filetype is a required argument'
                print ''
            return -1

        if len(self.filesize) < 3:
            if (self.debug==True):
                print 'filesize is a required argument'
                print ''
            return -1
            
        if len(self.samplename) == '':
            self.samplename = self.filename        
                                   
        return 0
