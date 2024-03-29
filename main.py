import os
import argparse
from image import process_image
from utils import create_path, add_end_slash
from optparse import OptionParser

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p',
    '--path',
    dest='dataset_path',
    help='Path to dataset',
    required=True
)
parser.add_argument(
    '-o',
    '--output',
    dest='output_path',
    help='Path that will be saved the resized dataset',
    default='./',
    required=True
)
parser.add_argument(
    '-x',
    '--new_x',
    dest='x',
    help='The new x images size / scale / percentage / target',
    required=True
)
parser.add_argument(
    '-y',
    '--new_y',
    dest='y',
    help='The new y images size / scale / percentage / target',
    required=True
)

parser.add_argument(
    '-m',
    '--mode',
    dest='mode',
    help='Resize mode: size, scale, percentage or target',
    required=False
)

IMAGE_FORMATS = ('.jpeg', '.JPEG', '.png', '.PNG', '.jpg', '.JPG')

args = parser.parse_args()

create_path(args.output_path)

args.dataset_path = add_end_slash(args.dataset_path)
args.output_path = add_end_slash(args.output_path)

for root, _, files in os.walk(args.dataset_path):
        output_path = os.path.join(args.output_path, root[len(args.dataset_path):])
        create_path(output_path)
        for file in files:
            print(f"Resizing in File {file}")
            if file.endswith(IMAGE_FORMATS):
                file_path = os.path.join(root, file)
                process_image(file_path, output_path, args.x, args.y, args.mode)

print("DONE")