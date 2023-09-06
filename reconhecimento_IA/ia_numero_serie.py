from PIL import Image
import pytesseract


def main(n_serie_path):
    return pytesseract.image_to_string(Image.open(n_serie_path)).strip()
