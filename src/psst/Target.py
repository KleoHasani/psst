from dataclasses import dataclass
from socket import AF_INET, AddressFamily, SocketKind
@dataclass
class Target:
    remote_add: str
    ports: list
    ip_type: SocketKind
    ip_fam: AddressFamily = AF_INET