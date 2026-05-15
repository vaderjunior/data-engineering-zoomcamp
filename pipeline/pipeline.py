import sys
import pandas as pd



print('arguments', sys.argv)

month = int(sys.argv[1])

df= pd.DataFrame({"Day":[1,2], "Present": [3,4]})

df['month']= month
print(df.head())

df.to_parquet()

print(f'Hello Pipeline, month={month}')
