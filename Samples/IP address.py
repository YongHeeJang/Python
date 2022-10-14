# 내 ip address 가져오기
# commit test

# 예전에 network를 연결할 때 socket이라는 개념이 있었다. 그래서 python에서 IP address를 가져올 때, socket이라는 library를 이용한다.
import socket

in_addr = socket.gethostbyname(socket.gethostname())
# ip address 뽑아줌

print(in_addr)

