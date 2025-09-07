import pytest


def test_first_try():
    print("Hello World!")


def test_assert_positive_case():
    assert (2 + 2) == 4


@pytest.mark.xfail(raises=AssertionError)
def test_assert_negative_case():
    assert (2 + 2) == 5
