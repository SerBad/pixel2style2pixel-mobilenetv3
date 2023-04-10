from PIL import Image
import os

#
# print(os.path.getsize("s.png"))

# from_im = Image.open("/home/zhou/Downloads/黄种人-FFHQ/55057.png")
from_im = Image.open("/kaggle/input/zhoudualstylegan/DualStyleGAN/data/yellow-FFHQ/46546.png")
print(from_im.getbands(), len(from_im.getbands()))
from_im = from_im.convert('RGB')
print(from_im.getbands(), len(from_im.getbands()))
# from_im.show()
