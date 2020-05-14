#!/usr/bin/env python3
""" Module for Language detection """
import logging
from typing import List


from language_detection import FT_MODEL_LANGUAGE
from language_detection.helpers.feature_engineering import remove_newline


def langdetect(text: str) -> str:
    """ language detection with fasttext (pre-trained model)

    Args:
        text (str): sentence to detect language

    Returns:
        str: code language ex: 'fr', 'en', 'de', ...

    Notes:
        - Fasttext language identification is sensitive to punctuation.
        - Input doesn't contains any punctuation (aka \\n)
        - ValueError: we raise an error if it occurs any \n in text
    """
    if isinstance(text, str):
        sanitized_text = remove_newline(text)
        language_pred = FT_MODEL_LANGUAGE.predict(sanitized_text, k=1)[0]
        return language_pred[0][0].split("__label__")[1]
    elif isinstance(text, str):
        sanitized_text = list(map(remove_newline, text))
        language_pred = FT_MODEL_LANGUAGE.predict(sanitized_text, k=1)[0]
        return [pred[0].split("__label__")[1] for pred in language_pred]
    else:
        raise ValueError("Invalid type of argument. It sould be either a str or a list of str.")