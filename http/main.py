def creat_server(host,port,max_link):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    server.listen(max_link)
    return server

def listen(server):
    content_header=b'''HTTP/1.x 200 ok
    Content-Type: text/html

    '''
    file=open('index.html','r')
    content_body=file.read()
    file.close()
    content=content_header+content_body

    while(1):
        con,addr=server.accept()
        print('link client is:',addr)
        con.sendall(content)
        con.close()
