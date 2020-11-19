import allure
import pytest
from hamcrest import assert_that, equal_to
from requests import codes
import json


class Checker:

    def _response_general_check(self, response, expected_code=codes.ok):
        assert_that(response.status_code, equal_to(expected_code),
                    f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')

    def _response_headers_check(self, response, expected_headers='application/json; charset=utf-8'):
        actual_response_headers = response.headers['Content-Type']
        assert_that(actual_response_headers, equal_to(expected_headers),
                    f'Expected response headers: {expected_headers}. Actual response headers: '
                    f'{actual_response_headers}.'
                    f'Url: {response.url}')

    def _response_body_length_check(self, response, expected_length=0):
        assert_that(len(response.json()), equal_to(expected_length),
                    f'Expected response length: {expected_length}. Actual response length: {len(response.json())}.'
                    f'Url: {response.url}')

    @allure.step
    def check_get_all_posts_response(self, response):
        self._response_general_check(response)
        self._response_headers_check(response)
        self._response_body_length_check(response, expected_length=100)

    @allure.step
    @pytest.mark.parametrize('post_id', [])
    def check_get_post_by_id_response(self, response, post_id: int):
        self._response_headers_check(response)
        if post_id < 1 or post_id > 100 or not isinstance(post_id, int):
            self._response_general_check(response, expected_code=codes.not_found)
            self._response_body_length_check(response)
        else:
            self._response_general_check(response, expected_code=codes.ok)
            self._response_body_length_check(response, expected_length=4)
            res = json.loads(response.text)
            assert_that(res['id'], equal_to(post_id))

    @allure.step
    def check_get_post_by_user_id_response(self, response, user_id: int):
        self._response_general_check(response, expected_code=codes.ok)
        self._response_headers_check(response)

        if user_id < 1 or user_id > 10 or not isinstance(user_id, int):
            self._response_body_length_check(response)
        else:
            self._response_body_length_check(response, expected_length=10)
            [assert_that(i['userId'], equal_to(user_id)) for i in response.json()]

    @allure.step
    def check_add_post_response(self, response, **kwargs):
        self._response_general_check(response, expected_code=codes.created)
        self._response_headers_check(response)
        self._response_body_length_check(response, expected_length=(len(kwargs) + 1))

        res = json.loads(response.text)
        assert_that(res['id'], equal_to(101))

        for k, v in kwargs.items():
            assert_that(res[k], equal_to(str(v)))

    @allure.step
    def check_update_post_response(self, response, post_id, **kwargs):
        self._response_general_check(response, expected_code=codes.ok)
        self._response_headers_check(response)

        if post_id < 1 or post_id > 100:
            self._response_body_length_check(response, expected_length=(len(kwargs)))
        elif 1 <= post_id <= 100:
            self._response_body_length_check(response, expected_length=(len(kwargs) + 1))

        res = json.loads(response.text)
        for k, v in kwargs.items():
            assert_that(res[k], equal_to(str(v)))
