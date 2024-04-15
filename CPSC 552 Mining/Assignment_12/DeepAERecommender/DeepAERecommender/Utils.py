import pandas as pd
import numpy as np
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import matplotlib.pyplot as plt
from TrainDataset import TrainDataset
from TestDataset import TestDataset


def prepare_train_validation_movielens_step1():
    """
    Prepares training and validation datasets from MovieLens data.

    This function performs the following steps:
        1. Reads ratings and movies data from CSV files.
        2. Splits ratings into training and validation sets based on timestamps.
        3. Removes users and movies not present in both sets.
        4. Saves the prepared datasets to CSV files.
    """

    rat = pd.read_csv('data/ratings.csv')
    mov = pd.read_csv('data/movies.csv')
    df_combined = pd.merge(rat, mov, on='movieId')
    print(rat.describe())

    ts = rat['timestamp'].quantile(0.98)
    train_ratings = pd.DataFrame(columns=['userId', 'movieId', 'rating'])
    validation_ratings = pd.DataFrame(columns=['userId', 'movieId', 'rating'])

    for i in range(len(rat)):
        if rat['timestamp'].iloc[i] <= ts:
            train_ratings = pd.concat([train_ratings, pd.DataFrame([{'userId': rat['userId'].iloc[i],
                                                                   'movieId': rat['movieId'].iloc[i],
                                                                   'rating': rat['rating'].iloc[i]}])])
        else:
            validation_ratings = pd.concat([validation_ratings, pd.DataFrame([{'userId': rat['userId'].iloc[i],
                                                                             'movieId': rat['movieId'].iloc[i],
                                                                             'rating': rat['rating'].iloc[i]}])])

    if i % 10000 == 0:
        print(i, "Completed")

    print(len(train_ratings))
    print(len(validation_ratings))

    # Remove users in validation set not present in Training Set
    train_users = train_ratings['userId'].unique()
    users_not_in_train_set = []
    for i in range(1, 611):
        if i in train_users:
            continue
        else:
            users_not_in_train_set.append(i)

    for i in users_not_in_train_set:
        validation_ratings = validation_ratings[validation_ratings['userId'] != i]
    validation_ratings.reset_index(drop=True)

    print(len(train_ratings['movieId'].unique()))
    print(len(validation_ratings['movieId'].unique()))

    # Remove Movies that are not in the Train Set
    validation_movies = validation_ratings['movieId'].unique()
    train_movies = train_ratings['movieId'].unique()
    movies_not_in_train_set = []
    for i in validation_movies:
        if i in train_movies:
            continue
        else:
            movies_not_in_train_set.append(i)

    for i in movies_not_in_train_set:
        validation_ratings = validation_ratings[validation_ratings['movieId'] != i]
    validation_ratings.reset_index(drop=True)

    print('Train Users:', train_ratings['userId'].nunique())
    print('Validation Users:', validation_ratings['userId'].nunique())
    print('Train Movies:', train_ratings['movieId'].nunique())
    print('Validation Movies:', validation_ratings['movieId'].nunique())

    train_ratings.to_csv("data/train_ratings.csv")
    validation_ratings.to_csv("data/validation_ratings.csv")

def prepare_traintest_movielens_step2():
    """
    Prepares training and test datasets from preprocessed MovieLens data.

    This function assumes preprocessed training and validation data exist in CSV files
    and performs the following steps:
        1. Reads training and validation data from CSV files.
        2. Creates pivot tables (user-movie rating matrices) for training and test sets.
        3. Fills missing values with 0.
        4. Saves the prepared training and test datasets to CSV files.
    """

    tr_ratings = pd.read_csv('data/train_ratings.csv')
    val_ratings = pd.read_csv('data/validation_ratings.csv')

    train_dataset = tr_ratings.pivot_table(index='userId', columns='movieId', values='rating')
    train_dataset.fillna(0, inplace=True)
    print(train_dataset.head(10))

    test_dataset = val_ratings.pivot_table(index='userId', columns='movieId', values='rating')
    test_dataset.fillna(0, inplace=True)
    print(test_dataset.head(10))

    train_dataset.to_csv("data/train.csv")
    test_dataset.to_csv('data/test.csv')

def get_traintestloaders():
    """
    Prepares training and testing data loaders.

    This function defines data transformations, creates TrainDataset and TestDataset instances,
    and creates PyTorch DataLoaders for training and testing data.

    Returns:
        tuple: A tuple containing the training and testing data loaders.
    """

    transformations = transforms.Compose([transforms.ToTensor()])

    train_dat = TrainDataset('data/train.csv', transformations)
    test_dat = TestDataset('data/test.csv', transformations)

    train_loader = DataLoader(dataset=train_dat, batch_size=128, shuffle=True, num_workers=1)
    test_loader = DataLoader(dataset=test_dat, batch_size=128, shuffle=True, num_workers=1)

    return train_loader, test_loader

