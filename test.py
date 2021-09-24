import pytest
import os
import pandas as pd

def test_if_data_exists():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') != True
    
def test_if_model_exists():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') != True  
    
def test_if_numpy_exists():
    print(os.path.isfile('bottleneck_features_train.npy'))
    assert os.path.isfile('bottleneck_features_train.npy') != True      
    
def test_accuracy_score():
    df = pd.read_csv('metrics.csv')
    print((df['accuracy']>0.70))
    assert (df['accuracy']>0.70).unique() == True
    
def test_train_model_accuracy():
    df = pd.read_csv('metrics.csv')
    max_acc = df[df.state == "train"]["accuracy"].max()
    assert max_acc >= 0.70    
    
def test_valid_model_accuracy():
    df = pd.read_csv('metrics.csv')
    max_acc = df[df.state == "valid"]["accuracy"].max()
    assert max_acc >= 0.70        
    
    