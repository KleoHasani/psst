from socket import SOCK_DGRAM, SOCK_STREAM, AF_INET, AF_INET6
from click import argument, group, option

from .logo import draw_logo
from .pprinter import p_print
from .scan import p_scan
from .Target import Target

@group(invoke_without_command=True)
@option("-i", default=False, is_flag=True, help="Is IPv6?")
@option("-u", default=False, is_flag=True, help="Is UDP?")
@option("-p", default=False, is_flag=True, help="Try all ports? (1 - 65353)")
@argument('remote_address', default="127.0.0.1")
def cli(remote_address, i, u, p):
    # Print logo.
    draw_logo()

    ip_fam = AF_INET
    ip_type = SOCK_STREAM
    port_range = [i for i in range(1, 10000)]

    if i:
        ip_fam = AF_INET6
    
    if u:
        ip_type = SOCK_DGRAM
    
    if p:
        port_range = [i for i in range(1, 65535)]

    # Scan target and Print TCP ports.
    p_print(p_scan(Target(remote_address, port_range, ip_fam, ip_type)))

    pass