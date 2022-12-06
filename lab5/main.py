import socket

sockC = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
sockS = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

PORT = 3001


def move():
    move = input("Enter move (r,p,s): ")
    while move not in ["r", "p", "s"]:
        move = input("Enter move (r,p,s): ")
        if move not in ["r", "p", "s"]:
            print("Invalid input")

    if move == "r":
        return "rock"
    elif move == "p":
        return "paper"
    elif move == "s":
        return "scissors"


def checkWin(serverMove, clientMove, score):
    if(serverMove == clientMove):
        return score
    elif(serverMove == "rock"):
        if(clientMove == "scissors"):
            return (score[0] + 1, score[1])
        else:
            return (score[0], score[1] + 1)
    elif(serverMove == "paper"):
        if(clientMove == "rock"):
            return (score[0] + 1, score[1])
        else:
            return (score[0], score[1] + 1)
    elif(serverMove == "scissors"):
        if(clientMove == "paper"):
            return (score[0] + 1, score[1])
        else:
            return (score[0], score[1] + 1)


def checkWinner(score, player):
    if score[player] == 3:
        print("You win {} against {}".format(score[player], score[1 - player]))
        return True
    elif score[1 - player] == 3:
        print("You lose {} against {}".format(
            score[player], score[1 - player]))
        return True


def client():
    ip = input("Enter ip: ")
    sockC.connect((ip, PORT))

    while True:
        data = sockC.recv(1024)
        if not data:
            break
        sockC.sendall(bytearray(move(), "ascii"))
        print("(Opponents move: {})".format(data.decode("ascii")))
        data = sockC.recv(1024)
        scoreServer = data.decode("ascii").split(": ")[1]
        score = (int(scoreServer[4]), int(scoreServer[1]))
        checkWinner(score, 1)
        print(data.decode("ascii"))

    sockC.close()


def server():
    sockS.bind(("127.0.0.1", PORT))
    sockS.listen(1)
    score = (0, 0)

    while True:
        print("Listening...")
        (sockC, address) = sockS.accept()
        print("Connection from: {} ".format(address))
        while True:
            print("Score: {}".format(score))
            serverMove = move()
            sockC.sendall(bytearray(serverMove, "ascii"))
            data = sockC.recv(1024)
            if not data:
                break
            score = checkWin(serverMove, data.decode("ascii"), score)
            sockC.sendall(
                bytearray("Score: {}".format((score[1], score[0])), "ascii"))
            print("(Opponents move: {}, score: {})".format(
                data.decode("ascii"), score))

            if checkWinner(score, 0):
                break

        sockC.close()


def main():
    player = input("Server (s) or Client (c)? ")
    if player == "s":
        server()
    elif player == "c":
        client()
    else:
        print("Invalid input")


if __name__ == '__main__':
    main()
