from gtts import gTTS
import os
import PyPDF2

def read_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()

    if file_extension == '.txt':
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif file_extension == '.pdf':
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

def text_to_speech(file_path, output_file):
    try:
        text_content = read_file(file_path)
        if not text_content.strip():
            print("No readable content found in the file.")
            return

        tts = gTTS(text_content)
        tts.save(output_file)
        print(f"MP3 file saved as: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file (e.g., .txt or .pdf): ").strip()
    output_file = input("Enter the name of the output MP3 file (e.g., output.mp3): ").strip()
    text_to_speech(file_path, output_file)



## /path/to/file.txtpdf
## output.mp3