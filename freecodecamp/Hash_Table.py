class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self, string):
        return sum([ord(char) for char in str(string)])
        
    def add(self, key, value):
        k = self.hash(key)
        if k in self.collection:
             self.collection[k][key] = value
        else:
            self.collection[k] = {key: value}
    def remove(self, key):
        k = self.hash(key)
        if k in self.collection:
            if key in self.collection[k]:
                del self.collection[k][key]
                if not self.collection[k]:
                    del self.collection[k]
    def lookup(self, key):
        k = self.hash(key)
        if k in self.collection:
            if key in self.collection[k]:
                return self.collection[k][key]
            else:
                return None
        else:
            return None 
 
table = HashTable() 
table.add(21,'Amjd') 
table.add(12,'Anas')
print(table.collection)
table.remove(21)
print(table.collection) 
table.remove(12)
print(table.collection)