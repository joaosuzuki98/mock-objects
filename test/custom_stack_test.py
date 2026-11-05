import pytest

from src.custom_stack_class import (
    CustomStack,
    StackEmptyException,
    StackFullException,
)


def test_new_stack_is_empty_and_has_size_zero():
    stack = CustomStack(3)

    assert stack.size() == 0
    assert stack.is_empty()


def test_push_adds_element_and_top_does_not_remove_it():
    stack = CustomStack(3)

    stack.push(5.0)

    assert stack.size() == 1
    assert not stack.is_empty()
    assert stack.top() == 5.0
    assert stack.size() == 1


def test_pop_returns_elements_in_last_in_first_out_order():
    stack = CustomStack(2)
    stack.push("first")
    stack.push("last")

    assert stack.pop() == "last"
    assert stack.top() == "first"
    assert stack.pop() == "first"
    assert stack.is_empty()


def test_push_raises_when_stack_is_full_without_changing_it():
    stack = CustomStack(1)
    stack.push("only element")

    with pytest.raises(StackFullException):
        stack.push("overflow")

    assert stack.size() == 1
    assert stack.top() == "only element"


def test_push_raises_when_stack_has_zero_capacity():
    stack = CustomStack(0)

    with pytest.raises(StackFullException):
        stack.push("cannot be stored")

    assert stack.is_empty()


@pytest.mark.parametrize("operation", ["pop", "top"])
def test_read_or_remove_from_empty_stack_raises(operation):
    stack = CustomStack(1)

    with pytest.raises(StackEmptyException):
        getattr(stack, operation)()
