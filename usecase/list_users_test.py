import unittest

from usecase import list_users


class TestListUsers(unittest.TestCase):
    def test_lists_all_users(self):
        self.assertEqual(len(list_users.run()), 2)
