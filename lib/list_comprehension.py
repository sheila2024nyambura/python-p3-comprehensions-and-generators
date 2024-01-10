#!/usr/bin/env python3


def return_evens(sequence):
    # Using list comprehension to filter even numbers
    even_numbers = [num for num in sequence if num % 2 == 0]
    return even_numbers

# Example usage
result_evens = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result_evens)
# Output: [0, 8]

def make_exclamation(sentences):
    # Using list comprehension to add exclamation marks
    exclamated_sentences = [sentence + '!' for sentence in sentences]
    return exclamated_sentences

# Example usage
result_exclamation = make_exclamation(["I like computers", "I require coffee", "Live long and prosper"])
print(result_exclamation)
# Output: ['I like computers!', "I require coffee!", "Live long and prosper!",]
    