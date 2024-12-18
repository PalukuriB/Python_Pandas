from faker import Faker
import pandas 
import random

print(pandas.__version__)
fake = Faker()
num = 30
data = {'student_name': [fake.name() for _ in range(1,num+1)],
        'Telugu': [random.randint(34,100) for _ in range(1,num+1)],
        'Hindi': [random.randint(34,100) for _ in range(1,num+1)],
        'Maths': [random.randint(34,100) for _ in range(1,num+1)],
        'Physics': [random.randint(34,100) for _ in range(1,num+1)],
        'Chemistry': [random.randint(34,100) for _ in range(1,num+1)],
        'Biology': [random.randint(50,100) for _ in range(1,num+1)]}

df = pandas.DataFrame(data)
# file_path = "C:\\Users\\palukuri.bhashwanth\\OneDrive - HCL TECHNOLOGIES LIMITED\\Desktop\\HCL\\Chinnu\\Python_Pandas\\basic.csv"
# print(df.to_csv(file_path)) 
df["Total"]= df['Telugu']+df['Hindi']+df['Maths']+df['Physics']+df['Chemistry']+df['Biology']
l=[]
for rec in df['Total']:
        l.append(rec)
for i in l:
        df["percentage"] = df['Total'].apply(lambda x: 'Pass' if x>=350 else 'Fail')
print(df)
