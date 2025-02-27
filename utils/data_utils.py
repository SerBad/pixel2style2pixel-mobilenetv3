"""
Code adopted from pix2pixHD:
https://github.com/NVIDIA/pix2pixHD/blob/master/data/image_folder.py
"""
import os

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP', '.tiff'
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def make_dataset(dir, exit: bool = True):
    images = []
    if not os.path.exists(dir):
        os.makedirs(dir)
    assert os.path.isdir(dir), '%s is not a valid directory' % dir
    for root, _, fnames in sorted(os.walk(dir)):
        for fname in fnames:
            if is_image_file(fname):
                path = os.path.join(root, fname)
                if os.path.getsize(path) <= 0:
                    print("检查文件", os.path.getsize(path), path)
                # if os.path.getsize(path) > 0 or exit:
                if os.path.getsize(path) > 0:
                    images.append(path)
    return images
