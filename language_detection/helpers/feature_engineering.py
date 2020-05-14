""" Pre-processing text """

import re


def remove_newline(text: str) -> str:
    """ Delete newlines

    Args:
        text (str): text to sanitize

    Returns:
        str: text without non-alphanumeric character, html tags, email, etc.

    """
    return re.sub(r"\n+", " ", text)
