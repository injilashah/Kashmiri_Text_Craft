# coding: utf8
"""
Complete collection of Urdu Unicode characters.
Maintainer: Ikram Ali(mrikram1989@gmail.com)
version = 2020.04.07
Source = https://github.com/urduhack/urdu-characters
"""

from typing import FrozenSet, Dict

# Urdu Alphabets
URDU_ALPHABETS: FrozenSet[str] = frozenset("آ أ ا ب پ ت ٹ ث "
                                           " ج چ ح خ "
                                           " د ڈ ذ ر ڑ ز ژ "
                                           " س ش ص ض ط ظ ع غ "
                                           " ف ق ک گ ل م "
                                           " ن ں و ؤ ہ ۂ ۃ "
                                           " ھ ء ی ئ ے ۓ ".split())
KASHMIRI_ALPHABETS: FrozenSet[str] = frozenset("ٲ ا آ ٳ  إ أ ب پ  ت  ٹ ٹھ ث ٮ۪ "
                                           "ج چ  ح خ "
                                           " د ڈ ذ ډ ر ڑ ز ژ "
                                           "س ش ص ض ط ظ ع غ "
                                           "ف ق ک  گ ل م "
                                           "ن ں و ؤ ۄ ۅ  ۆ ة ہ "
                                           " ھ ء ی ؠ ۍ ے ".split())


# Urdu Digits from 0 to 9
URDU_DIGITS: FrozenSet[str] = frozenset("۰ ۱ ۲ ۳ ۴ ۵ ۶ ۷ ۸ ۹".split())

# Urdu Punctuations
URDU_PUNCTUATIONS: FrozenSet[str] = frozenset("؛ ، ٫  ؟ ۔ ٪".split())

# Urdu Aerabs
#URDU_DIACRITICS: FrozenSet[str] = frozenset("\u064e \u064B \u0670 \u0650 \u064F \u064d".split())
KASHMIRI_DIACRITICS :FrozenSet[str] = frozenset("\u064e \u0622 \u0627 \u0623 \u0654 \u0672 \u0650 \u06CC \u0656 \u0625 \u0655 \u0673 \u065F \u064F \u0648 \u0657 \u06C6 \u06C4 \u065A \u06D2 \u065A \u0620 ".split())

# Urdu Extra Characters
URDU_EXTRA_CHARACTERS: FrozenSet[str] = frozenset(" ؀ ؁ ؂ ؃ ؍ ؎ ؏ ؐ ؑ ؒ ؓ ؔ ؕ ٌ ّ ْ ٓ ٔ ٖ ٗ ٘ ٬".split())
KASHMIRI_EXTRA_CHARACTERS: FrozenSet[str] = frozenset(" ،  ٍ  ء  ٰ  ّ  ٗ  ُ  ۭ  ٖ  ۄ ۍ  ٕ  ِ  َ  ؟   ".split())

# Complete list of Urdu language Characters.
URDU_ALL_CHARACTERS: FrozenSet[str] = frozenset().union(URDU_ALPHABETS, URDU_DIGITS, URDU_PUNCTUATIONS,  # type: ignore
                                                        URDU_DIACRITICS, URDU_EXTRA_CHARACTERS)  # type: ignore

URDU_ALL_CHARACTERS_UNICODE: Dict[str, str] = {'\u0600': '\u0600',
                                               '\u0601': '\u0601',
                                               '\u0602': '\u0602',
                                               '\u0603': '\u0603',
                                               '،': '\u060c',
                                               '؍': '\u060d',
                                               '؎': '\u060e',
                                               '؏': '\u060f',
                                               'ؐ': '\u0610',
                                               'ؑ': '\u0611',
                                               'ؒ': '\u0612',
                                               'ؓ': '\u0613',
                                               'ؔ': '\u0614',
                                               'ؕ': '\u0615',
                                               '؛': '\u061b',
                                               '؟': '\u061f',
                                               'ء': '\u0621',
                                               'ً': '\u064b',
                                               'ٌ': '\u064c',
                                               'ٍ': '\u064d',
                                               'َ': '\u064e',
                                               'ُ': '\u064f',
                                               'ِ': '\u0650',
                                               'ّ': '\u0651',
                                               'ْ': '\u0652',
                                               'ٓ': '\u0653',
                                               'ٔ': '\u0654',
                                               'ٖ': '\u0656',
                                               'ٗ': '\u0657',
                                               '٘': '\u0658',
                                               '٪': '\u066a',
                                               '٫': '\u066b',
                                               '٬': '\u066c',
                                               'ٰ': '\u0670',
                                               '۔': '\u06d4',
                                               'آ': '\u0622',
                                               'أ': '\u0623',
                                               'ا': '\u0627',
                                               'ب': '\u0628',
                                               'پ': '\u067e',
                                               'ت': '\u062a',
                                               'ٹ': '\u0679',
                                               'ث': '\u062b',
                                               'ج': '\u062c',
                                               'چ': '\u0686',
                                               'ح': '\u062d',
                                               'خ': '\u062e',
                                               'د': '\u062f',
                                               'ڈ': '\u0688',
                                               'ذ': '\u0630',
                                               'ر': '\u0631',
                                               'ڑ': '\u0691',
                                               'ز': '\u0632',
                                               'ژ': '\u0698',
                                               'س': '\u0633',
                                               'ش': '\u0634',
                                               'ص': '\u0635',
                                               'ض': '\u0636',
                                               'ط': '\u0637',
                                               'ظ': '\u0638',
                                               'ع': '\u0639',
                                               'غ': '\u063a',
                                               'ف': '\u0641',
                                               'ق': '\u0642',
                                               'ک': '\u06a9',
                                               'گ': '\u06af',
                                               'ل': '\u0644',
                                               'م': '\u0645',
                                               'ن': '\u0646',
                                               'ں': '\u06ba',
                                               'و': '\u0648',
                                               'ؤ': '\u0624',
                                               'ھ': '\u06be',
                                               'ہ': '\u06c1',
                                               'ۂ': '\u06c2',
                                               'ۃ': '\u06c3',
                                               'ی': '\u06cc',
                                               'ئ': '\u0626',
                                               'ے': '\u06d2',
                                               'ۓ': '\u06d3',
                                               '۰': '\u06f0',
                                               '۱': '\u06f1',
                                               '۲': '\u06f2',
                                               '۳': '\u06f3',
                                               '۴': '\u06f4',
                                               '۵': '\u06f5',
                                               '۶': '\u06f6',
                                               '۷': '\u06f7',
                                               '۸': '\u06f8',
                                               '۹': '\u06f9',
                                               }

KASHMIRI_ALL_CHARACTERS_UNICODE: Dict[str, str] = {
                                               '،': '\u060c',
                                               '؛': '\u061b',
                                               '؟': '\u061f',
                                               'ء': '\u0621',
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
                                               'غ': '\u063a',
                                               'ف': '\u0641',
                                               'ق': '\u0642',
                                               'ک': '\u06a9',
                                               #'کھ': u'\u0643\u06BE',
                                               'گ': '\u06af',
                                               'ل': '\u0644',
                                               'م': '\u0645',
                                               'ن': '\u0646',
                                               'ں': '\u06ba',
                                               'و': '\u0648',
                                               'ھ': '\u06be',
                                               'ہ': '\u06c1',
                                               'ی': '\u06cc',
                                               'ؠ': '\u0620',
                                               'ے': '\u06d2',
                                               'أ': u'\u0623',
                                               'ٲ' : '\u0672',
                                               'آ': u'\u0622\u0627',
                                               'اِ' : '\u0650',
                                              'إ' : '\u0625',
                                              'ٳ' : '\u0673',
                                              'اُ' : '\u064F',
                                              'اوٗ': '\u0648\u0657',
                                              'اۆ' : '\u06C6',
                                              'او' : '\u0648',
                                              'اۄ' : '\u06C4',
                                              'اۄا' : '\u06C4\u0627',
                                              'ایٚـ ': '\u06CC\u065A',   
                                              'اےٚ' : '\u06CC\u065A',
                                              'ایـ' : '\u06CC',
                                              'اے': '\u06D2',
                                              'اؠـ' : '\u0620',
                                              'اؠے':'\u0620',
                                               
                                               ' ِ' : '\0u650',
                                               ' َ' : '\0u54E',
                                               ' ُ' : '\0u64F',
                                               ' ٗ' : '\0u657',
                                               ' ٔ' : '\0u655',
                                               ' ٕ' : '\0u654',
                                               ' ٛ' : '\0u65B',
                                               ' ٚ' : '\u065A',
                                               ' ً' : '\u064D',
                                               ' ُ' : '\u064F',
                                               '۔' : '\u06D4',
                                               ' ٰ' : '\u0656',
                                               '۰': '\u06f0',
                                               '۱': '\u06f1',
                                               '۲': '\u06f2',
                                               '۳': '\u06f3',
                                               '۴': '\u06f4',
                                               '۵': '\u06f5',
                                               '۶': '\u06f6',
                                               '۷': '\u06f7',
                                               '۸': '\u06f8',
                                               '۹': '\u06f9',
                                               'ۍ' : '\u06CD',
                                              #'ٮ۪'  : '\u'wavy hamza
  
                                      }
