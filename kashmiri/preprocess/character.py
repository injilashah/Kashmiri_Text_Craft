
"""
kashmiri Character preprocess functions
"""

from .regexes import _SPACE_AFTER_ALL_PUNCTUATIONS_RE, _SPACE_BEFORE_ALL_PUNCTUATIONS_RE
from .regexes import _SPACE_AFTER_DIGITS_RE, _SPACE_BEFORE_DIGITS_RE
from .regexes import _SPACE_BEFORE_ENG_CHAR_RE, _SPACE_AFTER_ENG_CHAR_RE


def digits_space(text: str) -> str:
 
    text = _SPACE_BEFORE_DIGITS_RE.sub(' ', text)
    text = _SPACE_AFTER_DIGITS_RE.sub(' ', text)

    return text


def english_characters_space(text: str) -> str:
  
 
    text = _SPACE_BEFORE_ENG_CHAR_RE.sub(' ', text)
    text = _SPACE_AFTER_ENG_CHAR_RE.sub(' ', text)

    return text


def all_punctuations_space(text: str) -> str:
   
    text = _SPACE_BEFORE_ALL_PUNCTUATIONS_RE.sub(' ', text)
    text = _SPACE_AFTER_ALL_PUNCTUATIONS_RE.sub(' ', text)
    return text


def preprocess(text: str) -> str:
  
    if not isinstance(text, str):
        raise TypeError("text must be str type.")

    text = digits_space(text)
    text = all_punctuations_space(text)
    text = english_characters_space(text)
    return text