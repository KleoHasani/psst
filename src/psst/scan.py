import socket
from .Target import Target

# Attempt Socket connection.
def connect(add: str, port: int) -> bool:
    is_open = True
    
    soc = socket.socket()

    # Connect.
    con = soc.connect_ex((add, port))
        
    if not con == 0:
        is_open = False
    
    # Close connection.
    soc.close()
    return is_open


# Perform scan.
def p_scan(target: Target) -> list:
    # Open ports list.
    open_ports: list = []

    ip_add = socket.gethostbyname(target.address)

    for port in target.ports:
        if connect(ip_add, port):
            open_ports.append(port)
            
    return open_ports