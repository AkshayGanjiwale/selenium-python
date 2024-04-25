import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_firstProgram1(self):
        print("Hello")

    def test_firstProgram2(self):
        print("Hello")

    def test_firstProgram3(self):
        print("Hello")

    def test_firstProgram4(self):
        print("Hello")


