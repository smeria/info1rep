from unittest import TestCase

from task_2 import list_duplicates

"""Cases that have to be tested:
    Structural:
    - Output is a list
    - Empty list returns empty list
    - Check if elements in lists are tuples
    Content of list:
    - negative values
    - three equal values
    - floats
    """

class Task2Test(TestCase):
    """
    Task 2: List duplicates
    """
    def test_is_list(self):
        self.assertTrue(type(list_duplicates)==list)

    def test_empty_list(self):
        self.assertEquals([], list_duplicates([]), "A empty list must return empty list")

    def test_tuples_in_list(self):
        for i in len(list_duplicates):
            self.assertTrue(type(i)==tuple)


if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    assert list_duplicates([-1,2,-3,4,-1,4,5]) == [(-1,(0,4)),(4,(3,5))]
    assert list_duplicates([2,2,2]) == [(2, (0, 1,2))]
    assert list_duplicates([2.1, 4.3, 1.2, 3,5,2.1]) == [(2.1, (0,5))]
