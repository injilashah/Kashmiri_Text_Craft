
"""Project Meta data description"""
import platform
from pathlib import Path
from typing import Dict

__version__ = '1.0.0' 
__description__ = 'Natural Language Processing (NLP) library for Kashmiri language.'
__url__ = 'https://github.com/injilashah/Kashmiri_normalizer.git'  
__author__ = 'INJILA SHAH' 
__author_email__ = 'shahinjila435@gmail.com'  


def get_info() -> Dict[str, str]:
   
    return {
        "Kashmiri_normalizer_version": __version__,
        "location": str(Path(__file__).parent.parent),
        "platform": platform.platform(),
        "python_version": platform.python_version(), }
