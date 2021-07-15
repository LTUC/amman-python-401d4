from linked_list import LinkedList

class Hashtable:
    def __init__(self, size):
        self.size = size
        self.map = [None]*size # [None, None, None, ....., None] size of 1024
    
    def hash(self, key):
        sum_of_asccii = 0
        for ch in key:
            asccii_of_ch = ord(ch)
            sum_of_asccii += asccii_of_ch
        temp_value = sum_of_asccii * 19
        hashed_key = temp_value % self.size
        return hashed_key
    
    def add(self, key, value):
        # hashed key (memory location aka array index)
        hashed_key = self.hash(key)
        # check if there is previous data
        # add the key and value to the map on that address
        if not self.map[hashed_key]:
            self.map[hashed_key] = LinkedList()
        self.map[hashed_key].add((key,value))
        
        # if self.map[hashed_key]:
        #     self.map[hashed_key].add((key,value))
        # else:
        #     self.map[hashed_key] = LinkedList()
        #     self.map[hashed_key].add((key, value))
        


if __name__ == '__main__':
    hashtable = Hashtable(1024)
    hashtable.add('ahmad', 25)
    hashtable.add('hamad', 29)
    hashtable.add('silent', True)
    hashtable.add('listen', 'Hey man')
    hashtable.add('class', 'Python-401d4')
    for index, item in enumerate(hashtable.map):
        if item:
            print(index, item)