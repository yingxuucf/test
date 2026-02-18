"""
text_utils.py - A collection of text processing utilities.
"""


def word_count(text):
    """Return the number of words in a string."""
    if not text or not text.strip():
        return 0
    return len(text.split())


def reverse_string(s):
    """Return the reverse of a string."""
    return s[::-1]


def capitalize_words(text):
    """Capitalize the first letter of each word in a string.

    Args:
        text: The input string.

    Returns:
        A new string with each word's first letter capitalized.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("the quick brown fox")
        'The Quick Brown Fox'
    """
    return " ".join(word.capitalize() for word in text.split())


def remove_duplicates(items):
    """Remove duplicate items from a list while preserving insertion order.

    Args:
        items: A list of items.

    Returns:
        A new list with duplicates removed, preserving original order.

    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 1])
        [1, 2, 3]
        >>> remove_duplicates(["a", "b", "a", "c"])
        ['a', 'b', 'c']
    """
    return list(dict.fromkeys(items))


def is_palindrome(s):
    """Check whether a string is a palindrome (ignoring case and spaces).

    Args:
        s: The input string.

    Returns:
        True if the string is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False
    """
    normalized = "".join(s.lower().split())
    return normalized == normalized[::-1]
