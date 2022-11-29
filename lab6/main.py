import socket

PORT = 8080


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", PORT))
    s.listen(1)
    print("Listening on port {}".format(PORT))

    while True:
        conn, addr = s.accept()
        print("Connection from {}".format(addr))
        data = conn.recv(1024).decode("ascii")
        conn.sendall(bytearray("HTTP/1.1 200 ok\n", "ascii"))
        conn.sendall(bytearray("\n", "ASCII"))
        conn.sendall(bytearray("<html>\n", "ASCII"))
        conn.sendall(bytearray("<body>\n", "ASCII"))
        conn.sendall(bytearray("<pre>\n", "ASCII"))
        conn.sendall(data.encode())
        conn.sendall(bytearray("</pre>\n", "ASCII"))
        conn.sendall(bytearray("</body>\n", "ASCII"))
        conn.sendall(bytearray("</html>\n", "ASCII"))
        conn.close()


if __name__ == '__main__':
    main()
