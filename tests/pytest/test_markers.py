import pytest


@pytest.mark.smoke
def test_smoke_case():
    pass


@pytest.mark.regression
def test_regression_case():
    pass


@pytest.mark.smoke
class TestSuite:

    @pytest.mark.some
    def test_smoke_case_2(self):
        pass

    def test_regression_case_2(self):
        pass


@pytest.mark.regression
class TestUserAuthentication:

    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass