
import unicodedata
from typing import Dict, List
import logging

#from normalization.regexes import _DIACRITICS_RE
from normalization.regexes import _SPACE_AFTER_PUNCTUATIONS_RE, _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE

logger = logging.getLogger(__name__)

# Contains wrong kashmiri characters mapping to correct characters
_CORRECT_KASHMIRI_CHARACTERS_MAPPING: Dict[str, List[str]] = {  'آ': ['ﺁ', 'ﺂ'],
                                                          'أ': ['ﺃ'],
                                                          'ٲ':  ['ٲ'],
                                                          
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
                                                          'ۃ': ['ة'],
                                                          
                                                          'ء': ['ﺀ'],
                                                          'ی': ['ﯼ'  , 'ى', 'ﯽ', 'ﻰ', 'ﻱ', 'ﻲ', 'ﯾ', 'ﯿ', 'ي'],
                                                          'ئ': ['ﺋ', 'ﺌ', ],
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
                                                          
                                                          '': ['ـ'],
                                                          'ۄ': ['ۄ'], 
                                                           
                                                          'ؤ': ['ؤ'],
                                                          'ؠ': ['ؠ'],
                                                          'ۅ': ['ۅ'],
                                                          'ۆ': ['ۆ'],
                                                          'ډ': ['ډ'],
                                                          'ۍ': ['ۍ'],
                                                          'إ': ['إ'],
                                                          'ٳ': ['ٳ'],
                                                          'ۈ': ['ۈ'],
                                                          'ۇ': ['ۇ'],
                                                          'ۉ': ['ۉ'],
                                                          'ێ': ['ێ'],
                                                          'ڒ': ['ڒ'], 
                                                         

}


                                                          

_TRANSLATOR = {}
for key, value in _CORRECT_KASHMIRI_CHARACTERS_MAPPING.items():
    _TRANSLATOR.update(dict.fromkeys(map(ord, value), key))


def normalize_characters(text: str) -> str:
  
    return text.translate(_TRANSLATOR)


COMBINE_KASHMIRI_CHARACTERS: Dict[str, str] = {'ٮ۪': [ 'ؠـ', 'ٮ۪'],

"ٮ۪":"ٮ۪", 
"اۆ":"اۆ",    
"اےٚ":"اےٚ", 
"چھِ":"چھِ", 
"نہٕ":"نہٕ", 
"چھَ":"چھَ", 
"ـؠ" :"ـؠ", 
                                               
"چُھ": "چُھ",
"اَ": "اَ",
"اِ": "اِ",
"اُ": "اُ",
"بَ": "بَ",
"بِ": "بِ",
"بُ": "بُ",
"بآ": "بآ",
"بٔ": "بٔ",
"بٕ": "بٕ",
"پَ": "پَ",
"پِ": "پِ",
"پُ": "پُ",
"پآ": "پآ",
"پٔ": "پٔ",
"پٕ": "پٕ",
"تَ": "تَ",
"تِ": "تِ",
"تُ": "تُ",
"تآ": "تآ",
"تٔ": "تٔ",
"تٕ": "تٕ",
"ٹَ": "ٹَ",
"ٹِ": "ٹِ",
"ٹُ": "ٹُ",
"ٹآ": "ٹآ",
"ٹٔ": "ٹٔ",
"ٹٕ": "ٹٕ",
"ثَ": "ثَ",
"ثِ": "ثِ",
"ثُ": "ثُ",
"ثآ": "ثآ",
"ثٔ": "ثٔ",
"ثٕ": "ثٕ",
"جَ": "جَ",
"جِ": "جِ",
"جُ": "جُ",
"جآ": "جآ",
"جٔ": "جٔ",
"جٕ": "جٕ",
"چَ": "چَ",
"چِ": "چِ",
"چُ": "چُ",
"چآ": "چآ",
"چٔ": "چٔ",
"چٕ": "چٕ",
"حَ": "حَ",
"حِ": "حِ",
"حُ": "حُ",
"حآ": "حآ",
"حٔ": "حٔ",
"حٕ": "حٕ",
"خَ": "خَ",
"خِ": "خِ",
"خُ": "خُ",
"خآ": "خآ",
"خٔ": "خٔ",
"خٕ": "خٕ",
"دَ": "دَ",
"دِ": "دِ",
"دُ": "دُ",
"دآ": "دآ",
"دٔ": "دٔ",
"دٕ": "دٕ",
"ڈَ": "ڈَ",
"ڈِ": "ڈِ",
"ڈُ": "ڈُ",
"ڈآ": "ڈآ",
"ڈٔ": "ڈٔ",
"ڈٕ": "ڈٕ",
"ذَ": "ذَ",
"ذِ": "ذِ",
"ذُ": "ذُ",
"ذآ": "ذآ",
"ذٔ": "ذٔ",
"ذٕ": "ذٕ",
"رَ": "رَ",
"رِ": "رِ",
"رُ": "رُ",
"رآ": "رآ",
"رٔ": "رٔ",
"رٕ": "رٕ",
"رٛ": "رٛ",
"ڑَ": "ڑَ",
"ڑِ": "ڑِ",
"ڑُ": "ڑُ",
"ڑآ": "ڑآ",
"ڑٔ": "ڑٔ",
"ڑٕ": "ڑٕ",
"زَ": "زَ",
"زِ": "زِ",
"زُ": "زُ",
"زآ": "زآ",
"زٔ": "زٔ",
"زٕ": "زٕ",
"ژَ": "ژَ",
"ژِ": "ژِ",
"ژُ": "ژُ",
"ژآ": "ژآ",
"ژٔ": "ژٔ",
"ژٕ": "ژٕ",
"سَ": "سَ",
"سِ": "سِ",
"سُ": "سُ",
"سآ": "سآ",
"سٔ": "سٔ",
"سٕ": "سٕ",
"شَ": "شَ",
"شِ": "شِ",
"شُ": "شُ",
"شآ": "شآ",
"شٔ": "شٔ",
"شٕ": "شٕ",
"شٛ": "شٛ",
"صَ": "صَ",
"صِ": "صِ",
"صُ": "صُ",
"صآ": "صآ",
"صٔ": "صٔ",
"صٕ": "صٕ",
"ضَ": "ضَ",
"ضِ": "ضِ",
"ضُ": "ضُ",
"ضآ": "ضآ",
"ضٔ": "ضٔ",
"ضٕ": "ضٕ",
"ۆ": "ۆ",
"طَ": "طَ",
"طِ": "طِ",
"طُ": "طُ",
"طآ": "طآ",
"طٔ": "طٔ",
"طٕ": "طٕ",
"ظَ": "ظَ",
"ظِ": "ظِ",
"ظُ": "ظُ",
"ظآ": "ظآ",
"ظٔ": "ظٔ",
"ظٕ": "ظٕ",
"عَ": "عَ",
"عِ": "عِ",
"عُ": "عُ",
"عآ": "عآ",
"عٔ": "عٔ",
"عٕ": "عٕ",
"غَ": "غَ",
"غِ": "غِ",
"غُ": "غُ",
"غآ": "غآ",
"غٔ": "غٔ",
"غٕ": "غٕ",
"فَ": "فَ",
"فِ": "فِ",
"فُ": "فُ",
"فآ": "فآ",
"فٔ": "فٔ",
"فٕ": "فٕ",
"قَ": "قَ",
"قِ": "قِ",
"قُ": "قُ",
"قآ": "قآ",
"قٔ": "قٔ",
"قٕ": "قٕ",
"کَ": "کَ",
"کِ": "کِ",
"کُ": "کُ",
"کآ": "کآ",
"کٔ": "کٔ",
"کٕ": "کٕ",
"گَ": "گَ",
"گِ": "گِ",
"گُ": "گُ",
"گآ": "گآ",
"گٔ": "گٔ",
"گٕ": "گٕ",
"لَ": "لَ",
"لِ": "لِ",
"لُ": "لُ",
"لآ": "لآ",
"لٔ": "لٔ",
"لٕ": "لٕ",
"مَ": "مَ",
"مِ": "مِ",
"مُ": "مُ",
"مآ": "مآ",
"مٔ": "مٔ",
"مٕ": "مٕ",
"نَ": "نَ",
"نِ": "نِ",
"نُ": "نُ",
"نآ": "نآ",
"نٔ": "نٔ",
"نٕ": "نٕ",
"نٛ": "نٛ",
"وَ": "وَ",
"وِ": "وِ",
"وُ": "وُ",
"وآ": "وآ",
"ؤ": "ؤ",
"وٕ": "وٕ",
"وٚ": "وٚ",
"ۄ": "ۄ",
"وٗ": "وٗ",
"ہَ": "ہَ",
"ہِ": "ہِ",
"ہُ": "ہُ",
"ہآ": "ہآ",
"ۂ": "ۂ",
"ہٕ": "ہٕ",
"ھَ": "ھَ",
"ھِ": "ھِ",
"ھُ": "ھُ",
"ھآ": "ھآ",
"ھٔ": "ھٔ",
"ھٕ": "ھٕ",
"ءَ": "ءَ",
"ءِ": "ءِ",
"ءُ": "ءُ",
"ءآ": "ءآ",
"ءٔ": "ءٔ",
"ءٕ": "ءٕ",
"یَ": "یَ",
"یِ": "یِ",
"یُ": "یُ",
"یآ": "یآ",
"یٔ": "یٔ",
"یٕ": "یٕ",
"یٚ": "یٚ",
"ۍَ": "ۍَ",
"ۍِ": "ۍِ",
"ۍُ": "ۍُ",
"آۍ":"آۍ",
"ۍٔ": "ۍٔ",
"ۍٕ": "ۍٕ",
"ےَ": "ےَ",
"ےِ": "ےِ",
"ےُ": "ےُ",
"آے": "آے",
"ۓ": "ۓ",
"ےٕ": "ےٕ",
                                           
                                           }


def normalize_combine_characters(text: str) -> str:
    if not text:
        return text  # Return early if the text is empty
    
    # Step 1: Normalize to NFC
    normalized_text = unicodedata.normalize('NFC', text)
    
    # Step 2: Combine diacritics with base characters
    combined_text = []
    for char in normalized_text:
        if unicodedata.combining(char):
            # Attach diacritic to the previous character only if the list is not empty
            if combined_text:
                combined_text[-1] += char
            else:
                # If there's no previous character, just append the diacritic (or handle as needed)
                combined_text.append(char)
        else:
            # Append base character
            combined_text.append(char)

    # Return the combined text as a string
    return "".join(combined_text)






 
    


def punctuations_space(text: str) -> str:
    
    text = _SPACE_AFTER_PUNCTUATIONS_RE.sub(' ', text)
    text = _REMOVE_SPACE_BEFORE_PUNCTUATIONS_RE.sub(r'\1', text)
    return text


#def remove_diacritics(text: str) -> str:
    
    #return _DIACRITICS_RE.sub('', text)


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

    #text = remove_diacritics(text)
    
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    return text
