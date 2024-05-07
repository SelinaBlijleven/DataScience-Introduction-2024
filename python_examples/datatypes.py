"""
A little cheatsheet on data types in Python
"""

"""" Simple types """
whole_number = 5            # Integer
dec_number = 2.5            # Float
binary = True               # Boolean
text = "Hello"              # String

# With type hints
a: int = 5                  # Integer
b: float = 2.5              # Float
c: bool = True              # Boolean
d: str = "Hello"            # String

""" Lists """
lst = []                    # List (empty)
lst2 = [1, 2, 3, 4, 5]      # List (with integers)
lst3 = ["a", 1, 4, "b"]     # Lists can mix datatypes

# We can put lists in lists
lst4 = [["Pietje", 10], ["Petra", 7.5], ["Paul", 8]]

# Lists with type hints
lst5: list = []
lst6: list[int] = [1, 2, 3, 4, 5]
lst7: list[list[str, int]] = [["Pietje", 10], ["Petra", 7.5], ["Paul", 8]]

""" Dictionaries """
# Dictionaries combine a list of so-called keys and values, making them great for mapping, translation and more.
alphabet = {
    'a':  1,
    'b':  2,
    'c':  3
}

# Empty dictionary
empty_dict = {}

# They are very useful for storing frequencies too, let's try!
# Empty dictionary with a type hint
freq: dict = {}
text_example = "I might be a longer piece of text, containing several words that we are now able to count. " \
               "We can then see how many times each word occurs in the text! Note that there are many libraries " \
               "that can do this more efficiently, however."

# Split all the words in the string
for word in text_example.split():
    if word in freq.keys():
        # Not the first time, +1
        freq[word] += 1
    else:
        # First time seeing this
        freq[word] = 1

# We can also print most datatypes directly in Python
print(f"Unsorted dictionary:\n {freq}")

# Sort the dictionary by value in descending order (remove reverse=True for ascending)
sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

# Print the top 5 most common words.
print(f"Sorted dictionary:\n {sorted_dict}")

""" 
Also check out: 
- Sets in python, which can be used to compare data between two sets and apply logical operations.
"""
