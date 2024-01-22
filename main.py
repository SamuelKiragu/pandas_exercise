import filter_data as f

dataframe_path = './Churn_Modelling.csv' # CSV File
start = 2 # Start Slice here
rows = 10 # No of rows to return

print(f.filter_data(dataframe_path, start, rows))
