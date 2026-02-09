import pytest

from faker import Faker


class TestOneOfProvider:
    """Test one_of provider methods"""

    num_samples = 100

    def test_one_of_returns_string_from_elements(self, faker, num_samples):
        elements = ("apple", "banana", "cherry")
        for _ in range(num_samples):
            result = faker.one_of(elements)
            assert isinstance(result, str)
            assert result in elements

    def test_one_of_with_list(self, faker, num_samples):
        elements = ["red", "green", "blue"]
        for _ in range(num_samples):
            result = faker.one_of(elements)
            assert isinstance(result, str)
            assert result in elements

    def test_one_of_single_element(self, faker, num_samples):
        elements = ["only_option"]
        for _ in range(num_samples):
            result = faker.one_of(elements)
            assert result == "only_option"

    def test_one_of_empty_elements_raises_error(self, faker):
        with pytest.raises(ValueError) as excinfo:
            faker.one_of([])
        assert str(excinfo.value) == "Elements cannot be empty"

    def test_one_of_empty_tuple_raises_error(self, faker):
        with pytest.raises(ValueError) as excinfo:
            faker.one_of(())
        assert str(excinfo.value) == "Elements cannot be empty"

    def test_one_of_non_string_element_raises_error(self, faker):
        with pytest.raises(ValueError) as excinfo:
            faker.one_of(["valid", 123, "also_valid"])
        assert str(excinfo.value) == "All elements must be strings"

    def test_one_of_integer_element_raises_error(self, faker):
        with pytest.raises(ValueError) as excinfo:
            faker.one_of([1, 2, 3])
        assert str(excinfo.value) == "All elements must be strings"

    def test_one_of_none_element_raises_error(self, faker):
        with pytest.raises(ValueError) as excinfo:
            faker.one_of(["valid", None])
        assert str(excinfo.value) == "All elements must be strings"

    def test_one_of_seedability(self, faker, num_samples):
        elements = ("option1", "option2", "option3", "option4", "option5")
        for _ in range(num_samples):
            random_seed = faker.random_int()
            faker.seed_instance(random_seed)
            expected_values = [faker.one_of(elements) for _ in range(100)]
            faker.seed_instance(random_seed)
            new_values = [faker.one_of(elements) for _ in range(100)]
            assert new_values == expected_values

    def test_one_of_distribution(self, faker):
        elements = ("a", "b", "c")
        results = {e: 0 for e in elements}
        iterations = 10000

        for _ in range(iterations):
            result = faker.one_of(elements)
            results[result] += 1

        # Each element should appear roughly 1/3 of the time
        # Allow for some variance (between 25% and 40%)
        for element in elements:
            ratio = results[element] / iterations
            assert 0.25 < ratio < 0.40, f"Element '{element}' appeared {ratio*100:.1f}% of the time"
