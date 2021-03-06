==================

Language identification

==================


Installation
--------
```
git clone git@github.com:MouslyDiaw/language_detection.git
cd language-detection
pip install .
```
or,

```
pip install git+ssh://git@github.com/MouslyDiaw/language_detection.git
```

Basic usage
--------
Out of box, this module uses [fasttext](https://fasttext.cc/docs/en/language-identification.html)
pre-trained model for language detection.
It can detect the language for a sentence, example:
``` 
from language_detection import LanguageDetector
lang = LanguageDetector()
text = "This module is for language identification"
print(lang.langdetect(text))
```
``` 'fr'```

It also supports batch language detection (list of sentence), example:

```
sentences = [
    "This module is for language identification",
    "Ce module est pour l'identification de la langue",
    "Dieses Modul dient zur Sprachidentifikation",
]
print(lang.langdetect(list_doc))
```

```
['en', 'fr', 'de']
```

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
