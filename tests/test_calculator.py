import pytest
import numpy as np
from src.calculator import calculate_power

class TestCalculatePower(object):
  def test_calculate_power(self):
    assert isinstance(calculate_power(2, 5), (np.float64, np.int64))
    assert calculate_power(2, 5) == pytest.approx(32)
