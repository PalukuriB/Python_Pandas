import pandas as pd

data = pd.read_csv("C:\\Users\\palukuri.bhashwanth\\OneDrive - HCL TECHNOLOGIES LIMITED\\Desktop\\HCL\\Chinnu\\Python_Pandas\\basic.csv")
df = pd.DataFrame(data)
print(df)
# print(df.describe())
# print(df.shape)
# print(df[2:6:1])
# print(df['Physics'][0:11:2])
# print(df[['Hindi','Biology']][0:6:2])
# print(df[['Telugu','Maths']][0:11:2])
# for rec in df.iterrows():
#     print(rec)

# print(df.loc[5])
# print(df.loc[5,['Telugu','Chemistry']])
# print(df.loc[0:2,"student_name": "Biology"])
# print(df.loc[0:3, ["Hindi","Chemistry"]])
