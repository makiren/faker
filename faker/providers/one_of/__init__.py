from typing import Sequence

from .. import BaseProvider


class Provider(BaseProvider):
    """Provider for randomly selecting one value from a list of string candidates."""

    def one_of(self, elements: Sequence[str]) -> str:
        """Randomly select and return one string from the provided list of candidates.

        All elements must be strings. If an empty sequence is provided, a ValueError
        will be raised.

        :param elements: A sequence of string values to choose from.
        :return: A randomly selected string from the provided elements.
        :raises ValueError: If elements is empty or contains non-string values.

        :sample: elements=('apple', 'banana', 'cherry')
        :sample: elements=['red', 'green', 'blue']

        Example:
            >>> from faker import Faker
            >>> fake = Faker()
            >>> fake.one_of(['option1', 'option2', 'option3'])
            'option2'
        """
        if not elements:
            raise ValueError("Elements cannot be empty")

        for element in elements:
            if not isinstance(element, str):
                raise ValueError("All elements must be strings")

        return self.random_element(elements)
