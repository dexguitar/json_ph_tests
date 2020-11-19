import allure
import pytest


@allure.suite('POST /posts')
@pytest.mark.usefixtures('client', 'checker')
class TestPostPosts:

    @allure.title('Positive. Add post')
    @pytest.mark.parametrize('data', [
        {'user_id': 17, 'title': "How to build a rocket", 'body': "E. Musk was here"},
        {'user_id': 11, 'title': 567, 'body': "Some new post"},
        {'user_id': 101, 'title': "Ridin' huskies in Swiss alps", 'body': "Post body about huskies"},
    ])
    def test_add_post(self, client, checker, data: dict):
        response = client.add_post(data)
        checker.check_add_post_response(response, **data)

    @allure.title('Negative. Add post')
    @pytest.mark.parametrize('data', [
        {'user_id': 0, 'title': 345, 'body': "E. Musk was here"},
        {'something': 11, 'other_thing': "Some new post", 'how_are_you': "Some new post"},
        {},
    ])
    def test_negative_add_post(self, client, checker, data: dict):
        response = client.add_post(data)
        checker.check_add_post_response(response, **data)
