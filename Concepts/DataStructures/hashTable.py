class HashTable(object):

    def __init__(self):
        self.dictionary = {}


hash_dict = HashTable()

def add(key, value):
    #if it exists, return error message
    #if not, then add it in the dictionary
    hash_dict.dictionary[key] = value

def get(key):
    return hash_dict.dictionary[key]

add("one", "1")
add("two", "2")
add("three", "3")
print get("three")
