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
@argument('address', default="127.0.0.1")
def cli(address: str, i: bool, u: bool, p: bool):
    # Print logo.
    draw_logo()

    ip_fam = AF_INET
    soc_type = SOCK_STREAM
    port_range = [i for i in range(1, 1000)]

    if i:
        ip_fam = AF_INET6
    
    if u:
        soc_type = SOCK_DGRAM
    
    if p:
        port_range = [i for i in range(1, 65535)]

    # Scan target and Print TCP ports.
    target = Target(address, port_range, ip_fam, soc_type)
    scan = p_scan(target)
    p_print(scan)

    pass