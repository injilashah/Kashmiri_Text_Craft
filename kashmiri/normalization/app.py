import tkinter as tk
from tkinter import messagebox

from character import normalize_characters, _CORRECT_KASHMIRI_CHARACTERS_MAPPING, \
    normalize_combine_characters, COMBINE_KASHMIRI_CHARACTERS, replace_digits
from character import punctuations_space, remove_diacritics

# Define the normalization function
def apply_normalization():
    input_text = input_text_box.get("1.0", "end-1c")  # Get the input text from the text box
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter some text to normalize.")
        return

    # Apply the normalization function (using your 'normalize' function)
    try:
        normalized_text = normalize(input_text)  # Call the normalize function from your project
        output_text_box.delete("1.0", "end")  # Clear any existing text in the output box
        output_text_box.insert("1.0", normalized_text)  # Insert normalized text into the output box
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Kashmiri Normalizer")

# Create and pack the input label and text box
input_label = tk.Label(root, text="Enter Kashmiri Text:")
input_label.pack(padx=10, pady=5)

input_text_box = tk.Text(root, height=5, width=40)
input_text_box.pack(padx=10, pady=5)

# Create and pack the normalize button
normalize_button = tk.Button(root, text="Normalize", command=apply_normalization)
normalize_button.pack(padx=10, pady=5)

# Create and pack the output label and text box
output_label = tk.Label(root, text="Normalized Text:")
output_label.pack(padx=10, pady=5)

output_text_box = tk.Text(root, height=5, width=40)
output_text_box.pack(padx=10, pady=5)

# Start the main loop
root.mainloop()
