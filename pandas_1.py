from faker import Faker
import pandas
import random

fake = Faker()
print(pandas.__version__)
number = 25

data = {'name_of_the_student': [fake.name() for _ in range(1,number+1)],
        'Telugu': [random.randint(35,100) for _ in range(1,number+1)],
        'Hindi': [random.randint(35,100) for _ in range(1,number+1)],
        'Maths': [random.randint(35,100) for _ in range(1,number+1)],
        'English': [random.randint(35,100) for _ in range(1,number+1)],
        'Physics': [random.randint(35,100) for _ in range(1,number+1)],
        'Chemistry': [random.randint(35,100) for _ in range(1,number+1)]}

df = pandas.DataFrame(data)
print(df)

        

