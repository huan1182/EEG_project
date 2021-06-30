# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:35:25 2021

@author: Huyunting Huang
"""

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







































