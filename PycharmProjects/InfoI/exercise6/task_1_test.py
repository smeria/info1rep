from unittest import TestCase

from task_1 import quick_sort

""" Only look at the cases with numbers. Strings, Tuples etc. can be ignored.
    Cases that have to be tested are:
    - Empty list - should return a empty list
    - single values - should return a list with the same single value
    - unsorted values - should return a list with sorted values
    - None
    - List of Floats and integers"""

class Task1Test(TestCase):
    """
    Task 1: Quicksort
    """
    def test_empty_list(self):
        # Tests if a sorted empty list is returned as empty list
        self.assertEquals([], quick_sort([]),"A empty list must return empty list")

    def test_none_list(self):
        # Tests if a list containing None returns None
        self.assertEquals([None], quick_sort([None]), "A list containing nothing should return a list containing nothing!")

    def test_returns_sorted_list(self):
        # Test if a unsorted list is returned sorted
        self.assertTrue(quick_sort([6,7,4,3,2])==sorted([6,7,4,3,2], reversed=True), "Your code does not return a sorted list.")

    def test_single_value_list(self):
        # Tests if a list with one value is returned unchanged
        self.assertEquals(quick_sort(self))

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    assert quick_sort([-1,2,-3,4,-1,4,5]) == [-3,-1,-1,2,4,4,5]
    assert quick_sort([2,2,2]) == [2,2,2]
    assert quick_sort([2.1, 4.3, 1.2, 3,5,2.1]) == [1.2,2.1,2.1,3.5,4.3]
