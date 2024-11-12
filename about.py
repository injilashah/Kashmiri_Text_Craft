
"""Project Meta data description"""
import platform
from pathlib import Path
from typing import Dict

__version__ = '1.0.0'  # Adjust the version number accordingly
__description__ = 'Natural Language Processing (NLP) library for Kashmiri language.'
__url__ = 'https://github.com/injilashah/Kashmiri_normalizer.git'  # Replace with your repo URL
__author__ = 'INJILA SHAH'  # Replace with your name
__author_email__ = 'shahinjila435@gmail.com'  # Replace with your email


def get_info() -> Dict[str, str]:
   
    return {
        
        "location": str(Path(__file__).parent.parent),
        "platform": platform.platform(),
        "python_version": platform.python_version(), }
