#!/usr/bin/env python3
# 00. Sort a sequence of integers

# Sort from less to more

# first try
import unittest


def insertion_sort(_list):
    len_list = len(_list)

    if len_list < 2:
        return _list
    if len_list == 2:
        return [_list[0], _list[1]] if _list[0] < _list[1] else [_list[1], _list[0]]
    if len_list > 2:
        # Insertion-sort
        for j in range(1, len(_list)):
            key = _list[j]
            # insert _list[j] into the sorted seq _list[0...j]
            i = j - 1
            while i > -1 and _list[i] > key:
                _list[i + 1] = _list[i]
                i = i - 1
            _list[i + 1] = key

        return _list


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([4, 1, 2, 2, 7]), [1, 2, 2, 4, 7])
        self.assertEqual(insertion_sort([5, 3, 1, 4, 2]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([2, 1]), [1, 2])
        self.assertEqual(insertion_sort([1, 2]), [1, 2])


if __name__ == "__main__":
    unittest.main()

# TODO: merge_sort
