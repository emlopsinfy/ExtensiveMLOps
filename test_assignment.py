import os

def check_if_data_exists():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') != True
    
def check_if_model_exists():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') != True  
    
    
    