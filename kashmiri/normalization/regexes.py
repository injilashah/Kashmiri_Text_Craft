import regex as re
import kashmiri_characters
from kashmiri_characters import KASHMIRI_PUNCTUATIONS, KASHMIRI_DIACRITICS

# Add spaces after ., if there is number then not Ex (9.00)
_SPACE_AFTER_PUNCTUATIONS_RE = re.compile(
    r"(?<=[" + "".join(KASHMIRI_PUNCTUATIONS) + "])(?=[^" + "".join(KASHMIRI_PUNCTUATIONS) + "0-9 \n])",
    flags=re.U | re.M | re.I)
_REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE = re.compile(r'\s+([' + "".join(KASHMIRI_PUNCTUATIONS) + '])',
                                                  flags=re.U | re.M | re.I)

_DIACRITICS_RE = re.compile(f'[{"".join(KASHMIRI_DIACRITICS)}]', flags=re.U | re.M | re.I)
