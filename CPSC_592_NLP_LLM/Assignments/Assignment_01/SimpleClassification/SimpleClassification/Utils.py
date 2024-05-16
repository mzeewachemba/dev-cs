import torch
from MyDataSet import MyDataset  # Assuming MyDataSet.py is in the same directory
import torchvision
import matplotlib.pyplot as plt


def get_train_loader(data_dir, batch_size, transform=None):
    dataset = MyDataset(data_dir, transform=transform)
    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, shuffle=True, num_workers=4, pin_memory=True, drop_last=True
    )
    return data_loader


def get_test_loader(data_dir, batch_size, transform=None):
    dataset = MyDataset(data_dir, transform=transform)
    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=batch_size, shuffle=False, num_workers=4, pin_memory=True
    )
    return data_loader


def plot_images(images, labels):
    img_grid = torchvision.utils.make_grid(images, nrow=4, normalize=True)
    np_img = img_grid.numpy().transpose(1, 2, 0)  # pytorch has the order, c,w,h
    plt.imshow(np_img)
    plt.show()

