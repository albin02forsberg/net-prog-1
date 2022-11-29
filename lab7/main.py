import socket
import select

PORT = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", PORT))
sockL.listen(1)

listOfSockets = [sockL]

print("Listening on port {}".format(PORT))


while True:
    tup = select.select(listOfSockets, [], [])
    sock = tup[0][0]

    if sock == sockL:
        (sockClient, addr) = sockL.accept()
        sock = sockClient
        listOfSockets.append(sock)
        for s in listOfSockets:
            if s != sockL:
                s.send("[{}{}] (connected)".format(addr[0], addr[1]).encode())
    else:
        data = sock.recv(1024)
        if not data:
            print("Client disconnected")
            listOfSockets.remove(sock)
            sock.close()
            for s in listOfSockets:
                if s != sockL:
                    s.send("[{}{}] (disconnected)".format(addr[0], addr[1]).encode())
        else:
            for s in listOfSockets:
                if s != sockL:
                    s.send("[{}{}] {}".format(addr[0], addr[1], data.decode()).encode())
