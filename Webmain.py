import socket


def service_client(client_socket):
    """为该客户端返回数据"""
    # 1、接收浏览器发送的请求
    request = client_socket.recv(1024)
    print(">"*30)
    print(request)
    print(">" * 30)
    # 2、返回浏览器需要的数据
    # 2.1、返回header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2返回body
    f = open("./HTML/hip.html", "rb")
    html_content = f.read()
    # response += "你好呀"
    #返回header
    client_socket.send(response.encode("utf-8"))
    #返回body
    client_socket.send(html_content)

    # 关闭套接字
    client_socket.close()


def main():
    "“”整体控制"""
    # 1、创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2、绑定
    server_socket.bind(("", 8888))

    # 3、变为监听套接字
    server_socket.listen(128)

    while True:
        # 4、等待新客户端的链接
        client_socket, client_addr = server_socket.accept()

        # 5、为这个客户端服务
        service_client(client_socket)

    # 关闭监听套接字
    server_socket.close()


if __name__ == '__main__':
    main()
