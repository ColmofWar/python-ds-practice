def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:
    
        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:
    
        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:
    
        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    """
    ord() does not follow expected return of "a"=1,"b"=2,ect
    ord("a") = 97, ord("b") = 98, ord("A") = 65, ord ("B") = 66
    ord() still returns odd on a and even on b and ect...
    ord() will work to return odd or even
    """
    total = 0
    for letter in word:
        total += ord(letter)
    if total % 2 == 0:
        return False
    return True