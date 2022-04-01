import os
import platform

from PIL import Image  # pillow library


def make_pdf_all(dir_path):
    if platform.system() == "Windows":
        join = str("/")
        dir_files = [dir_path + join + f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return dir_files

    elif platform.system() == "Linux":
        join = str('\'')
        dir_files = [dir_path + join + f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return dir_files

def make_pdf_only_selected(selected_files, file_name, pdf_location):
    images_list = []
    for f in selected_files:
        try:
            images_list.append((Image.open(f)).convert('RGB'))
        except IOError:
            pass
    os.chdir(pdf_location)
    images_list[0].save(file_name, save_all=True, append_images=images_list[1:])

def make_doc_to_pdf(selected_file, pdf_location, pdf_name):
    import os

    from docx2pdf import convert

    dir_name = pdf_location
    base_filename = str(pdf_name)
    

    output_file = os.path.join(dir_name, base_filename)

    convert(selected_file, output_file)


def convert_pdf2doc(selected_file, pdf_location, pdf_name):
    import os
    from pdf2docx import Converter

    dir_name = pdf_location
    base_filename = str(pdf_name)
    output_file = os.path.join(dir_name, base_filename)

    pdf_file = selected_file
    docx_file = output_file

    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

if __name__ == '__main__':
    print("This Is The Main Backend Module!")
