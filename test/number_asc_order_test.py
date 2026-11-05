import random

import pytest

from src.custom_stack_class import CustomStack
from src.number_asc_order import NumberAscOrder


def test_sort_six_random_mega_sena_numbers_without_changing_stack():
    drawn_numbers = random.sample(range(1, 61), 6)
    stack = CustomStack(6)
    for number in drawn_numbers:
        stack.push(number)

    result = NumberAscOrder().sort(stack)

    assert result == sorted(drawn_numbers)
    assert isinstance(result, list)
    assert stack.size() == 6
    assert stack.top() == drawn_numbers[-1]
    assert [stack.pop() for _ in range(6)] == list(reversed(drawn_numbers))


def test_sort_empty_stack_returns_empty_list():
    stack = CustomStack(6)

    assert NumberAscOrder().sort(stack) == []
    assert stack.is_empty()


def test_sort_rejects_non_custom_stack():
    with pytest.raises(TypeError, match="CustomStack"):
        NumberAscOrder().sort([1, 2, 3, 4, 5, 6])


def test_sort_rejects_stack_with_other_than_six_numbers():
    stack = CustomStack(6)
    for number in range(1, 6):
        stack.push(number)

    with pytest.raises(ValueError, match="exatamente seis"):
        NumberAscOrder().sort(stack)


def test_sort_rejects_non_integer_numbers():
    stack = CustomStack(6)
    for number in (1, 2, 3, 4, 5, "6"):
        stack.push(number)

    with pytest.raises(TypeError, match="inteiros"):
        NumberAscOrder().sort(stack)


@pytest.mark.parametrize("out_of_range", [0, 61])
def test_sort_rejects_numbers_outside_mega_sena_range(out_of_range):
    stack = CustomStack(6)
    for number in (out_of_range, 2, 3, 4, 5, 6):
        stack.push(number)

    with pytest.raises(ValueError, match="entre 1 e 60"):
        NumberAscOrder().sort(stack)


def test_sort_rejects_repeated_numbers():
    stack = CustomStack(6)
    for number in (1, 2, 3, 4, 5, 5):
        stack.push(number)

    with pytest.raises(ValueError, match="não podem se repetir"):
        NumberAscOrder().sort(stack)
