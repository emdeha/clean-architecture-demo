import unittest

from repository import users
from usecase.list_users import ListUsers, User


class TestListUsers(unittest.TestCase):
    def test_lists_no_users_when_no_users_in_repository(self):
        list_users = ListUsers(users.UsersHardcoded([]))
        self.assertEqual(0, len(list_users.run()))

    def test_lists_many_users_when_many_users_in_repository(self):
        list_users = ListUsers(users.UsersHardcoded([
            User("joe", "joe@test.com", "0048123123"),
            User("peter", "peter@test.com", "0045123123")
        ]))
        self.assertEqual(2, len(list_users.run()))

    def test_lists_many_users_from_json(self):
        list_users = ListUsers(users.UsersJson("./test_users.json"))
        users_list = list_users.run()
        self.assertListEqual(
            list(map(vars, [
                User("joe", "joe@test.com", "0048123123"),
                User("peter", "peter@test.com", "0045123123")
            ])),
            list(map(vars, users_list))
        )
