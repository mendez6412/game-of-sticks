import unittest
from sticks import *
from sticks_ai import AI

def test_is_input_valid():
    assert is_input_valid(10) == 10
    assert is_input_valid('a') == False
    assert is_input_valid(8) == False

def test_ai_creates_dict():
    test_comp = AI(100)

    assert type(test_comp.hats) == dict

def test_ai_creates_correct_length_dictionary():
    test_comp = AI(100)

    assert len(test_comp.hats) == 100

def test_comp_turn():
    test_comp = AI(10)

    assert test_comp.comp_turn(5) in [1, 2, 3]
