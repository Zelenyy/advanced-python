import socketserver
import logging

logging.root.setLevel(logging.DEBUG)


class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    players = {}

    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        logging.debug(f"{socket} {data}")
        n = data[0]
        name = data[1:n+1]
        self.players[name] = data

        data = b""
        for value in self.players.values():
            data += value
        data = len(data).to_bytes(2, byteorder="big") + \
               len(self.players).to_bytes(1, byteorder="big") + data
        logging.debug(f"{self.client_address[0]} {data}")
        socket.sendto(data, self.client_address)
        logging.debug(str(self.players))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()