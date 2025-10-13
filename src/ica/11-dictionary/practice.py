income = {}
years = {
    "Susan": 1968,
    "Amelia": 1999,
    "Freddy": 2001
}
years2 = years.copy()
print("Susan's birth year:", years["Susan"])
years["Henry"] = 2004
del years2["Susan"]
print("years:", years)
print("years2 (after deleting Susan):", years2)
print("income (should still be empty):", income)