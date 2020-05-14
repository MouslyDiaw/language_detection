"""Top-level package for language_detection."""
import os

import fasttext

__author__ = """Mously Diaw"""
__email__ = 'mouslydiaw@gmail.com'
__version__ = '0.1.0'


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(ROOT_DIR, "models", "lid.176.ftz")
FT_MODEL_LANGUAGE = fasttext.load_model(MODEL_PATH)

