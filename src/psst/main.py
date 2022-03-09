from socket import SOCK_DGRAM, SOCK_STREAM
from click import argument, group
from .logo import draw_logo
from .pprinter import p_print
from .scan import p_scan
from .Target import Target

@group(invoke_without_command=True)
@argument('remote_address', default="127.0.0.1")
def cli(remote_address):
    # Print logo.
    draw_logo()

    # Scan target and Print TCP ports.
    p_print(p_scan(Target(remote_address, [i for i in range(1, 65535)], SOCK_STREAM)))

    # Scan target and Print UDP ports.
    p_print(p_scan(Target(remote_address, [i for i in range(1, 65535)], SOCK_DGRAM)))

    pass