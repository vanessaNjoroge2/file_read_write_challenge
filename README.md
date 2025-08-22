# File Read & Write Challenge with Error Handling

## Overview
This Python program demonstrates how to **read from a file, modify its content, and write to a new file** while handling errors gracefully. The program ensures that users cannot accidentally process non-existent files, making it robust and user-friendly.  

---

## Features
- Reads content from a user-specified file.
- Modifies the content (e.g., converts all text to uppercase).
- Writes the modified content to a new file (`modified_<original_filename>`).
- Handles errors gracefully:
  - `FileNotFoundError` if the original file does not exist.
  - `IOError` if the file cannot be read or written.
  - Other unexpected errors are caught and displayed.

---

## How to Use
1. Clone this repository or download the files.
2. Ensure you have Python 3 installed.
3. Create a sample text file (e.g., `sample.txt`) in the same directory.
4. Run the program:

```bash
python file_challenge.py
