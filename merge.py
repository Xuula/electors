import os
import pandas as pd

directory = 'data/'

csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

df = pd.DataFrame()

for csv_file in csv_files:
    df_temp = pd.read_csv(os.path.join(directory, csv_file))
    df = pd.concat([df, df_temp])


df.to_csv('electors1906.csv', index=False)
