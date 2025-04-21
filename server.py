import socket
# from handler import hamdler_req
def server(host="0.0.0.0",port=8080):
    serv_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serv_socket.bind((host,port))
    serv_socket.listen(10)


    while True:
        client_socket=serv_socket.accept()
        clientAddr= serv_socket.accept()
        print(f"Connection Established Client IP:Port {clientAddr}:{client_socket}")
if __name__=="__main__":
    print("my name",__name__)
    server()