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

# filepath: path of the data file
# output: dataset with males only
def filter_males(filepath):
    filtered_data = []
    df = pd.read_csv(filepath) # Read data frame
    filtered_data = df.groupby(by="Gender").get_group("Male")
    return filtered_data

# filepath: path of the data file
# output: dataset with female only
def filter_females(filepath):
    df = pd.read_csv(filepath) # Read data frame
    filtered_data = df.groupby(by="Gender").get_group("Female")
    return filtered_data

# dataframe: the data frame to convert
# desired_path: the desired path
# output: csv file
def create_csv(dataframe, desired_path, output):
    pass