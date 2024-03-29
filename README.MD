# Resize-GAN-Research

It's a package for resizing ALL your dataset images (into local folder)

# Index

- [How it works?](#How-it-works?)
- [Warnings](#Warnings)
- [Install requirements](#Install-requirements)
- [Usage](#Usage)
- [Usage GUI](#GUI)
- [Usage Executable](#Executable)
- [Parameters](#Parameters)

### How it works?

- Walk by paths and searching by image format
- Resize the image

## Warnings

1º: Don't worry if you have a big folder structure with many nested folders, the package will walk recursively in your dataset folder and recreate the same structure into output_path.

## Install requirements

```
pip install -r requirements.txt
```

## Usage

```
python main.py -p <IMAGES> --output <IMAGES> --new_x <NEW_X_SIZE> --new_y <NEW_X_SIZE>
```

## Example

```
python main.py -p /images_example --output ./output --new_x 150 --new_y 150
```

## Executable

A portable .exe file is available in `/dist` to be run from any directory on machine that has python installed `run gui.exe` (might need to wait a little bit for the program to get started)

## GUI

If you are not comfortable using the command line to input parameters run `python gui.py` and follow the instructions on the GUI

![gui](./gui.png)

## Parameters

To know more about parameters use `python main.py -h`:

```
usage: main.py [-h] -p DATASET_PATH -o OUTPUT_PATH -x X -y Y [-m MODE]
```

| Parameter                         | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| **-h**, **--help**                | Show this help message and exit                     |
| **-p** **--path** _DATASET_PATH_  | Path to dataset data ?(image and annotations).      |
| **-o** **--output** _OUTPUT_PATH_ | Path that will be saved the resized dataset         |
| **-x** **--new_x** _X_            | The new x images size / scale / percentage / target |
| **-y** **--new_y** _Y_            | The new y images size / scale / percentage / target |
| **-m** **--mode** _MODE_          | The resize mode: size, scale, percentage or target  |
