from tasks import *

def test_token_counts():
    text = """The quick brown fox jumps over the lazy dog. The fox and the dog play together. 
              The fox chases the dog, but the dog runs quickly. The fox is fast, and the dog escapes."""
    expected = {'the': 9, 'quick': 1, 'brown': 1, 'fox': 4, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 5, 
                'and': 2, 'play': 1, 'together': 1, 'chases': 1, 'but': 1, 'runs': 1, 'quickly': 1, 
                'is': 1, 'fast': 1, 'escapes': 1}
    expected2 = {'the': 9, 'fox': 4, 'dog': 5, 'and': 2}
    expected3 = {'the': 9, 'dog': 5}
    
    obtained = token_counts(text)
    assert type(obtained) == dict, "expected return type 'dict' (k=1)"
    assert set(obtained.keys()) == set(expected.keys()), "unexpected keys in dict (k=1)"
    assert all(obtained[key] == expected[key] for key in expected), "unexpected counts (k=1)"

    obtained = token_counts(text, 2)
    assert type(obtained) == dict, "expected return type 'dict' (k=2)"
    assert set(obtained.keys()) == set(expected2.keys()), "unexpected keys in dict (k=2)"
    assert all(obtained[key] == expected2[key] for key in expected2), "unexpected counts (k=2)"

    obtained = token_counts(text, 5)
    assert type(obtained) == dict, "expected return type 'dict' (k=5)"
    assert set(obtained.keys()) == set(expected3.keys()), "unexpected keys in dict (k=5)"
    assert all(obtained[key] == expected3[key] for key in expected3), "unexpected counts (k=5)"

    obtained = token_counts(text, 10)
    assert type(obtained) == dict, "expected return type 'dict' (k=10)"
    assert obtained == {}, "expected an empty dictionary (k=10)"
##