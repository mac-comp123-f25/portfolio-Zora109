import string

def clean(s: str) -> str:
    """
    Return a copy of s with all punctuation and whitespace removed, using recursion.
    Examples:
      clean('The big elephant') -> 'Thebigelephant'
      clean('--A man, a plan, a canal: Panama!') -> 'AmanaplanacanalPanama'
      clean('One') -> 'One'
      clean('') -> ''
    """
    if len(s) == 0:
        return ""
    first_chr = s[0]
    rest_str = clean(s[1:])
    if first_chr in string.punctuation + string.whitespace:
        return rest_str
    else:
        return first_chr + rest_str


if __name__ == "__main__":
    print(clean("The big elephant"))
    print(clean("--A man, a plan, a canal: Panama!"))
    print(clean("One"))
    print(clean(""))

