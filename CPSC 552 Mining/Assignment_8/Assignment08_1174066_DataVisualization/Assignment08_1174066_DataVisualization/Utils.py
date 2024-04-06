from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

def read_data():
    # TCGA dataset from UCI
    #uci_tcga_url = the location of the file changed 
    #from "https://archive.ics.uci.edu/ml/machine-learning-databases/00401/"   
    #to search for TCGA-PANCAN-HiSeq-801x20531.tar.gz in "https://ics.uci.edu/~ddua/archive/usage_201902.html"

    #archive_name = "TCGA-PANCAN-HiSeq-801x20531.tar.gz"
    # above has already been extracted to the following files
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
    print(f"Shape of data: \n{data.shape}")
    print(f"\n First 5 rows and first 3 columns of data:\n{data[:5, :3]}")
    print(f"\n First 5 true label names:\n{true_label_names[:5]}")


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
    
    print(f"\n First 5 true labels: \n {true_labels[:5]}")
    print(f"\n Label encoder classes: \n {label_encoder.classes_}")

    return data, true_labels
