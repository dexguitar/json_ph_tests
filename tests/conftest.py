import pytest
from framework.client import Client
from framework.checker import Checker


@pytest.fixture(scope='module')
def client():
    return Client()


@pytest.fixture(scope='module')
def checker():
    return Checker()
