"""Tests for `language-detection` package."""
import pytest
from language_detection.language_detection import langdetect


@pytest.fixture
def text_example():
    text = "JobTeaser est une entreprise française qui fournit des solutions de recrutement et marque employeur aux \
    entreprises pour embaucher des jeunes talents et une plateforme carrières gratuite pour les services carrières \
    des établissements d’enseignement supérieur en Europe."
    return text


def test_language_detector_format(text_example):
    """
    Test output format.
    """

    detected_lang_single = langdetect(text_example)
    detected_lang_batch = langdetect([text_example])
    assert isinstance(detected_lang_single, str)
    assert isinstance(detected_lang_batch, list)


def test_language_detector_langdetect_output(text_example):
    """
    Test output result.
    """

    detected_lang_single = langdetect(text_example)
    detected_lang_batch = langdetect([text_example])
    assert detected_lang_single == "fr"
    assert detected_lang_batch == ["fr"]
    assert len(detected_lang_batch) == 1
