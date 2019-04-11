import unittest
from lab1 import *

list1 = [1,23, 42, 4, 2, 9]
list2 = [1,2,3,4,5,6,7,98]
list3 = [1, 4, 6, 7, 12, 45]

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        ''' These tests cases test to make sure that the real max number
            shows up'''
        self.assertEqual(max_list_iter(list1), 42)
        self.assertEqual(max_list_iter(list2), 98)
        self.assertEqual(max_list_iter(list3), 45)

    def test_reverse_rec(self):
        ''' tests to see if the function properly reverses the lists '''
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec(list1), [9,2,4,42,23,1])
        self.assertEqual(reverse_rec(list2), [98,7,6,5,4,3,2,1])
        self.assertEqual(reverse_rec(list3), [45,12,7,6,4,1])
        self.assertEqual(reverse_rec([]), [])
        with self.assertRaises(ValueError):
            reverse_rec(None)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        ''' tests to make sure that the function runs and checks what happens
            if the number isn't in the list'''
        self.assertEqual(bin_search(4, 0, len(list2), list2), 3)
        self.assertEqual(bin_search(-1, 0, len(list3), list3), None)
        self.assertEqual(bin_search(7, 0, len(list3), list3), 3)
        self.assertEqual(bin_search(98, 0, len(list2), list2), 7)


if __name__ == "__main__":
        unittest.main()
