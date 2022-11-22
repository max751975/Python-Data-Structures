def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    counter = {}
    for ltr in phrase:
        if counter.get(ltr) is not None:
            counter[ltr] +=1
        else: counter[ltr] = 1
    return counter