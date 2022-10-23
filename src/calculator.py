import numpy as np

def calculate_power(base, power) -> float:
  assert isinstance(base, (int, float))
  assert isinstance(power, int)
  return(np.power(base, power))

