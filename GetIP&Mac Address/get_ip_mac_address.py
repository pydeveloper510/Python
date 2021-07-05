# Get IP and Mac Address
import socket
import getmac

print(f'Ip blocked IP Address: {socket.gethostbyname(socket.getfqdn())} Mac Address: {getmac.get_mac_address()}')
