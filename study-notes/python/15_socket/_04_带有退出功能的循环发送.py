import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input("请输入要发送的数据: ")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), ("172.16.23.170", 7788))
    udp_socket.close()


if __name__ == '__main__':
    main()