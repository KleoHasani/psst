from click import progressbar, echo, style
from socket import SOCK_STREAM, socket as Socket
from .Target import Target

# Perform scan.
def p_scan(target: Target) -> list:
    open_ports = []

    # Label.
    ip_type = "TCP Scan" if target.ip_type == SOCK_STREAM else "UDP Scan"
    echo(f'{style(str(ip_type), fg="red")}')

    # Progress bar.
    with progressbar(target.ports) as bar:
        for port in bar:
            connection = None
            # Create soccet.
            soc = Socket(target.ip_fam, target.ip_type)
            try:
                # Create connection.
                connection = soc.connect((target.remote_add, port))
            except:
                pass
            
            if connection == 0:
                # Open connection ports added to open_ports var.
                open_ports.append(port)

    return open_ports