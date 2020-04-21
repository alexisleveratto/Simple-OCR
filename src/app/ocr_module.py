from PIL import Image
import pytesseract

# allow files of a specific type
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

# function to check the file extension
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def searh_paragraph(extracted_text, search_words):
    if not search_words:
        return [extracted_text]

    search_words_list = search_words.split(",")
    extracted_text_list = extracted_text.split("\n")

    paragraphs = []

    for word in search_words_list:
        for text_paragraph in extracted_text_list:
            if word.lower() in text_paragraph.lower():
                paragraphs.append(text_paragraph)
    return paragraphs
