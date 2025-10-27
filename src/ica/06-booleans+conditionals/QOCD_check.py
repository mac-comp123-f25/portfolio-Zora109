def has_QOCD(input_string):
  """
  Checks if the input string contains at least one of the uppercase
  letters 'Q', 'O', 'C', or 'D'.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains at least one of the specified
    letters, otherwise False.
  """
  return 'Q' in input_string or 'O' in input_string or 'C' in input_string or 'D' in input_string

# Unit tests
if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")