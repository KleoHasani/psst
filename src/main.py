from click import argument, group, progressbar, clear, echo, style
from socket import AF_INET, SOCK_STREAM, socket as Socket


def tcp_scan(remote_address, port_range):
    ports = []
    with progressbar(port_range) as bar:
        for port in bar:
            soc_con = Socket(AF_INET, SOCK_STREAM)
            connection = soc_con.connect_ex((remote_address, port))
            
            if connection == 0:
                ports.append(port)

    return ports


@group(invoke_without_command=True)
@argument('remote_address', default="127.0.0.1")
def cli(remote_address):
    tcp_open_ports = []

    # Print logo.
    clear()
    echo(f'{style("-" * 48, fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 20} PSST {" " * 20}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("-" * 48, fg="blue")}')

    # Perform scan.
    tcp_open_ports = tcp_scan(remote_address, range(1, 65534))
    

    # Print ports.
    echo(f'{style("TCP Ports", fg="yellow")}')
    for port in tcp_open_ports:
            echo(f'{" " * 4}Port: {style(port, fg="green")}')

    echo(f'{style("UDP Ports", fg="cyan")}')
    for port in udp_open_ports:
            echo(f'{" " * 4}Port: {style(port, fg="green")}')
    pass



if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        print("Interrupted")
    except Exception as ex:
        print(f'\033[31m \n{ex} \033[0m \n')
    finally:
        exit(0)