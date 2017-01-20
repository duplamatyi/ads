"""
Hashing is a search concept that consists of building
a data structure that can be searched in O(1) time.
"""


class HashTable:
    """
    Implements a HashTable data structure. The hash_function
    maps a key to a slot. Each slot stores the key and the data
    corresponding to the key. The HashTable supports the following
    operations: insert, get, remove, contains and len. Collisions
    are solved by rehashing.
    """
    def __init__(self, size):
        r"""Sets the HashTable's size and creates the slots and data lists"""
        self._size = size
        self._slots = [None] * self._size
        self._data = [None] * self._size

    def insert(self, key, data):
        """Inserts a key pointing to the data."""
        hash_value = self._hash_function(key)
        if self._slots[hash_value] in [None, key]:
            self._slots[hash_value] = key
            self._data[hash_value] = data
        else:
            rehash = self._rehash(hash_value)
            while self._slots[rehash] not in [None, key]:
                rehash = self._rehash(rehash)

            if self._slots[rehash] is None:
                self._slots[rehash] = key
                self._data[rehash] = data
            else:
                self._data[rehash] = data  # replace

    def get(self, key):
        """Returns the data associated with the key."""
        hash_value = self._hash_function(key)
        if self._slots[hash_value] == key:
            return self._data[hash_value]

        rehash = self._rehash(hash_value)
        while rehash != hash_value:
            if self._slots[rehash] == key:
                return self._data[rehash]

            rehash = self._rehash(rehash)
            
        return None

    def remove(self, key):
        """Removes the key and the data associated to it."""
        hash_value = self._hash_function(key)
        if self._slots[hash_value] == key:
            self._slots[hash_value] = None
            self._data[hash_value] = None
        else:
            rehash = self._rehash(hash_value)
            while rehash != hash_value:
                if self._slots[rehash] == key:
                    self._slots[rehash] = None
                    self._data[rehash] = None
                    break

                rehash = self._rehash(rehash)

    def contains(self, key):
        """Checks if the HashTable contains the key. Returns Boolean."""
        hash_value = self._hash_function(key)
        if self._slots[hash_value] == key:
            return True

        rehash = self._rehash(hash_value)
        while rehash != hash_value:
            if self._slots[rehash] == key:
                return True

            rehash = self._rehash(rehash)

        return False

    def len(self):
        """Returns the number of keys set in the HashTable."""
        return len(list(filter(lambda x: x is not None, self._slots)))

    def _search(self):
        pass

    def _hash_function(self, key):
        return key % self._size

    def _rehash(self, old_hash):
        return (old_hash + 1) % self._size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.insert(key, data)

if __name__ == "__main__":
    h = HashTable(11)

    h[0] = 'foo'
    h[1] = 'bar'
    h[11] = 'baz'

    print("h[0] = {}\nh[1] = {}\nh[2] = {}".format(h[0], h[1], h[11]))

    print("h contains 0: {}.\nh contains 1: {}.\nh contains 11: {}.".format(h.contains(0), h.contains(1), h.contains(11)))

    h.remove(0)
    h.remove(1)
    h.remove(11)

    print("h[0] = {}\nh[1] = {}\nh[2] = {}".format(h[0], h[1], h[11]))
