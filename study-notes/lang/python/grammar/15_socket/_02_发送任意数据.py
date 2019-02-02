import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    send_data = input("请输入要发送的数据: ")
    udp_socket.sendto(send_data.encode("utf-8"), ("172.16.23.170", 8080))
    udp_socket.close()


if __name__ == '__main__':
    main()