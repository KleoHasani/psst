from socket import SOCK_DGRAM
from click import argument, group, clear, echo, style
import scan, Target

cat_row_1 = " _._     _,-'""`-._"
cat_row_2 = "(,-.`._,'(       |\`-/|"
cat_row_3 = "    `-.-' \ )-`( , o o)"
cat_row_4 = """          `-    \`_`"'-"""

@group(invoke_without_command=True)
@argument('remote_address', default="127.0.0.1")
def cli(remote_address):
    tcp_open_ports = []
    udp_open_ports = []

    # Print logo.
    clear()
    echo(f'{style("-" * 48, fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 20} PSST {" " * 20}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 10} Port Super Scanner Tool {" " * 11}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 46}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_1, fg="red")}{" " * 18}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_2, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_3, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 11}{style(cat_row_4, fg="red")}{" " * 12}{style("#", fg="blue")}')
    echo(f'{style("#", fg="blue")}{" " * 20}By: Kleo Hasani {" " * 10}{style("#", fg="blue")}')
    echo(f'{style("-" * 48, fg="blue")}')

    # Perform scan.
    tcp_target = Target.Target(remote_add=remote_address)
    udp_target = Target.Target(ip_type=SOCK_DGRAM)


    tcp_open_ports = scan.p_scan(tcp_target)
    udp_open_ports = scan.p_scan(udp_target)
    

    # Print ports.
    # Print ports.
    echo(f'{style("TCP Ports", fg="yellow")}')

    if len(tcp_open_ports) == 0:
        echo(f'{" " * 4}{style("None", fg="red")}')
    else:
        for port in udp_open_ports:
            echo(f'{" " * 4}Port: {style(port, fg="green")}')

    # Print ports.
    echo(f'{style("UDP Ports", fg="cyan")}')

    if len(udp_open_ports) == 0:
        echo(f'{" " * 4}{style("None", fg="red")}')
    else:
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