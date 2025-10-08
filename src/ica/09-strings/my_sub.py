def name_subst(name: str, text: str) -> str:
    """
    Replace every occurrence of the placeholder 'ZZZ' in `text` with `name`,
    and return the new string.
    """
    return text.replace("ZZZ", name)

if __name__ == "__main__":
    sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
    print(sallie)  # My friend, Sallie, won an award.

    print(name_subst("Fred", "Jamie and ZZZ flew over the trees."))
    # Jamie and Fred flew over the trees.