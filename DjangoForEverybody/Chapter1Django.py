from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM) # Connects to INET, SOCK_STREAM decides if we are making the call or recieving the call 
    try:
        serversocket.bind(('localhost', 9000)) # We are basically creating a faux port 9000 because there will only be one connection on it, ours.
        serversocket.listen(5) # It will listen for 1 call and will put any of the other similar 4 calls trying to connect in a queue
        while(1): # While 1 connected call is true
            (clientsocket, address) = serversocket.accept() # .accept() creates a new socket to communicate with the connected client 
                                                            # so the other active socket listening for ports cannot get blocked by the communication transfer

            rd = clientsocket.recv(5000).decode() # This line only runs if a call is recieved and will decode and recieve up to 5000 characters
            pieces = rd.split('\n') # Then we split the information by the newlines
            if (len(pieces) > 0 ): print(pieces[0]) # Prints the pieces recieved

            data = 'HTTP/1.1 200 OK\r\n'  # It tells the network on the other side (localhost) that we
            data += 'Content-Type: text/html; charset=utf-8\r\n' # have recieved the request for data (200 OK)
            data += '\r\n'                  # We send a raw (\r) new line (\n)
            data += '<html><body>Hello World</body></html>\r\n\r\n' # The information in html that localhost requested us to send
            clientsocket.sendall(data.encode()) # We encode the new data from unicode into utf-8 and .sendall requested data to the clientsocket
            clientsocket.shutdown(SHUT_WR) # The clientsocket then shuts down, closes the connection and hangs up
            # Will continue sending and recieving data until the clientsocket shuts down
    except KeyboardInterrupt :
        print('\nShutting down...\n')
    except Exception as exc :
        print('Error:\n')
        print(exc)
    
    serversocket.close() # Then we hang up the call and close our socket host-side

print('Access http://localhost:9000') # When you run the server, this is giving you the URL to go to access the client-side information
# It will print all GET requests. It will also try and get the favicon.ico which is for the icon at the top of the tab.
createServer()