class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def _hash_function(self, key):
        return hash(key) % self.size

    def _linear_probe(self, index):
        return (index + 1) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._linear_probe(index)

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = self._linear_probe(index)

        return print(f"Key '{key}' not found.")
        

    def delete(self, key):
        index = self._hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                return
            index = self._linear_probe(index)

        
        raise KeyError("Key not found in the hash table")



hash_table = HashTable(10)

hash_table.insert('apple', 5)
hash_table.insert('banana', 7)

print(hash_table.get('apple'))   

hash_table.delete('banana')

print(hash_table.get('banana'))   
