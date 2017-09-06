"""
usage:
$ python check_timeout.py <logfile>
$ python check_timeout.py log170829.txt
"""
import pandas as pd
import sys

names = ['date', 'time', 'raspi', 'latency', 'unit']
df = pd.read_csv(sys.argv[1], sep=' ', names=names, header=0)

time_list=[]
for i in range(len(df)):
    if df['date'][i] == 'timeout!!!!!':
        time_list.append(df['time'][i-1])

df = df.dropna()

raspi_list = list(df['raspi'].unique())
num_bc = len(list(df['time'].unique()))
print('num. of bc = ', num_bc)

print('num. of timeout:')
for name in raspi_list:
    raspi_time_list = list(df[df['raspi'].isin([name])]['time'])
    timeout_list = list(set(time_list)-set(raspi_time_list))
    print(name, len(timeout_list))

print()
print('RPI at timeout:')
for time in time_list:
    time_raspi_list = df[df['time'].isin([time])]['raspi']
    raspiout_list = list(set(raspi_list) - set(time_raspi_list))
    if raspiout_list != []:
        print(time, raspiout_list)
