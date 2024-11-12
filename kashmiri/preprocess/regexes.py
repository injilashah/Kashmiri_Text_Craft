# coding: utf8
"""List of Regex for preprocess"""

import string

import regex as re
import kashmiri_characters
from kashmiri_characters import KASHMIRI_ALL_CHARACTERS, KASHMIRI_PUNCTUATIONS
# Add spaces before|after numeric number and KASHMIRI words

_EXCEPT_HAMZA = list(filter(lambda c: c != '\u0621', KASHMIRI_ALL_CHARACTERS))
_SPACE_BEFORE_DIGITS_RE = re.compile(r"(?<=[" + "".join(KASHMIRI_ALL_CHARACTERS) + "])(?=[0-9])", flags=re.U | re.M | re.I)
_SPACE_AFTER_DIGITS_RE = re.compile(r"(?<=[0-9])(?=[" + "".join(_EXCEPT_HAMZA) + "])", flags=re.U | re.M | re.I)

# Add spaces before|after english characters and KASHMIRI words

_SPACE_BEFORE_ENG_CHAR_RE = re.compile(r"(?<=[" + "".join(KASHMIRI_ALL_CHARACTERS) + "])(?=[a-zA-Z])",
                                       flags=re.U | re.M | re.I)
_SPACE_AFTER_ENG_CHAR_RE = re.compile(r"(?<=[a-zA-Z])(?=[" + "".join(KASHMIRI_ALL_CHARACTERS) + "])",
                                      flags=re.U | re.M | re.I)

# add space before and after all PUNCTUATIONS
_ALL_PUNCTUATIONS: str = "".join(KASHMIRI_PUNCTUATIONS) + "".join(string.punctuation)
_SPACE_BEFORE_ALL_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(KASHMIRI_ALL_CHARACTERS) + "])(?=[" + "".join(_ALL_PUNCTUATIONS) + "])",
    flags=re.U | re.M | re.I)
_SPACE_AFTER_ALL_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(_ALL_PUNCTUATIONS) + "])(?=[^" + "".join(_ALL_PUNCTUATIONS) + "0-9 \n])",
    flags=re.U | re.M | re.I)