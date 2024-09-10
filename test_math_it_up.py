import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(3589742) == True
  assert math_it_up.is_even(-194569) == False
  assert math_it_up.is_even(-46) == True
  assert math_it_up.is_even(4) == True
  assert math_it_up.is_even(385728987) == False
  assert math_it_up.is_even(-7) == False

def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(29375875) == True
  assert math_it_up.is_odd(-234776) == False
  assert math_it_up.is_odd(-35) == True
  assert math_it_up.is_odd(3) == True
  assert math_it_up.is_odd(877561874) == False
  assert math_it_up.is_odd(-7) == True

def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([1, 1, 1, 1, 1, 1]) == 1
  assert math_it_up.mean([9, 1, 5]) == 5
  assert math_it_up.mean([2467]) == 2467

def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([1, 1, 1, 1, 1]) == 1
  assert math_it_up.median([2, 4]) == 3
  assert math_it_up.median([192347]) == 192347
  assert math_it_up.median([5, 6, 4, 234, 5, 63, 65, 0]) == 5.5

def test_mode():
  """
  Tests for the `mode` function
  """
  assert math_it_up.mode([1, 1, 1, 1, 1]) == [1]
  assert math_it_up.mode([1, 3, 2, 5, 4]) == [1, 3, 2, 5, 4]
  assert math_it_up.mode([1, 3, 3, 3, 534577, 213]) == [3]
  assert math_it_up.mode([1, 3, 3, 3, 2, 2, 5, 5, 5, 4]) == [3, 5]