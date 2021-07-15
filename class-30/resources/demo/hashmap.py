class Hashmap:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size

    def add(self, key, value):
        idx = self.get_hash(key)
        # First time we access this location, no colision detected
        if not self.map[idx]:
            self.map[idx] = [[key, value],]
        # There is a colition and we visited this array index before
        else:
            self.map[idx].append([key, value])

    def find(self, key):
        pass

    def contains(self, key):
        pass

    def get_hash(self, key):
        # 1. calculate summation of all asccii codes
        ascii_total = 0
        for ch in key:
            ascii_total += ord(ch)
        # 2. multiply by prime number
        hashed = ascii_total * 17
        # 3. modula by size of array
        hashed = hashed % self.size
        return hashed



if __name__=='__main__':
    things = Hashmap(1024)
    # things.add('name', 'Ahmad')
    # things.add('color', 'red')
    # things.add('num', 3)
    # assert things.find('color') == 'red'
    # assert things.find('num') == 3
    things.add('could', 67)
    things.add('cloud', 34)
    things.add('coldu', 344)
    assert ['could', 67] in things.map[things.get_hash('could')]
    assert ['cloud', 34] in things.map[things.get_hash('cloud')]
    assert ['coldu', 344] in things.map[things.get_hash('coldu')]
    print(things.get_hash('could'))
    print(things.map[things.get_hash('could')])
    print('TESTED Successfully!!!!!')
    print(things.get_hash('Pioneer Square'))
    print(things.get_hash('Alki Beach'))


    # [['could', 67],['cloud', 34],['coldu', 344]]


