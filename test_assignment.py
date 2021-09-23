import os

def test_if_data_exists():
    print(os.path.isdir('data'))
    assert os.path.isdir('data') != True
    
def test_if_model_exists():
    print(os.path.isfile('model.h5'))
    assert os.path.isfile('model.h5') != True  
    
    
    