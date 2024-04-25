import pytest


@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataLoad():
    print("Data is being created")
    return ["Akshay", "Ganjiwale"]


@pytest.fixture(params=[("chrome", "Akshay", "Ganjiwale"), ("firefox", "Akshay"), ("IE", "AG")])
def crossBrowser(request):
    print(request)
    return request.param
