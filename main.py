import filter_data as f

dataframe_path = './Churn_Modelling.csv' # CSV File
start = 2 # Start Slice here
rows = 10 # No of rows to return

# Test function filter_data
# print(f.filter_data(dataframe_path, start, rows))

# Test function filter_female
print(f.filter_females(dataframe_path))

# Test function filter_male
print(f.filter_males(dataframe_path))