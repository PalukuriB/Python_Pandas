import pandas 

file_path = "C:\\Users\\palukuri.bhashwanth\\OneDrive - HCL TECHNOLOGIES LIMITED\\Desktop\\HCL\\Chinnu\\Python_Pandas\\pandas_data_set.csv"
data = pandas.read_csv(file_path)
df = pandas.DataFrame(data)
print(df.shape)
