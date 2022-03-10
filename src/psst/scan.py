import socket
from .Target import Target

# Attempt Socket connection.
def connect(soc: socket.socket, add: str, port: int) -> bool:
    is_open = True

    # Connect.
    try:
        soc.connect((add, port))
    except:
        is_open = False
    
    # Close connection.
    soc.close()
    return is_open

# Perform scan.
def p_scan(target: Target) -> list:
    # Open ports list.
    open_ports: list = []

    # Create socket object.
    soc: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip_add = socket.gethostbyname(target.address)

    for port in target.ports:
        if connect(soc, ip_add, port):
            open_ports.append(port)
            
    return open_ports