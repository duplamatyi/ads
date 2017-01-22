"""Sorting algorithms in Python"""

import copy


class Sorter:
    @staticmethod
    def bubble_sort(lst):
        """The greatest item bubbles to the top in each iteration"""
        lst = copy.deepcopy(lst)
        for i in range(len(lst) - 1, 0, -1):
            ordered = True
            for j in range(i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    ordered = False

            if ordered is True:
                break

        return lst

    @staticmethod
    def selection_sort(lst):
        """The greatest element is always paced to the right location"""
        lst = copy.deepcopy(lst)
        for i in range(len(lst) - 1, 0, -1):
            pos_max = 0
            for j in range(1, i + 1):
                if lst[pos_max] < lst[j]:
                    pos_max = j

            lst[pos_max], lst[i] = lst[i], lst[pos_max]

        return lst

    @staticmethod
    def insertion_sort(lst):
        r"""The current element gets always inserted in it's
        position in an already sorted sub list.
        """
        lst = copy.deepcopy(lst)
        for i in range(1, len(lst)):
            pos = i
            current = lst[i]

            while pos > 0 and lst[pos - 1] > current:
                lst[pos - 1], lst[pos] = lst[pos], lst[pos - 1]
                pos -= 1

            lst[pos] = current

        return lst

    @classmethod
    def shell_sort(cls, lst):
        """Sorts sub lists with a gap using insertion sort, until gap is 1.
        This version uses a gap sequence len(list) // 2
        """
        lst = copy.deepcopy(lst)
        gap = len(lst) // 2
        while gap > 0:
            for start_pos in range(gap):
                cls._gap_insertion_sort(lst, start_pos, gap)

            gap //= 2

        return lst

    @staticmethod
    def _gap_insertion_sort(lst, start_pos, gap):
        for i in range(start_pos + gap, len(lst), gap):
            pos = i
            current = lst[i]

            while pos > 0 and lst[pos - gap] > current:
                lst[pos - gap], lst[pos] = lst[pos], lst[pos - gap]
                pos -= gap

            lst[pos] = current

    @classmethod
    def merge_sort(cls, lst):
        """Uses divide et impera: sorts parts and than merges them together"""
        lst = copy.deepcopy(lst)

        return cls._merge_sort_helper(lst)

    @classmethod
    def _merge_sort_helper(cls, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_half = lst[:mid]
            right_half = lst[mid:]
            cls._merge_sort_helper(left_half)
            cls._merge_sort_helper(right_half)

            i = 0
            j = 0
            k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    lst[k] = left_half[i]
                    i += 1
                else:
                    lst[k] = right_half[j]
                    j += 1

                k += 1

            while i < len(left_half):
                lst[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                lst[k] = right_half[j]
                j += 1
                k += 1

        return lst

    @classmethod
    def quick_sort(cls, lst):
        """Selects a pivot element, places in place. Sorts the two sub lists."""
        lst = copy.deepcopy(lst)
        cls._quick_sort_helper(lst, 0, len(lst) - 1)

        return lst

    @classmethod
    def _quick_sort_helper(cls, lst, first, last):
        if first < last:
            split_point = cls._partition(lst, first, last)

            cls._quick_sort_helper(lst, first, split_point - 1)
            cls._quick_sort_helper(lst, split_point + 1, last)

    @staticmethod
    def _partition(lst, first, last):
        pivot = lst[first]
        left_mark = first + 1
        right_mark = last

        done = False
        while not done:
            while left_mark <= right_mark and lst[left_mark] <= pivot:
                left_mark += 1

            while left_mark <= right_mark and lst[right_mark] >= pivot:
                right_mark -= 1

            if right_mark < left_mark:
                done = True
            else:
                lst[left_mark], lst[right_mark] = lst[right_mark], lst[left_mark]

        lst[first], lst[right_mark] = lst[right_mark], lst[first]

        return right_mark


if __name__ == '__main__':
    a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(a)
    print(sorted(a))
    print(Sorter.bubble_sort(a))
    print(Sorter.selection_sort(a))
    print(Sorter.insertion_sort(a))
    print(Sorter.shell_sort(a))
    print(Sorter.merge_sort(a))
    print(Sorter.quick_sort(a))
