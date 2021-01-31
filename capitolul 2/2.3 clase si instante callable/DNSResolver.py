import socket

class DNSResolver:
    def __init__(self):
        self.cache = {}

    def __call__(self, nume):
        if nume in self.cache:
            print(f"{nume} se afla in DNS cache")
            return self.cache[nume]
        return self.resolve_address(nume)

    def resolve_address(self, name):
        translate = socket.gethostbyname(name)
        self.cache[name] = translate
        return translate


d1 = DNSResolver()
print(d1.resolve_address('www.telacad.ro'))
print(d1('www.telacad.ro')) #cele două moduri de apel sunt echivalente datorită