from stack_and_queues.queue import Queue
from stack_and_queues.node import Node

import pytest


def test_enqueue(queue_vals):
    assert queue_vals.rear.value == 6
    assert queue_vals.front.value == 8

def test_dequeue(queue_vals):
    data = queue_vals.dequeue()
    assert data == 8
    assert queue_vals.front.value == 'hi'

def test_peek(queue_vals):
    pass

def test_is_empty(queue_vals):
    pass

""" Notes
6 <- -4 <- 'hi' <- 8
                   F
R

"""

# Decorator
@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue


