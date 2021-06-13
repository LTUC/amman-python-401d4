from abc import ABC

class Band():
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
    def add_musician(self, member):
        self.members.append(member)

class Musician(ABC):
    pass

class Bassist(Musician):
    pass

class Drummer(Musician):
    pass

class Guitarist(Musician):
    pass



if __name__ == "__main__":
    mo_nada = Bassist('Mo Nada')
    suhaib = Drummer('Suhaib')
    bayan = Guitarist('Bayan')

    asac_band = Band('ASAC Band', [mo_nada, suhaib, bayan])

    asac_band.add_musician(Drummer('Hamza'))

# Fixtures

