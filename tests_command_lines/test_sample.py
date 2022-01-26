import pytest


class TestDemo:
    def test_secret_auth(self, auth):
        print("\nmy auth are {}".format(auth))
        assert True
