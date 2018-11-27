from unittest import TestCase

from task_4 import swap_case

"""Blackbox Testing:
    What needs to be tested:
    - input is a string or None
    - Empty string is returned empty
    - Test multiple example"""

class Task4Test(TestCase):
    """
    Task 4: Swap case
    """
    def test_input_none(self):
        self.assertEquals(None, swap_case(None)) #input: None --> Output: None

    def test_input_string(self):
        self.assertTrue(type(swap_case)==str) #the input must be a string

if __name__ == "__main__":
    assert swap_case() == ()
    assert swap_case("The DOG is called AMY") == ("tHE dog IS CALLED amy")
