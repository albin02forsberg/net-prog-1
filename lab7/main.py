import socket
import select

PORT = 8080
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(('', PORT))
sockL.listen(1)

listOfSockets = [sockL]

print("Listening on port {}".format(PORT))

while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        pass
    else:
        data = sock.recv(1024)
        if not data:
            pass
        else:
            pass
