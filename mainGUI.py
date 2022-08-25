import os
from image import process_image
from utils import create_path, add_end_slash


IMAGE_FORMATS = ('.jpeg', '.JPEG', '.png', '.PNG', '.jpg', '.JPG')


def mainCall(path,out,x,y,mode=None):

    create_path(out)

    path = add_end_slash(path)
    out = add_end_slash(out)

    for root, _, files in os.walk(path):
            output_path = os.path.join(out, root[len(path):])
            create_path(output_path)
            for file in files:
                print(f"Resizing in File {file}")
                if file.endswith(IMAGE_FORMATS):
                    file_path = os.path.join(root, file)
                    process_image(file_path, output_path, x, y, mode)

    print("DONE")