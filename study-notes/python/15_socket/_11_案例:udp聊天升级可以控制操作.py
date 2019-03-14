import socket


def send_msg(udp_socket):
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))
    send_data = input("请输入要发送的消息:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7788))
    while True:
        print("-----xxx聊天器-----")
        print("1:发送消息")
        print("2.接收消息")
        print("0.退出系统")
        op = input("请输入功能:")
        if op == "1":
            send_msg(udp_socket)
        elif op == "2":
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("输入有误请重新输入...")


if __name__ == '__main__':
    main()