import allure
import pytest


@allure.suite('GET /posts')
@pytest.mark.usefixtures('client', 'checker')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self, client, checker):
        response = client.get_all_posts()
        checker.check_get_all_posts_response(response)

    @allure.title('Positive. Get post by post ID')
    @pytest.mark.parametrize('post_id', [1, 17, 35, 68, 100])
    def test_get_post_by_id(self, client, checker, post_id: int):
        response = client.get_post_by_id(post_id)
        checker.check_get_post_by_id_response(response, post_id)

    @allure.title('Negative. Get post by post ID')
    @pytest.mark.parametrize('post_id', [0, 101, 99.5, 12.5, 1000001])
    def test_negative_get_post_by_id(self, client, checker, post_id: int):
        response = client.get_post_by_id(post_id)
        checker.check_get_post_by_id_response(response, post_id)

    @allure.title('Positive. Get post by user ID')
    @pytest.mark.parametrize('user_id', [1, 3, 5, 7, 10])
    def test_get_post_by_user_id(self, client, checker, user_id: int):
        response = client.get_post_by_user_id(user_id)
        checker.check_get_post_by_user_id_response(response, user_id)

    @allure.title('Negative. Get post by user id')
    @pytest.mark.parametrize('user_id', [0, 11, 100, 12.1234, 3.14])
    def test_negative_get_post_by_user_id(self, client, checker, user_id: int):
        response = client.get_post_by_user_id(user_id)
        checker.check_get_post_by_user_id_response(response, user_id)
