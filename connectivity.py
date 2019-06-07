import socket
def internet_on():
    try:
        print("checking internet connection..")
        socket.setdefaulttimeout(5)
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        s.close()
        print('internet on.')
        return True

    except Exception as e:
        print(e)
        print("internet off.")
        return False
internet_on()
