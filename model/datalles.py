import pandas as pd
import pathlib

# Lee el archivo CSV
df = pd.read_csv(pathlib.Path('data/traffic.csv'))

result=df["Traffic Situation"].unique()
print(result)