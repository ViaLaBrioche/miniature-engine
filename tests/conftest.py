import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--dog-base-url",
        action="store",
        default="https://dog.ceo/api",
    )

    parser.addoption(
        "--openbrewery-base-url",
        action="store",
        default="https://api.openbrewerydb.org",
    )

    parser.addoption(
        "--jsonplaceholder-base-url",
        action="store",
        default="https://jsonplaceholder.typicode.com",
    )

    parser.addoption("--url", action="store", default="https://ya.ru")

    parser.addoption("--status-code", action="store", default=200, type=int)


@pytest.fixture
def dog_base_url(request):
    return request.config.getoption("--dog-base-url")


@pytest.fixture
def openbrewery_base_url(request):
    return request.config.getoption("--openbrewery-base-url")


@pytest.fixture
def jsonplaceholder_base_url(request):
    return request.config.getoption("--jsonplaceholder-base-url")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status-code")
