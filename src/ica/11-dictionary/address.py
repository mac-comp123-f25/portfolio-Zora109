betsy_info = {
    'Name': 'Betsy Foobar',
    'Phone': 'x8012',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'bfoobar@macalester.edu'
}
tom_info = {
    'Name': 'Tom Riddle',
    'Phone': 'x8512',
    'Street': '1600 Grand Avenue',
    'City': 'Saint Paul',
    'State': 'MN',
    'Email': 'triddle@macalester.edu'
}
address_book = [
    betsy_info,
    tom_info,
    {
        'Name': 'Susan Fox',
        'Phone': 'x6553',
        'Street': '1600 Grand Avenue',
        'City': 'Saint Paul',
        'State': 'MN',
        'Email': 'fox@macalester.edu'
    }
]

print("Original address_book (3 entries):")
print(address_book)

address_book.append({
    'Name': 'Harry Potter',
    'Phone': 'x7777',
    'Street': '200 Main Street',
    'City': 'Minneapolis',
    'State': 'MN',
    'Email': 'hpotter@macalester.edu'
})

address_book.append({
    'Name': 'Hermione Granger',
    'Phone': 'x5555',
    'Street': '10 Lake Avenue',
    'City': 'Duluth',
    'State': 'MN',
    'Email': 'hgranger@macalester.edu'
})

print("\nUpdated address_book (5 entries):")
print(address_book)

def filter_by_city(city: str, book: list[dict]) -> list[dict]:
    """Return a new list containing only contacts whose City equals `city`."""
    # Using a list comprehension; .get('City') avoids KeyError if key is missing
    return [entry for entry in book if entry.get('City') == city]