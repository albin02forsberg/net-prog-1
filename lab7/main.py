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
        (sockC, addr) = sockL.accept()
        listOfSockets.append(sockC)
        for s in listOfSockets:
            if s != sockL:
                s.send("[{}{}] (connected)".format(addr[0], addr[1]).encode())

    else:
        data = sock.recv(1024)
        if not data:
            pass
        else:
            pass
