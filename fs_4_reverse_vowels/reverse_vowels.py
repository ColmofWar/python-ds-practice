VOWELS = set("aeiou")
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s_vowel_list = []
    string = list(s)
    for letter in string:
        if letter in VOWELS:
            s_vowel_list.append(letter)
    s_vowel_list.reverse()
    svl_index = 0
    for i in range(len(string)):
        if string[i] in VOWELS:
            string[i] = s_vowel_list[svl_index]
            svl_index += 1
    return "".join(string)