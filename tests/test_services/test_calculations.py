import pytest

from app.services.calculations import calculate_cross_sums

class TestCalculations:
    def test_with_solvable_values(self):
        assert calculate_cross_sums([1, 2], [0, 3], [[1, 1], [5, 2]], [[1, 5], [1, 2]]) == [[0, 1], [0, 1]]

    def test_with_unsolvable_values(self):
        with pytest.raises(ValueError) as excinfo:
            calculate_cross_sums([0, 2], [0, 3], [[1, 1], [5, 2]], [[1, 5], [1, 2]])
        assert str(excinfo.value) == "Solution not found"