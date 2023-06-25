"""The four python modules that follow come from the Kurose-Ross
textbook: Computer Networks: A Top-Down Approach, 6th ed.  These modules
have been slightly modified and commented on by Prof. Paul Amer
for use in his computer networks course at the University of
Delaware.  In particular, changes are made from the authors' Python 2 
code to be compatible with Python 3.

Students that cut and paste these modules are expected to add comments 
(1) in the header indicating their names, class, current date, and what 
the module does, and (2) in the body explaining any code they add/delete. 
"""

##########################################################################
"""  TCPClient.py                                     
Use the better name for this module:   MakeUpperCaseClientUsingTCP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
"""

from socket import *

# STUDENTS - replace your server machine's name 
serverName = "servername"

# STUDENTS - you should randomize your port number.         
# This port number in practice is often a "Well Known Number"  
serverPort = 12000

# create TCP socket on client to use for connecting to remote
# server.  Indicate the server's remote listening port
# Error in textbook?   socket(socket.AF_INET, socket.SOCK_STREAM)  Amer 4-2013 
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName,serverPort))

# interactively get user's line to be converted to upper case
# authors' use of raw_input changed to input for Python 3  Amer 4-2013
sentence = input("Input lowercase sentence: ")

# send the user's line over the TCP connection
# No need to specify server name, port
# sentence casted to bytes for Python 3  Amer 4-2013
clientSocket.send(bytes(sentence, "utf-8"))

#output to console what is sent to the server
print ("Sent to Make Upper Case Server: ", sentence)

# get user's line back from server having been modified by the server
modifiedSentence = clientSocket.recv(1024)

# output the modified user's line 
print ("Received from Make Upper Case Server: ", modifiedSentence)

# close the TCP connection
clientSocket.close()

##########################################################################
""" TCPServer.py                                     
Use the better name for this module:   MakeUpperCaseServerUsingTCP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
"""

from socket import *

# STUDENTS: randomize this port number (use same one that client uses!)
serverPort = 12000

# create TCP welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)

# output to console that server is listening 
print ("The Make Upper Case Server running over TCP is ready to receive ... ")

while 1:
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()
     
    # read a sentence of bytes from socket sent by the client
    sentence = connectionSocket.recv(1024)

    # output to console the sentence received from the client 
    print ("Received From Client: ", sentence)
	 
    # convert the sentence to upper case
    capitalizedSentence = sentence.upper()
	 
    # send back modified sentence over the TCP connection
    connectionSocket.send(capitalizedSentence)

    # output to console the sentence sent back to the client 
    print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()


##########################################################################
"""  UDPClient.py                                     
Use the better name for this module: MakeUpperCaseClientUsingUDP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
"""

from socket import *

# STUDENTS - replace with your server machine's name 
serverName = "hostname"

# STUDENTS - randomize your port number (use the same one in the server)         
# This port number in practice is often a "Well Known Number"  
serverPort = 12000

# create UDP socket
# Error in book? clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
#    corrected by  Amer 4-2013 
clientSocket = socket(AF_INET, SOCK_DGRAM)


# get user's input from keyboard
# raw_input changed to input for Python 3  Amer 4-2013
message = input("Input lowercase sentence: ")

# send user's sentence out socket; destination host and port number req'd
# need to cast message to bytes for Python 3   Amer 4-2013
clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))

print ("Sent to Make Upper Case Server running over UDP: ", message)

# receive modified sentence in all upper case letters from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# output modified sentence and close the socket
print ("Received back from Server: ", modifiedMessage)

# close the UDP socket
clientSocket.close()


##########################################################################
""" UDPServer.py                                     
Use the better name for this module:    MakeUpperCaseServerUsingUDP   
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT NAME                                 
  COURSE NAME and SEMESTER                    
  DATE                                         
  This module will <blah, blah, blah>              
"""

from socket import *

# STUDENTS - you should randomize your port number.         
# This port number in practice is often a "Well Known Number" 
serverPort = 12000

# create UDP socket and bind to your specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

# output to console that server is listening
print ("The Make Upper Case Server running over UDP is ready to receive ... ")

while 1:
    # read client's message AND REMEMBER client's address (IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)

    # output to console the sentence received from client over UDP
    print ("Received from Client: ", message)
	
    # change client's sentence to upper case letters
    modifiedMessage = message.upper()
	
    # send back modified sentence to the client using remembered address
    serverSocket.sendto(modifiedMessage, clientAddress)
 
    # output to console the modified sentence sent back to client
    print ("Sent back to Client: ", modifiedMessage)
