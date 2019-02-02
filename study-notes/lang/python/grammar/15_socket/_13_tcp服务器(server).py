import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.listen(128)
    print("-----1-----")
    new_client_socket, client_addr = tcp_server_socket.accept()
    print("-----2-----")
    print(client_addr)
    recv_data = new_client_socket.recv(1024)
    print(recv_data)
    new_client_socket.send("ok".encode("utf-8"))
    new_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()