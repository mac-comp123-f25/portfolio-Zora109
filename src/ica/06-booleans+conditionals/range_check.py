def range_limit(num):
  """
  Limits a number to be within the range of 1 to 10.

  Args:
    num: The input number.

  Returns:
    The number, but limited to the range [1, 10].
  """
  if num < 1:
    return 1
  elif num > 10:
    return 10
  else:
    return num

# Unit tests
if __name__ == "__main__":
  assert range_limit(5) == 5
  assert range_limit(0) == 1
  assert range_limit(11) == 10
  assert range_limit(1) == 1
  assert range_limit(10) == 10
  print("All tests passed!")