# Text-to-Speech Converter

![image](https://github.com/user-attachments/assets/e571f11e-1eb4-4a91-974c-23964166223d)


This project is a Python-based script that converts text from files (like `.txt` and `.pdf`) into an `.mp3` audio file using **Google Text-to-Speech (gTTS)**. The script also includes support for multi-language conversion and customizable options for better user experience.

---

## Features
- **File Support**: Supports `.txt` (plain text) and `.pdf` (extracts text from all pages).
- **Dynamic Input**: Prompts the user for input and output file paths.
- **Multi-Language Support**: Converts text to speech in different languages (default is English).
- **Efficient and Fast**: Handles large files efficiently.
- **Customizable Output**: Users can specify the output `.mp3` file name.
- **Error Handling**: Detects and handles issues like unsupported file types or empty files.

---

## Requirements
### Prerequisites
1. **Python**: Python 3.x installed on your system. Download it from [python.org](https://www.python.org/).
2. Required Python libraries:
   - `gTTS`: For text-to-speech conversion.
   - `PyPDF2`: For reading and extracting text from PDF files.

### Install Required Libraries
Run the following command to install the necessary libraries:
```bash
pip install gTTS PyPDF2
