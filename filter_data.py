import pandas as pd

# filepath: path of the data file
# start: index to start slicing operation
# n: number of rows to be sliced
def filter_data(filepath, start, n):
    filtered_data = []
    df = pd.read_csv(filepath) # Read data frame
    df = df.iloc[start: start+n] # Split the data

    for row in df.values:
        dict = {k:v for k,v in zip(df.columns, row)}
        filtered_data.append(dict)

    return filtered_data

def filter_males(filepath):
    pass