from dataclasses import dataclass
from socket import AF_INET, AddressFamily, SocketKind
@dataclass
class Target:
    address: str
    ports: list
    soc_type: SocketKind
    ip_fam: AddressFamily = AF_INET