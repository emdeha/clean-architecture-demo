import json
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from repository import users
from usecase.list_users import ListUsers, User

from rest_api.users import UsersRestApi


class TestListUsers(unittest.TestCase):
    def test_lists_no_users_when_no_users_in_repository(self):
        list_users_usecase = ListUsers(users.UsersHardcoded([]))
        users_response = self.do_request(list_users_usecase)
        self.assertEqual(200, users_response.status_code)
        self.assertEqual([], users_response.json())

    def test_lists_many_users_when_many_users_in_repository(self):
        list_users_usecase = ListUsers(users.UsersHardcoded([
            User("joe", "joe@test.com", "0048123123"),
            User("peter", "peter@test.com", "0045123123")
        ]))
        users_response = self.do_request(list_users_usecase)
        self.assertEqual(users_response.status_code, 200)
        self.assertListEqual(
            [
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123"}
            ],
            users_response.json()
        )

    def test_lists_many_users_from_json(self):
        list_users_usecase = ListUsers(users.UsersJson("./test_users.json"))
        users_response = self.do_request(list_users_usecase)
        self.assertEqual(users_response.status_code, 200)
        self.assertListEqual(
            [
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123"}
            ],
            users_response.json()
        )

    def do_request(self, list_users_usecase: ListUsers):
        users_rest_api = UsersRestApi(list_users_usecase)
        app = FastAPI()
        app.include_router(users_rest_api.router)
        client = TestClient(app)
        return client.get("/")
