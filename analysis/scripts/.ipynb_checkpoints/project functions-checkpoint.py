import pandas as pd
import numpy as np

#Step 2
##wrap method chains in function

def load_and_process(path_to_directory):
    
    ##method chaining (load and clean)
    df1 = (
pd.read_csv("/Users/aidenb/Documents/Year_3/DATA_301/Project/Datafiniti_Fast_Food_Restaurants.csv")
    
    .dropna()
)
    
    #method chaining (process)
    df2 = (
        df
    .drop([
        'address',
        'keys',
        'latitude',
        'longitude',
        'postalCode',
        'websites',
        'sourceURLS',
        'id',
        'dateAdded',
        'dateUpdated',
        'categories'],
        axis = 1)
    )
    return df2
