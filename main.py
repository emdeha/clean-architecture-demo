from fastapi import FastAPI

from repository.users import UsersJson
from usecase.list_users import ListUsers

app = FastAPI()


list_users = ListUsers(UsersJson("./users.json"))


@app.get("/")
def read_root():
    return list_users.run()