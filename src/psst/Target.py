from dataclasses import dataclass
from queue import Queue
from socket import AF_INET, AddressFamily, SocketKind
@dataclass
class Target:
    address: str
    ports: Queue
    results: list
    soc_type: SocketKind
    ip_fam: AddressFamily = AF_INET