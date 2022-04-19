class Scoop():
    def __init__(self, flavour):
        self.flavour = flavour

def create_scoops(*args):
    scoops = [Scoop(arg) for arg in args]
    for scoop in scoops:
        print(scoop.flavour)

create_scoops('vanilla', 'chocolate', True)

