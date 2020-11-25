#Step 2
##wrap method chains in function

def load_and_process(path_to_directory):
    
    ##method chaining (load and clean)
    df1 = (
pd.read_csv("https://raw.githubusercontent.com/data301-2020-winter1/course-project-solo_200/main/data/raw/FastFoodRestaurants.csv?token=ARAL4ZNEP46YNJJAVWW7T2C7X26OI")
    
    .dropna()
)
    
    #method chaining (process)
    df2 = (
        df
    .drop([
        'address',
        'keys',
        'websites'],
        axis = 1)
    )
    return df2
