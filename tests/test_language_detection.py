"""Tests for `language-detection` package."""
import pytest
from language_detection.langdetector import LanguageDetector


@pytest.fixture(scope="module")
def text_example():
    text = "Ce module est conçu pour détecter la langue d'un text ou une liste de text."
    return text


def test_language_detector_format(text_example):
    """
    Test output format.
    """
    lang = LanguageDetector()
    detected_lang_single = lang.langdetect(text_example)
    detected_lang_batch = lang.langdetect([text_example])
    assert isinstance(detected_lang_single, str)
    assert isinstance(detected_lang_batch, list)


def test_language_detector_langdetect_output(text_example):
    """
    Test output result.
    """
    lang = LanguageDetector()
    detected_lang_single = lang.langdetect(text_example)
    detected_lang_batch = lang.langdetect([text_example])
    assert detected_lang_single == "fr"
    assert detected_lang_batch == ["fr"]
    assert len(detected_lang_batch) == 1


def test_language_detector_exception():
    """ test that exception is raised for invalid input """
    lang = LanguageDetector()
    with pytest.raises(Exception) as e:
        assert lang.langdetect(3)
        assert "Invalid type of argument" in str(e)
