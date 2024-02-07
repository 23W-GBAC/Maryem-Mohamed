import PyPDF2
import pyttsx3

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

def text_to_speech(text, output_file='output.mp3'):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    pdf_path = 'your_pdf_file.pdf'  # Replace with the path to your PDF file
    output_audio_file = 'output.mp3'

    text_content = pdf_to_text(pdf_path)
    text_to_speech(text_content, output_audio_file)

    print(f"Conversion complete. Audio file saved as {output_audio_file}")
