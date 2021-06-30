# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:35:25 2021

@author: Huyunting Huang
"""
from __future__ import print_function,division
import os
import torch
import glob
import numpy as np
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms


import pandas as pd

def data_create(path):
    data=pd.read_csv(path)
    data.columns=['time', 'chan1','chan2','chan3','chan4','chan5','chan6','chan7','chan8']
    return data


def address_reader(pre,research_num=1,day_num=1):
    name=pre+"/Research "+str(research_num)+"/Day "+str(day_num)+"/Day "+str(day_num)+".csv"
    return name

def add_label(length,label,data):
    label0= pd.DataFrame(label, columns=['label'])
    data['label']=label0
    return data


class EEGDataset(Dataset):

    class_to_id = {"ill": 0, "non_ill": 1}
    
    def __init__(self, data_root, transform=None):
        super().__init__()
        self.data_root = data_root
        self.transform = transform
        self.eeg_files = glob.glob(os.path.join(self.data_root, "**", "*.npy"))
        # print(self.eeg_files)
 
    def __getitem__(self, index):
        eeg_file = self.eeg_files[index]
        eeg_data = np.load(eeg_file)
        label = os.path.basename(os.path.dirname(eeg_file))

        if self.transform is not None:
            eeg_data = self.transform(eeg_data)

        return eeg_data, self.class_to_id[label]
 
    def __len__(self):
        return len(self.eeg_files)


if __name__ == "__main__":
    
    train_transforms = transforms.Compose([
        transforms.ToTensor()
    ])
    eeg_dataset = EEGDataset("data", transform=train_transforms)

    train_loader = DataLoader(dataset=eeg_dataset, batch_size=1, shuffle=True)
    for data, label in train_loader:
        print(label)

































