def has_q(input_string):
  """
  Checks if the input string contains the lowercase letter 'q'.

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains 'q', otherwise False.
  """
  return 'q' in input_string

# Unit tests
if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")