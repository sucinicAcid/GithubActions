import unittest
from main import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unsorted_array(self):
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element_array(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_duplicate_elements(self):
        self.assertEqual(bubble_sort([4, 2, 2, 1]), [1, 2, 2, 4])

if __name__ == "__main__":
    unittest.main()
