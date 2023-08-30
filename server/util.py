import json
import pickle
import numpy as np
__location = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    saved_artifacts()
    return __location

def saved_artifacts():
    print("Loading... Saved Artifacts...")
    global __location
    global __data_columns
    global __model
    with open(r"./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]
    with open(r"./artifacts/bangalore_home_prices_model.pickel", "rb") as f:
        __model = pickle.load(f)
    print("Loaded... Saved Artifacts...")


saved_artifacts()
