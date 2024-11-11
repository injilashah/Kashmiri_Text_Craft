

from typing import FrozenSet, Dict

# Urdu Alphabets

KASHMIRI_ALPHABETS: FrozenSet[str] = frozenset("ٲ ا آ ٳ  إ أ ب پ  ت  ٹ ٹھ ث ٮ۪ "
                                           "ج چ  ح خ "
                                           " د ڈ ذ ډ ر ڑ ز ژ "
                                           "س ش ص ض ط ظ ع غ "
                                           "ف ق ک  گ ل م "
                                           "ن ں و ؤ ۄ ۅ  ۆ ة ہ "
                                           " ھ ء ی ؠ ۍ ے ".split())


# KASHMIRI Digits from 0 to 9
KASHMIRI_DIGITS: FrozenSet[str] = frozenset("۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹".split())

# KASHMIRI Punctuations
KASHMIRI_PUNCTUATIONS: FrozenSet[str] = frozenset("؛ ، ٫  ؟ ۔ ٪".split())


#KASHMIRI_DIACRITICS: FrozenSet[str] = frozenset("\u064e \u064B \u0670 \u0650 \u064F \u064d".split())
KASHMIRI_DIACRITICS :FrozenSet[str] = frozenset("\u064E \u064F \u064B \u064D   \u0650   \u0651 \u0652    \u0654  \u0655 \u0656  \u0657 \u065A \u065B \u065C \u065D  \u065F   \u0657   \u065A  \u0670 \u0674 ".split())

# KASHMIRI Extra Characters
KASHMIRI_EXTRA_CHARACTERS: FrozenSet[str] = frozenset(" ؀ ؁ ؂ ؃ ؍ ؎  ؐ ؑ ؒ ؓ ؔ ؕ ٌ ّ ْ ٓ ٔ ٖ ٗ ٘ ٬ ".split())


# Complete list ofKASHMIRI language Characters.
KASHMIRI_ALL_CHARACTERS: FrozenSet[str] = frozenset().union(KASHMIRI_ALPHABETS, KASHMIRI_DIGITS, KASHMIRI_PUNCTUATIONS,  # type: ignore
                                                       KASHMIRI_DIACRITICS, KASHMIRI_EXTRA_CHARACTERS)  # type: ignore

                               
                               
                          

KASHMIRI_ALL_CHARACTERS_UNICODE: Dict[str, str] = {
                                               '،': '\u060c',
                                               '؛': '\u061b',
                                               '؟': '\u061f',
                                               '٪': '\u066a',
                                               '٬': '\u066c',
                                               
                                               'ا': '\u0627',
                                               'ب': '\u0628',
                                               'پ': '\u067e',
                                               #'پھ':  u'[U+067E]+[U+06BE]'
                                               #'پھ': u'\u067E\u06BE',
                                               'ت': '\u062a',
                                               #'تھ':  u'\u062A\u06BE',
                                               'ٹ': '\u0679',
                                               #'ٹھ':  u'\u0679\u06BE',
                                               'ث': '\u062b',
                                               'ج': '\u062c',
                                               'چ': '\u0686',
                                               #'چھ': u'\u0686\u06BE',
                                               'ح': '\u062d',
                                               'خ': '\u062e',
                                               'د': '\u062f',
                                               'ډ': '\u0689',
                                               'ڈ': '\u0688',
                                               'ذ': '\u0630',
                                               'ر': '\u0631',
                                               'ڑ': '\u0691',
                                               'ز': '\u0632',
                                               'ژ': '\u0698',
                                               #'ژھ': u'\u698\u06BE',
                                               'س': '\u0633',
                                               'ش': '\u0634',
                                               'ص': '\u0635',
                                               'ض': '\u0636',
                                               'ط': '\u0637',
                                               'ظ': '\u0638',
                                               'ع': '\u0639',
                                               'غ': '\u063A',
                                               'ف': '\u0641',
                                               'ق': '\u0642',
                                               'ک': '\u06A9',
                                               #'کھ': u'\u0643\u06BE',
                                               'گ': '\u06AF',
                                               'ل': '\u0644',
                                               'م': '\u0645',
                                               'ن': '\u0646',
                                               'ں': '\u06BA',
                                               'و': '\u0648',
                                               'ھ': '\u06BE',
                                               'ہ': '\u06C1',
                                               'ء': '\u0621',
                                               'ی': '\u06CC',
                                               'ؠ': '\u0620',
                                               'ۍ': '\u06CD',
                                               'ٮ': '\u066E',
                                               'ے': '\u06D2',
                                               'أ':  '\u0623',
                                               'ٲ':  '\u0672',
                                               'آ':  '\u0622',
                                               'اِ':  '\u0650',
                                               'إ':  '\u0625',
                                               'ٳ':  '\u0673',
                                               'اُ':  '\u064F',
                                               'ۇ':  '\u06C7',
                                               'ۈ':  '\u06C8',
                                               'ۉ':  '\u06C9',
                                               'ۆ': '\u06C6',
                                               'ۄ':  '\u06C4',   
                                               'ۅ':  '\u06C5',
                                             
                                               ' ِ' : '\0u650',
                                               ' َ' : '\0u54E',
                                               ' ُ' : '\0u64F',
                                               ' ٗ' : '\0u657',
                                               ' ٔ' : '\0u655',
                                               ' ٕ' : '\0u654',
                                               ' ٛ' : '\0u65B',
                                               ' ٚ' : '\u065A',
                                               ' ٍ' : '\u064D',
                                               ' ً' : '\u064B', 
                                               '۔' : '\u06D4',
                                               ' ٰ' : '\u0656',
                                               ' ً' : '\u064B ',
                                               ' ّ' : '\u0651',
                                               ' ْ' : '\u0652 ',
                                              '  ٜ' : '\u065C',
                                               ' ٝ' : '\u065D ',
                                               ' ٟ' : '\u065F',
                                               ' ٰ' : '\u0670 ',
                                               'ٴ ':  '\u0674 ',
                                               
                                               '۰': '\u06F0',
                                               '۱': '\u06F1',
                                               '۲': '\u06F2',
                                               '۳': '\u06F3',
                                               '۴': '\u06F4',
                                               '۵': '\u06F5',
                                               '۶': '\u06F6',
                                               '۷': '\u06F7',
                                               '۸': '\u06F8',
                                               '۹': '\u06F9',
                                               

  
                                      }
