import string


def compute_frequencies(filename: str) -> dict:
    """
    Read a text file and return a dictionary mapping each cleaned word to its frequency.
    Steps:
      1. Read the file contents.
      2. Split into words and strip punctuation.
      3. Count occurrences in a dictionary.
    """
    # Step 1: Read file
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    # Step 2: Split text and remove punctuation
    words = text.split()
    cleaned_words = []
    for word in words:
        # remove leading/trailing punctuation and make lowercase
        cleaned = word.strip(string.punctuation).lower()
        if cleaned:  # skip empty strings
            cleaned_words.append(cleaned)

    # Step 3: Build frequency dictionary
    freq_dict = {}
    for word in cleaned_words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    return freq_dict


# ---------- OPTIONAL EXTENSION ----------

def print_frequencies_sorted(freq_dict: dict, top_n: int = 20):
    """
    Print words and their frequencies sorted by descending frequency.
    Only show the top N most frequent words (default 20).
    """
    # Convert to list of tuples (freq, word)
    freq_list = [(freq, word) for word, freq in freq_dict.items()]
    # Sort by freq descending
    freq_list.sort(reverse=True)

    print("\nTop", top_n, "words by frequency:\n")
    print("WORD".ljust(15), "COUNT")
    print("-" * 25)
    for freq, word in freq_list[:top_n]:
        print(word.ljust(15), freq)


# ---------- TESTING ----------

if __name__ == "__main__":
    # Example small test file
    filename = "TextFiles/alice.txt"   # change path to any file you have

    freq = compute_frequencies(filename)

    # Print entire dictionary (for short texts)
    print("Full frequency dictionary (first 50 entries):")
    print(dict(list(freq.items())[:50]))  # show first 50 for readability

    # Print nicely sorted top frequencies
    print_frequencies_sorted(freq, top_n=20)
