import pandas as pd

df = pd.DataFrame(
    {
        'name': ['John', 'Sam'],
        'age': [10, 30]    
    }
)

x = df.isnull().sum()
print(df['age'].mean())

df_2 = pd.read_csv('sample.csv')