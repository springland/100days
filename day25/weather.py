import csv
import pandas as pd
def  get_temperatures():
    with open('weather_data.csv') as weather_file:
        rows = csv.reader(weather_file)
        return [row[1]  for row in rows ]


temps = [ int(t) for t in get_temperatures()[1:]]
print(temps)

df = pd.read_csv('weather_data.csv')
print(df.loc[: , 'temp'].values)

print(df['temp'].agg(['mean' , 'max']))
print(df[df['temp'] == df['temp'].max()])
print(df[df['day'].isin(['Monday' , 'Tuesday'])])
