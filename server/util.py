import json
import pickle
import numpy as np
##defining the global variables
__locations=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)
def get_locations_names():
    return __locations
def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    with open("./artifacts/columns1.json","r") as f:
        __data_columns=json.load(f)['data_columns']#json key value pair so passing the key
        __locations=__data_columns[3:]#taking from the 3rd column with everything else included
    with open("./artifacts/HousePricePredicyionBanglore.pickle","rb") as f:
        __model=pickle.load(f)
        print("loading saved artifacts...done")

if __name__=="__main__":
    load_saved_artifacts()
    print(get_locations_names())
    print(get_estimated_price('1st phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('kalhalli', 1000, 2, 2))#other location
    print(get_estimated_price('Ejipura', 1000, 2,2))#other location
