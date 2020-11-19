import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, data: dict):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=data)

    def _patch(self, path: str, data: dict):
        return r.patch(url=JSONPLACEHOLDER_HOST + path, data=data)

    #  GET
    @allure.step
    def get_all_posts(self):
        return self._get(path='/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_post_by_user_id(self, user_id: int):
        return self._get(path=f'/posts?userId={user_id}')

    #  POST
    @allure.step
    def add_post(self, data: dict):
        return self._post(path='/posts', data=data)

    #  UPDATE
    def update_post(self, post_id, data: dict):
        return self._patch(path=f'/posts/{post_id}', data=data)
