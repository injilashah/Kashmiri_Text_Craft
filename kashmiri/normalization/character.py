

from typing import Dict, Lists
import logging

from .regexes import _DIACRITICS_RE
from .regexes import _SPACE_AFTER_PUNCTUATIONS_RE, _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE

logger = logging.getLogger(__name__)

# Contains wrong Urdu characters mapping to correct characters



_CORRECT_Kashmiri_CHARACTERS_MAPPING: Dict[str, List[str]] = {  'آ': ['ﺁ', 'ﺂ'],
                                                          'أ': ['ﺃ'],
                                                          '[ٲ]': 'ٲ,
                                                          'ا':['ﺍ',  'ﺎ' ],
                                                          'ب': ['ﺏ', 'ﺐ', 'ﺑ', 'ﺒ'],
                                                          'پ': ['ﭖ', 'ﭘ', 'ﭙ' ],
                                                          'ت': ['ﺕ', 'ﺖ', 'ﺗ', 'ﺘ'],
                                                          'ٹ': ['ﭦ', 'ﭧ', 'ﭨ', 'ﭩ'],
                                                          'ث': ['ﺛ', 'ﺜ', 'ﺚ'],
                                                          'ج': ['ﺝ', 'ﺞ', 'ﺟ', 'ﺠ'],
                                                          'ح': ['ﺡ', 'ﺣ', 'ﺤ', 'ﺢ'],
                                                          'خ': ['ﺧ', 'ﺨ', 'ﺦ'],
                                                          'د': ['ﺩ', 'ﺪ'],
                                                          'ذ': ['ﺬ', 'ﺫ'],
                                                          'ر': ['ﺭ', 'ﺮ'],
                                                          'ز': ['ﺯ', 'ﺰ', ],
                                                          'س': ['ﺱ', 'ﺲ', 'ﺳ', 'ﺴ', ],
                                                          'ش': ['ﺵ', 'ﺶ', 'ﺷ', 'ﺸ'],
                                                          'ص': ['ﺹ', 'ﺺ', 'ﺻ', 'ﺼ', ],
                                                          'ض': ['ﺽ', 'ﺾ', 'ﺿ', 'ﻀ'],
                                                          'ط': ['ﻃ', 'ﻄ'],
                                                          'ظ': ['ﻅ', 'ﻇ', 'ﻈ'],
                                                          'ع': ['ﻉ', 'ﻊ', 'ﻋ', 'ﻌ', ],
                                                          'غ': ['ﻍ', 'ﻏ', 'ﻐ', ],
                                                          'ف': ['ﻑ', 'ﻒ', 'ﻓ', 'ﻔ', ],
                                                          'ق': ['ﻕ', 'ﻖ', 'ﻗ', 'ﻘ', ],
                                                          'ل': ['ﻝ', 'ﻞ', 'ﻟ', 'ﻠ', ],
                                                          'م': ['ﻡ', 'ﻢ' , 'ﻣ', 'ﻤ', ],
                                                          'ن': ['ﻥ', 'ﻦ', 'ﻧ', 'ﻨ', ],
                                                          'چ': ['ﭺ', 'ﭻ', 'ﭼ', 'ﭽ'],
                                                          'ڈ': ['ﮈ', 'ﮉ'],
                                                          'ڑ': ['ﮍ', 'ﮌ'],
                                                          'ژ': ['ﮋ', ],
                                                          'ک': ['ﮎ', 'ﮏ', 'ﮐ', 'ﮑ', 'ﻛ', 'ك'],
                                                          'گ': ['ﮒ', 'ﮓ', 'ﮔ', 'ﮕ'],
                                                          'ں': ['ﮞ', 'ﮟ'],
                                                          'و': ['ﻮ', 'ﻭ', 'ﻮ', ],
                                                          
                                                          'ھ': ['ﮪ', 'ﮬ', 'ﮭ', 'ﻬ', 'ﻫ', 'ﮫ'],
                                                          'ہ': ['ﻩ', 'ﮦ', 'ﻪ', 'ﮧ', 'ﮩ', 'ﮨ', 'ه' ],
                                                          
                                                          
                                                          'ء': ['ﺀ'],
                                                          'ی ': ['ﯼ'  , 'ى', 'ﯽ', 'ﻰ', 'ﻱ', 'ﻲ', 'ﯾ', 'ﯿ', 'ي'],
                                                          'ے': ['ﮮ', 'ﮯ', 'ﻳ', 'ﻴ', ],
                                                          
                                                          '۰': ['٠'],
                                                          '۱': ['١'],
                                                          '۲': ['٢'],
                                                          '۳': ['٣'],
                                                          '۴': ['٤'],
                                                          '۵': ['٥'],
                                                          '۶': ['٦'],
                                                          '۷': ['٧'],
                                                          '۸': ['٨'],
                                                          '۹': ['٩'],
                                                          '۔': [],
                                                          '؟': [],
                                                          '٫': [],
                                                          '،': [],
                                                          
                                                          '': ['ـ']
                                                          'ۄ': ['ۄ'], 
                                                          'ٮ۪': [ 'ؠـ', 'ٮ۪'], 
                                                          'ؤ': ['ؤ'],
                                                          'ؠ': ['ؠ'],
                                                          'ۅ': ['ۅ'],
                                                          'ۆ': ['ۆ'],
                                                          'ډ': ['ډ'],
                                                          'ۍ': ['ۍ'],
                                                          'إ': ['إ'],
                                                          'ٳ': ['ٳ'],
                                                          'ۈ': ['ۈ']
                                                          'ۇ': ['ۇ']
                                                          'ۉ': ['ۉ']
                                                          'ێ': ['ێ']
                                                          'ڒ': ['ڒ'], 
                                                         

}


                                                          

_TRANSLATOR = {}
for key, value in _CORRECT_KASHMIRI_CHARACTERS_MAPPING.items():
    _TRANSLATOR.update(dict.fromkeys(map(ord, value), key))


def normalize_characters(text: str) -> str:
  
    return text.translate(_TRANSLATOR)


COMBINE_KASHMIRI_CHARACTERS: Dict[str, str] = {"آ": "آ",
                                           "أ": "أ",
                                           
                                           }


# Issue to be resolved: Words like کیجئے and کیجیے appear in the same context but they have different unicodes.
# We cannot merge them neither can we have them separately. Because if we decompose ئ,
# we get unicode that are not available in our unicode list.

def normalize_combine_characters(text: str) -> str:
 
    for _key, _value in COMBINE_KASHMIRI_CHARACTERS.items():
        text = text.replace(_key, _value)
    return text


def punctuations_space(text: str) -> str:
    
    text = _SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
    text = _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE.sub(r'\1', text)
    return text


'''def remove_diacritics(text: str) -> str:
    
    return _DIACRITICS_RE.sub('', text)'''


ENG_KASHMIRI_DIGITS_MAP: Dict = {
    '0': ['۰'],
    '1': ['۱'],
    '2': ['۲'],
    '3': ['۳'],
    '4': ['۴'],
    '5': ['۵'],
    '6': ['۶'],
    '7': ['۷'],
    '8': ['۸'],
    '9': ['۹']
}

_ENG_DIGITS_TRANSLATOR = {}
for key, value in ENG_KASHMIRI_DIGITS_MAP.items():
    _ENG_DIGITS_TRANSLATOR.update(dict.fromkeys(map(ord, value), key))

KASHMIRI_ENG_DIGITS_MAP: Dict = {
    '۰': ['0'],
    '۱': ['1'],
    '۲': ['2'],
    '۳': ['3'],
    '۴': ['4'],
    '۵': ['5'],
    '۶': ['6'],
    '۷': ['7'],
    '۸': ['8'],
    '۹': ['9']
}

_KASHMIRI_DIGITS_TRANSLATOR = {}
for key, value in KASHMIRI_ENG_DIGITS_MAP.items():
    _KASHMIRI_DIGITS_TRANSLATOR.update(dict.fromkeys(map(ord, value), key))


def replace_digits(text: str, with_english: bool = True) -> str:
    """
    Replace kasmiri digits with English digits and vice versa

    Args:
        text : kashmiri text string
        with_english (bool): Boolean to convert digits from one language to other
    Returns:
        Text string with replaced digits
    """
    if with_english:
        return text.translate(_ENG_DIGITS_TRANSLATOR)
    return text.translate(_KASHMIRI_DIGITS_TRANSLATOR)


def normalize(text: str) -> str:
   
    if not isinstance(text, str):
        raise TypeError("Text must be str type.")

    logger.info("Normalizing the text.")

    text = remove_diacritics(text)
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    return text
