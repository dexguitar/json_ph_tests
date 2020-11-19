import allure
import pytest


@allure.suite('UPDATE /posts')
@pytest.mark.usefixtures('client', 'checker')
class TestUpdatePosts:

    @allure.title('Positive. Update post by ID')
    @pytest.mark.parametrize('post_id, data', [
        (1, {'id': 123, 'title': 'Article 144 Updated Title', 'body': 'Article 144 Updated Body'}),
        (99, {'id': 'wow', 'title': 3.14, 'body': 'Article 144 Updated Body'}),
        (56, {'id': 0, 'title': 23, 'body': 'Article 144 Updated Body'}),
    ])
    def test_update_post(self, client, checker, post_id: int, data: dict):
        response = client.update_post(post_id=12, data=data)
        checker.check_update_post_response(response, post_id=12, **data)

    @allure.title('Negative. Update post by ID')
    @pytest.mark.parametrize('post_id, data', [
        (0, {'id': 123, 'title': 'Article 144 Updated Title', 'body': 'Article 144 Updated Body'}),
        (101, {'id': 'wow', 'title': 12.76, 'body': 'Article 144 Updated Body'}),
        (3.14, {'id': 0, 'title': 23, 'body': 'Article 144 Updated Body'}),
    ])
    def test_negative_update_post(self, client, checker, post_id: int, data: dict):
        data = {'id': 99, 'title': 'Out Of Range Title Update', 'body': 'Out Of Range Body Update'}
        response = client.update_post(post_id=0, data=data)
        checker.check_update_post_response(response, post_id=0, **data)
