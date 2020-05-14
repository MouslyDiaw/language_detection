#!/usr/bin/env python3
""" Module for Language detection """
import logging


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
    sanitized_text = remove_newline(text)
    try:
        language_pred = FT_MODEL_LANGUAGE.predict(sanitized_text, k=1)
        return language_pred[0][0].split("__label__")[-1], language_pred[1][0]
    except ValueError:
        logging.exception("Input doesn't contain `\\n`")
    except AttributeError:
        logging.exception(f"Input must be a str but you give {text}")
