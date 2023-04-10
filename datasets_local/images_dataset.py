from torch.utils.data import Dataset
from PIL import Image
from utils import data_utils
Image.LOAD_TRUNCATED_IMAGES = True


class ImagesDataset(Dataset):

    def __init__(self, source_root, target_root, opts, target_transform=None, source_transform=None):
        self.source_paths = sorted(data_utils.make_dataset(source_root, exit=False))
        self.target_paths = sorted(data_utils.make_dataset(target_root))
        # print("初始化source_paths", len(self.source_paths), " target_paths ", len(self.target_paths), "source_root",
        #       source_root, "target_root", target_root)
        self.source_transform = source_transform
        self.target_transform = target_transform
        self.opts = opts

    def __len__(self):
        return len(self.source_paths)

    def __getitem__(self, index):
        from_path = self.source_paths[index]
        print("开始加载", index, len(self.target_paths), " == ", from_path)
        from_im = Image.open(from_path)
        from_im = from_im.convert('RGB') if self.opts.label_nc == 0 else from_im.convert('L')

        to_path = self.target_paths[index]
        # print("to_path", to_path)
        to_im = Image.open(to_path).convert('RGB')
        if self.target_transform:
            to_im = self.target_transform(to_im)

        if self.source_transform:
            from_im = self.source_transform(from_im)
        else:
            from_im = to_im

        return from_im, to_im
