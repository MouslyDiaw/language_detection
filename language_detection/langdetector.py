#!/usr/bin/env python3
""" Module for Language detection """
from os import path
import fasttext
from typing import Union, List

from language_detection.helpers.feature_engineering import remove_newline


ROOT_PATH = path.dirname(path.abspath(__file__))

MODEL_PATH = path.join(ROOT_PATH, "models", "lid.176.ftz")


class LanguageDetector:
    """ Module for language identification """

    def __init__(self):
        """ Module for language identification """
        self.model = fasttext.load_model(MODEL_PATH)

    def langdetect(self, text) -> Union[List[str], str]:
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
            language_pred = self.model.predict(sanitized_text, k=1)[0]
            return language_pred[0].split("__label__")[1]
        elif isinstance(text, list):
            sanitized_text = list(map(remove_newline, text))
            language_pred = self.model.predict(sanitized_text, k=1)[0]
            return [pred[0].split("__label__")[1] for pred in language_pred]
        else:
            raise ValueError("Invalid type of argument. It should be either a str or a list of str.")
