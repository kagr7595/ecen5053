#Client Pi ended up not getting done.

#The idea behind the QT UI was pretty complete so please run and take a look:
python3 project_ui.py

#The sqs I was hoping to get working had problems as I couldn't get more than one message coming at a time 
#and I never knew if there were more out there.  Also ran into asynchronous problems that I finally fixed on
#the html portion but never got around to getting the client version working.

#Please see the demos that I did on video for the mid-report sqs standard and fifo queues
#The code relating to these is found in UnitTests/aws/sqs
#This code was done before I had to redo my aws account and therefore if you wish to run it, you will need to change the queue names

#Client and Server side need to have the .aws credentials file filled out to work

#boto3 needs to be installed
#QT5 and python need to be installed