import pytest
from fine_calculator import calculate_fine

def test_zero_days():
    assert calculate_fine(0) == 0

@pytest.mark.parametrize("days, expected", [
    (1, 5),      # boundary: smallest overdue
    (5, 25),     # valid
    (10, 50),    # valid
    (30, 150),   # larger value
])
def test_valid_days(days, expected):
    assert calculate_fine(days) == expected

@pytest.mark.parametrize("bad_input", [-1, -10, "abc", None, 2.5])
def test_invalid_days(bad_input):
    with pytest.raises(ValueError):
        calculate_fine(bad_input)