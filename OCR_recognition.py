import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def do_the_thing(file):
    if file.lower().endswith('.pdf'):
        pics = convert_from_path(file)
        words = ""
        for pic in pics:
            words += pytesseract.image_to_string(pic)
    else:
        pic = Image.open(file)
        words = pytesseract.image_to_string(pic)
    return words

def process_stuff(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.pdf', '.png', '.jpg', '.jpeg'))]
    
    if len(files) == 1:
        file = files[0]
        path = folder + '/' + file
        if not os.path.exists(path.rsplit('.', 1)[0] + '.txt'):
            words = do_the_thing(path)
            save_text(folder, file, words)
        else:
            print(f"File {file} has already been processed.")
    elif len(files) > 1:
        for file in files:
            path = folder + '/' + file
            if not os.path.exists(path.rsplit('.', 1)[0] + '.txt'):
                words = do_the_thing(path)
                save_text(folder, file, words)
            else:
                print(f"File {file} has already been processed.")
    else:
        print("No suitable files found in the folder.")

def save_text(folder, filename, text):
    txt_filename = filename.rsplit('.', 1)[0] + '.txt'
    with open(folder + '/' + txt_filename, 'w') as f:
        f.write(text)
    print(f"Saved text from {filename} to {txt_filename}")

# Example usage
folder = '/home/zeus/Downloads/nse/jn'
process_stuff(folder)

# Scan a specific file
def scan_one_file(file):
    return do_the_thing(file)

# Example
my_file = '/home/zeus/Downloads/nse/jn/1.pdf'
result = scan_one_file(my_file)
print(f"Text from {my_file}:")
