from hashing import HashTable


class TestHashTable:
    def test_insert(self):
        h = HashTable(11)
        h[0] = 0
        h[1] = 1
        h[11] = 11
        assert h[0] == 0
        assert h[1] == 1
        assert h[2] is None
        assert h[11] == 11

    def test_remove(self):
        h = HashTable(11)
        h[0] = 0
        h[11] = 11
        h.remove(0)
        h.remove(11)
        assert h[0] is None
        assert h[11] is None

    def test_contains(self):
        h = HashTable(11)
        h[0] = 0
        h[11] = 11
        assert h.contains(0) is True
        assert h.contains(1) is False
        assert h.contains(11) is True

    def test_len(self):
        h = HashTable(11)
        assert h.len() == 0
        h[0] = 0
        h[11] = 11
        assert h.len() == 2
