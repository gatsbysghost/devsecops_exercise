import unittest

from sort_two_lists import sort_two_lists

class SortTwoListsTest(unittest.TestCase):
    def test_merges_two_sorted_lists(self):
        self.assertEqual(sort_two_lists([1, 2, 7, 9], [3, 6, 8]), [1, 2, 3, 6, 7, 8, 9])

    def test_merges_two_sorted_lists_with_duplicate_values(self):
        self.assertEqual(sort_two_lists([6, 8, 9], [1, 4, 6]), [1, 4, 6, 6, 8, 9])

    def test_merges_one_sorted_list_and_one_empty_array(self):
        self.assertEqual(sort_two_lists([], [1, 2, 3]), [1, 2, 3])

    def test_safe_exit_if_first_list_is_unsorted(self):
        with self.assertRaisesWithMessage(ValueError):
            sort_two_lists([2, 1, 3], [4, 5, 6])

    def test_safe_exit_if_second_list_is_unsorted(self):
        with self.assertRaisesWithMessage(ValueError):
            sort_two_lists([1, 2, 3], [6, 5, 4])

    def test_safe_exit_if_lists_contain_non_numerics(self):
        with self.assertRaisesWithMessage(ValueError):
            sort_two_lists([1, 'b', 3], [4, 5, 6])

    def test_safe_exit_if_one_arg_is_not_a_list(self):
        with self.assertRaisesWithMessage(ValueError):
            sort_two_lists(1, [2, 3, 4])

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
