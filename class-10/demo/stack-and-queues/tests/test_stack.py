from stack_and_queues.stack  import Stack
from stack_and_queues.node import Node

import pytest

def test_push(stack_3_vals):
    actual = stack_3_vals.top.value
    expected = 'd'
    assert actual == expected

def test_pop(stack_3_vals):
    actual = stack_3_vals.pop()
    expected = 'd'
    assert actual == expected
    assert stack_3_vals.top == -7

def test_peek(stack_3_vals):
    actual = stack_3_vals.peek()
    expected = 'd'
    assert actual == expected
    assert stack_3_vals.top == 'd'

def test_is_empty(stack_3_vals):
    assert stack_3_vals.is_empty() == False


# Decorator
@pytest.fixture
def stack_3_vals():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    return stack


