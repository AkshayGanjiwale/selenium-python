# pytest file name starts with test_ or ends with _test
# pytest method name should start with test
# Any method should be wrapped in method only
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_greet(setup):
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])