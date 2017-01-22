from python.sorting.sorting import Sorter


class TestClass:
    def test_bubble_sort(self):
        assert [] == Sorter.bubble_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.bubble_sort(a) == sorted(a)

    def test_selection_sort(self):
        assert [] == Sorter.selection_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.selection_sort(a) == sorted(a)

    def test_insertion_sort(self):
        assert [] == Sorter.insertion_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.insertion_sort(a) == sorted(a)

    def test_shell_sort(self):
        assert [] == Sorter.shell_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.shell_sort(a) == sorted(a)

    def test_merge_sort(self):
        assert [] == Sorter.merge_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.merge_sort(a) == sorted(a)

    def test_quick_sort(self):
        assert [] == Sorter.quick_sort([])
        a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        assert Sorter.quick_sort(a) == sorted(a)
