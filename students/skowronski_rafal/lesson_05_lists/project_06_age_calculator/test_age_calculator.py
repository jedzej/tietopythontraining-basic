import pytest
from age_calculator import get_adults_average_age
from age_calculator import get_children_average_age


class TestAgeCalculator:
    test_data = [
        (
            [],
            None,
            None
        ),
        (
            [1, 2, 3],
            None,
            2
        ),
        (
            [18, 19, 20],
            19,
            None
        ),
        (
            [1, 2, 3, 18, 19, 20],
            19,
            2
        ),
    ]

    @pytest.mark.parametrize(
        'ages, average_adults, average_children', test_data)
    def test_get_adults_average_age_on_test_data(
            self,
            ages,
            average_adults,
            average_children):
        assert get_adults_average_age(ages) == average_adults

    @pytest.mark.parametrize(
        'ages, average_adults, average_children', test_data)
    def test_get_children_average_age_on_test_data(
            self,
            ages,
            average_adults,
            average_children):
        assert get_children_average_age(ages) == average_children
