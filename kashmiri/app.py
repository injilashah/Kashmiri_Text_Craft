import tkinter as tk
from tkinter import messagebox
from normalization.character import normalize, normalize_characters, _CORRECT_KASHMIRI_CHARACTERS_MAPPING, \
    normalize_combine_characters, COMBINE_KASHMIRI_CHARACTERS, replace_digits, \
    punctuations_space, remove_diacritics
from preprocess.character import digits_space, english_characters_space

# Define the normalization and preprocessing function
def apply_normalization_and_preprocessing():
    input_text = input_text_box.get("1.0", "end-1c")  # Get input text from the text box
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter some text to process.")
        return

    # Apply normalization and preprocessing functions
    try:
        # Step 1: Normalize Kashmiri text
        normalized_text = normalize(input_text)
        
        # Step 2: Preprocess - adjust spacing for digits and English characters
        preprocessed_text = digits_space(normalized_text)
        preprocessed_text = english_characters_space(preprocessed_text)
        
        # Display output
        output_text_box.delete("1.0", "end")  # Clear existing text
        output_text_box.insert("1.0", preprocessed_text)  # Insert final processed text
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create main application window
root = tk.Tk()
root.title("Kashmiri Text Processor")
root.geometry("800x600")  # Set window size to 800x600 pixels

# Input label and text box
input_label = tk.Label(root, text="Enter Kashmiri Text:", font=("Arial", 14))
input_label.pack(padx=10, pady=10)
input_text_box = tk.Text(root, height=10, width=80, font=("Arial", 12))  # Larger text box
input_text_box.pack(padx=20, pady=10)

# Normalize and preprocess button with larger padding
process_button = tk.Button(root, text="Normalize & Preprocess", command=apply_normalization_and_preprocessing, font=("Arial", 14))
process_button.pack(padx=10, pady=20)

# Output label and text box
output_label = tk.Label(root, text="Processed Text:", font=("Arial", 14))
output_label.pack(padx=10, pady=10)
output_text_box = tk.Text(root, height=10, width=80, font=("Arial", 12))  # Larger text box
output_text_box.pack(padx=20, pady=10)

# Start main loop
root.mainloop()
