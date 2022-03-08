from socket import AF_INET, SOCK_STREAM

class Target:
    def __init__(self, remote_add = "127.0.0.1", ports = [i for i in range(1, 65535)], ip_fam = AF_INET, ip_type = SOCK_STREAM):
        self.remote_add = remote_add
        self.ports = ports
        self.ip_fam = ip_fam
        self.ip_type = ip_type
        pass