import socket
print(socket.gethostbyname("localhost"))
print(socket.gethostbyaddr("127.0.0.1"))
print(socket.gethostbyname("www.johnmuellerbooks.com"))
print(socket.getaddrinfo("localhost", 110))
print(socket.getaddrinfo("johnmuellerbooks.com", 80))
print(socket.getservbyport(25))
print(socket.gethostbyname(socket.gethostbyname("www.google.com")))