import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# [A] List Comprehensions and String Manipulation: Tokenization
#     Objective: Practice list comprehensions and basic string operations: split a sentence 
#                into individual words and use list comprehensions to make the code cleaner 
#                and more readable.

# List comprehension provides a concise way to create lists by embedding a for-loop inside 
# square brackets.
# Syntax: [expression for item in iterable if condition] (condition is optional).
# Example: squares = [x**2 for x in range(10) if x % 2 == 0]

# Large language models work with "tokens," which are the basic units of text (often words or subwords). 
# Tokenization is the process of breaking down sentences into these tokens. In this exercise, you’ll 
# create a simple tokenizer to split a sentence into words and remove punctuation.



# Task 1: Given a paragraph of text, implement a simple "tokenizer" that splits the paragraph 
#   into individual words (tokens) and removes any punctuation. Implement this using a list 
#   comprehension.

# Your code here:
# -----------------------------------------------
text = "The quick brown fox jumps over the lazy dog!"

# Write a list comprehension to tokenize the text and remove punctuation
tokens = [word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~') for word in text.split()]
print(tokens)


# Expected output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(tokens)
# -----------------------------------------------




# Task 2: Create a function that takes a string and breaks it up into tokens and removes any 
#   punctuation, and then converts each token to lowercase. The function should returns unique 
#   words in alphabetical order.

# Your code here:
# -----------------------------------------------
def tokenize(string: str) -> list:
    # List comprehension to tokenize, remove punctuation, and convert to lowercase
    tokens = [word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~').lower() for word in string.split()]
    # Return unique words in alphabetical order
    return sorted(set(tokens))


# -----------------------------------------------



# [B] Dictionary Comprehensions: Frequency Count of Tokens
#     Objective: Practice dictionary comprehensions for token frequency counts.

# Dictionary comprehension is a concise way to create dictionaries using a for-loop inside curly braces.
# Syntax: {key: value for item in iterable if condition} (condition is optional).
# Example: char_count = {char: ord(char) for char in "hello" if char != 'e'}

# Once tokens are extracted, a common task in NLP is to count how often each word appears. 
# This is called calculating the frequency of tokens, and it’s useful because words that appear 
# frequently might have different importance compared to rare words. In this exercise, you’ll 
# create a dictionary where each word is a key and its frequency (count) is the value.



# Task 3: Using the tokens list from the previous exercise, create a dictionary comprehension 
#   that counts the frequency of each word.

# Using the list of tokens from Exercise 1, count the frequency of each word within one 
# dictionary comprehension

# Your code here:
# -----------------------------------------------
# Task 3: Frequency count of tokens, only keeping words that appear more than once
word_frequencies = {word: tokens.count(word) for word in tokens}
word_frequencies = {word: count for word, count in word_frequencies.items() if count > 1}
print(word_frequencies)  # Output: {'the': 2} 
#

# Modify the comprehension to include only words that appear more than once.
# -----------------------------------------------



# Task 4: Define a function that takes a string and an integer k, and returns a dictionary with
#   the token frequencies of only those tokens that occur more than k times in the string.

# Your code here:
# -----------------------------------------------
def token_counts(string: str, k: int = 1) -> dict:
    # First, use the tokenize function to extract tokens from the string
    tokens = tokenize(string)
    
    # Use numpy to count occurrences of each token
    unique, counts = np.unique(tokens, return_counts=True)
    
    # Create a dictionary with word frequencies
    word_frequencies = {str(word): count for word, count in zip(unique, counts)}
    
    # Filter out words that appear less than or equal to `k` times
    filtered_frequencies = {word: count for word, count in word_frequencies.items() if count > k}
    
    return filtered_frequencies
####

##


# test:
text_hist = {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
all(text_hist[key] == value for key, value in token_counts(text).items())
# -----------------------------------------------




# [C] Sets & Dictionary comprehension: Mapping unique tokens to numbers and vice versa
#   Objective: Practice dictionary comprehensions and create mappings from tokens to unique 
#              numerical IDs and back.

# Once tokens are created, they often need to be converted to numerical representations 
# for use in models. Two essential mappings are:
#
# Token to ID: Maps each token to a unique number.
# ID to Token: Maps each unique number back to its corresponding token.
#
# These mappings are necessary for transforming text data into numerical data that models can 
# process. In this exercise, you’ll use dictionary comprehensions to create these mappings.



# Task 5: Given a list of tokens from Exercise 1, construct two dictionaries:
#   `token_to_id`: a dictionary that maps each token to a unique integer ID.
#   `id_to_token`: a dictionary that maps each unique integer ID back to the original token.

# Your code here:
# -----------------------------------------------
token_to_id = {token: idx for idx, token in enumerate(tokens)}

# Expected output: {'dog': 0, 'quick': 1, 'fox': 2, 'the': 3, 'over': 4, 'lazy': 5, 'brown': 6, 'jumps': 7}
print(token_to_id)
# -----------------------------------------------



# Task 6: Define a dictionary that reverses the maping in `token2int`
#
# Your code here:
# -----------------------------------------------
id_to_token = {idx: token for token, idx in token_to_id.items()}

# tests: 
# test 1
assert id_to_token[token_to_id['dog']] == 'dog'
# test 2
assert token_to_id[id_to_token[4]] == 4
# test 3
assert all(id_to_token[token_to_id[key]]==key for key in token_to_id) and all(token_to_id[id_to_token[k]]==k for k in range(len(token_to_id)))
# -----------------------------------------------



# Task 7: Define a function that will take a list of strings ('documents'), determines all the
#   unique tokens across all documents, and returns two dictionaries: one (token2int) that maps 
#   each unique token to a unique integer, and a dictionary (int2token) that maps each integer
#   to the corresponding token in the first dictionary

# Your code here:
# -----------------------------------------------
# Define Vocabulary Mapping Function
def make_vocabulary_map(documents: list) -> tuple:
    # Flatten all tokenized documents into one list of unique tokens
    tokens = sorted(set(word for doc in documents for word in tokenize(doc)))
    
    # Create token-to-ID mapping
    token_to_id = {token: idx for idx, token in enumerate(tokens)}
    
    # Create ID-to-token mapping
    id_to_token = {idx: token for token, idx in token_to_id.items()}
    
    return token_to_id, id_to_token


# Test
t2i, i2t = make_vocabulary_map([text])
all(i2t[t2i[tok]] == tok for tok in t2i) # should be True
# -----------------------------------------------



# Task 8: Define a function that will take in a list of strings ('documents') and a vocabulary
#   dictionary token_to_id, that tokenizes each string in the list and returns a list with
#   each string converted into a list of token ID's. For example:
#   ['Good day!', 'What a day'] -> [[0, 1], [2, 3, 1]]
#   The function should return three values: the list of encoded sentences, the token_to_id,
#   and the id_to_token dictionaries.

# Your code here:
# -----------------------------------------------
def tokenize(string: str) -> list:
    # Tokenize the string by removing punctuation and converting to lowercase
    tokens = [word.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~').lower() for word in string.split()]
    return tokens

tokenize("The quick brown fox jumps over the lazy dog!")

def tokenize_and_encode(documents: list) -> tuple:
    # Generate token-to-ID and ID-to-token mappings
    token_to_id, id_to_token = make_vocabulary_map(documents)
    
    # Encode each document as a list of token IDs
    encoded_sentences = [
        [token_to_id[token] for token in tokenize(doc)] for doc in documents
    ]
    
    # Return the encoded sentences and mappings
    return encoded_sentences, token_to_id, id_to_token

# Test:
enc, t2i, i2t = tokenize_and_encode([text, 'What a luck we had today!'])
" | ".join([" ".join(i2t[i] for i in e) for e in enc]) == 'the quick brown fox jumps over the lazy dog | what a luck we had today'
# -----------------------------------------------



# In the following set of exercises you're going to implement an RNN from scratch. You'll also
# fit it to an existing time series.


# [D] Using a lambda expression to define functions: One line definition of a function
# Objective: practicing to work with lambda functions

# You'll implement a RNN with the logistic (sigmoid) activation function for
# the nodes. We need to implement this function first.



# Task 9: use a lambda function to implement the logistic function using the np.exp
#   function to work elementwise with numpy arrays

# Your code here:
# -----------------------------------------------
sigmoid = lambda x: 1 / (1 + np.exp(-x))

# Test:
np.all(sigmoid(np.log([1, 1/3, 1/7])) == np.array([1/2, 1/4, 1/8]))
# -----------------------------------------------



