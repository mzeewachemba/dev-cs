import torch
from MyDataSet import MyDataSet
from torch.utils.data import DataLoader
from torch.utils.data.dataset import random_split
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def get_train_test_loaders(batch_size):
    datafile = "E:/16.Data_for_assignments/CPSC552/TCGA-PANCAN-HiSeq-801x20531/data.csv"
    labels_file = "E:/16.Data_for_assignments/CPSC552/TCGA-PANCAN-HiSeq-801x20531/labels.csv"
    data = np.genfromtxt(
        datafile,
        delimiter=",",
        usecols=range(1, 20532),
        skip_header=1
    )
    true_label_names = np.genfromtxt(
        labels_file,
        delimiter=",",
        usecols=(1,),
        skip_header=1,
        dtype="str"
    )
    print(type(data))
    print(data.shape)
    print(data[:5, :3])
    print(true_label_names[:5])
    
    # The data variable contains all the gene expression values
    # from 20,531 genes. The true_label_names are the cancer
    # types for each of the 801 samples.
    # BRCA: Breast invasive carcinoma
    # COAD: Colon adenocarcinoma
    # KIRC: Kidney renal clear cell carcinoma
    # LUAD: Lung adenocarcinoma
    # PRAD: Prostate adenocarcinoma
    # we need to convert the labels to integers with LabelEncoder:
    label_encoder = LabelEncoder()
    true_labels = label_encoder.fit_transform(true_label_names)
    print(true_labels[:5])
    print(label_encoder.classes_)
    
    dmax = data.max()
    x_tensor = torch.from_numpy(data).float() / dmax  # max scaling
    y_tensor = torch.from_numpy(true_labels).int()
    
    mydataset = MyDataSet(x_tensor, y_tensor)
    train_dataset, test_dataset = random_split(mydataset, [len(mydataset) - 150, 150])
    train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size)
    test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size)
    
    return train_loader, test_loader
