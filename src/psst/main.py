import socket
from queue import Queue
from threading import Thread
from os import cpu_count
from socket import SOCK_DGRAM, SOCK_STREAM, AF_INET, AF_INET6
from click import argument, group, option

from .logo import draw_logo
from .pprinter import p_print
from .Target import Target

# Attempt Socket connection.
def connect(q: Target):
    while not q.ports.empty():
        # Current queued port.
        port = q.ports.get()

        # Create socket object.
        soc = socket.socket()

        # Connect.
        con = soc.connect_ex((q.address, port))
            
        # Add to results list if port is open.
        if con == 0:
            q.results.append(port)
        
        # Close connection.
        soc.close()

        # Task done for queue.
        q.ports.task_done()

@group(invoke_without_command=True)
@option("-i", default=False, is_flag=True, help="Is IPv6?")
@option("-u", default=False, is_flag=True, help="Is UDP?")
@option("-p", default=False, is_flag=True, help="Try all ports? (1 - 65353)")
@argument('address', default="127.0.0.1")
def cli(address: str, i: bool, u: bool, p: bool):
    # Max threads.
    CPU_THREADS = cpu_count() + 4
    
    # Print logo.
    draw_logo()

    ip_fam = AF_INET
    soc_type = SOCK_STREAM
    port_range = 1000

    if i:
        ip_fam = AF_INET6
    
    if u:
        soc_type = SOCK_DGRAM
    
    if p:
        port_range = 65353
    
    # Build port range queue.
    q = Queue(port_range)
    for i in range(1, port_range):
        q.put(i)

    # Create target.
    target = Target(address = socket.gethostbyname(address), ports=q, results=[], soc_type=soc_type, ip_fam=ip_fam)

    for i in range(CPU_THREADS):
        worker: Thread = Thread(target=connect, args=(target, ))
        worker.setDaemon(True)
        worker.start()
    
    # Join queue.
    q.join()

    # Print results.
    p_print(target.results)

    pass