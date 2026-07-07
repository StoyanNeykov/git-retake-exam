import pytest
from AgeChecker import is_adult


@pytest.mark.parametrize(
    "age, expected",
    [(19, True)],
)
def test_is_adult(age, expected):
    assert is_adult(age)