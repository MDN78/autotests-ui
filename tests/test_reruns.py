import random

import pytest


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Перезапуски реализуются на уровне маркировки flaky
def test_reruns():
    assert random.choice([True, False])


# tests run 'python -m pytest -k "test_reruns" -s -v'


@pytest.mark.flaky(reruns=3, reruns_delay=2)
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])

# tests run 'python -m pytest -k "TestReruns" -s -v'
