import json
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from repository import users
from usecase.list_users import ListUsers

from rest_api.users import UsersRestApi
from usecase.promote_user import PromoteUser


class TestPromoteUser(unittest.TestCase):
    def tearDown(self):
        with open("test_users.json", "w") as test_users:
            json.dump([
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123"}
            ], indent=2, fp=test_users)

    def test_user_without_promotion_becomes_developer(self):
        promote_user_usecase = PromoteUser(users.UsersJson("./test_users.json"))
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        list_users_response = self.do_list_user_request()
        self.assertListEqual(
            [
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123", "promotion": "DEVELOPER"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123", "promotion": None}
            ],
            list_users_response.json()
        )

    def test_promoted_developer_becomes_manager(self):
        promote_user_usecase = PromoteUser(users.UsersJson("./test_users.json"))
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        list_users_response = self.do_list_user_request()
        self.assertListEqual(
            [
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123", "promotion": "MANAGER"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123", "promotion": None}
            ],
            list_users_response.json()
        )

    def test_cannot_promote_manager_further(self):
        promote_user_usecase = PromoteUser(users.UsersJson("./test_users.json"))
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        promote_user_response = self.do_promote_user_request(
            promote_user_usecase,
        )
        self.assertEqual(promote_user_response.status_code, 204)
        list_users_response = self.do_list_user_request()
        self.assertListEqual(
            [
                {"name": "joe", "email": "joe@test.com", "phone": "0048123123", "promotion": "MANAGER"},
                {"name": "peter", "email": "peter@test.com", "phone": "0045123123", "promotion": None}
            ],
            list_users_response.json()
        )

    @staticmethod
    def do_promote_user_request(promote_user_usecase: PromoteUser):
        users_rest_api = UsersRestApi(ListUsers(users.UsersJson("./test_users.json")), promote_user_usecase)
        app = FastAPI()
        app.include_router(users_rest_api.router)
        client = TestClient(app)
        return client.patch("/user/joe@test.com/promote")

    @staticmethod
    def do_list_user_request():
        users_rest_api = UsersRestApi(ListUsers(users.UsersJson("./test_users.json")), PromoteUser(users.UsersJson("./test_users.json")))
        app = FastAPI()
        app.include_router(users_rest_api.router)
        client = TestClient(app)
        return client.get("/")
