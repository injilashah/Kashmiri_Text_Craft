from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtGui import QColor,QFont



from normalization.character import normalize

from preprocess.character import digits_space, english_characters_space,all_punctuations_space

class Kashmiri_Text_Craft_GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set up the text editor for Kashmiri input
        self.input_text_box = QtWidgets.QTextEdit(self)
        self.input_text_box.setFixedSize(600, 150)
        self.input_text_box.setLayoutDirection(Qt.RightToLeft)  # Right-to-left layout
        self.input_text_box.setAlignment(Qt.AlignRight)  # Align the text to the right
        font = QFont("Arial", 19)  # Arial font with size 14
        self.input_text_box.setFont(font)
        
        
        # Set up the processed output text box
        self.output_text_box = QtWidgets.QTextEdit(self)
        self.output_text_box.setFixedSize(600, 150)
        self.output_text_box.setLayoutDirection(Qt.RightToLeft)
        self.output_text_box.setAlignment(Qt.AlignRight)
        self.output_text_box.setFont(font)
        self.output_text_box.setReadOnly(True) 

        # Normalize and Preprocess button
        self.process_button = QtWidgets.QPushButton('Click to Normalize and Preprocess', self)
        
        color = QColor(144, 238, 144) 
        
       
        self.process_button.setStyleSheet(f"background-color: {color.name()};")

        
        self.process_button.clicked.connect(self.process_text)
        
        
        # Layout for the application
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.input_text_box)
        layout.addWidget(self.process_button)
        layout.addWidget(self.output_text_box)

        self.setLayout(layout)

        # Set up window properties
        self.setWindowTitle("Kashmiri Normalizer & Preprocessor")
        self.setGeometry(100, 100, 640, 480)

    def process_text(self):
        """Function to preprocess and normalize Kashmiri text."""
        input_text = self.input_text_box.toPlainText()


        # Step 1: Normalize the input text
        
        normalized_text = normalize(input_text)


        # Step 2: Apply preprocessing (handling digits and English words)
        processed_text = self.apply_preprocessing(normalized_text)

         

        # Step 3: Output the processed and normalized text
        self.output_text_box.setText(processed_text)

    def apply_preprocessing(self, text):
        """Function to apply preprocessing steps."""
        # Applying preprocessing: handling digits and English words
        text = digits_space(text)
        text = english_characters_space(text)
        text = all_punctuations_space(text)
        
        return text


# Run the application
app = QtWidgets.QApplication(sys.argv)
window = Kashmiri_Text_Craft_GUI()
window.show()
sys.exit(app.exec_())
