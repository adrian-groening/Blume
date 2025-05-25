
import os
import datetime

import IPython
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

may20 = pd.read_csv('2025-05-20_aggs.csv')
may21 = pd.read_csv('2025-05-21_aggs.csv')
may22 = pd.read_csv('2025-05-22_aggs.csv')

# importing the dataset
df = pd.concat([may20, may21, may22], ignore_index=True)

# Convert 'Timestamp' to datetime and ensure correct data types
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# addtional features to find extra patterns in the data
#df['hour'] = df['Timestamp'].dt.hour
#df['minute'] = df['Timestamp'].dt.minute
#df['dayofweek'] = df['Timestamp'].dt.dayofweek

#for lag in range(1, 6):  # past 5 minutes
#    df[f'Close_lag_{lag}'] = df['Close'].shift(lag)
#    df[f'Volume_lag_{lag}'] = df['Volume'].shift(lag)
#    df[f'VWAP_lag_{lag}'] = df['VWAP'].shift(lag)

# split the data into training and testing sets
#df_train  = df[df['Timestamp'] < '2025-05-22 12:00:00']
#df_test = df[df['Timestamp'] >= '2025-05-22 12:00:00']

#print(df_train.shape, df_test.shape)

# drop the 'Timestamp' column
datetime = df.pop('Timestamp')
#date_time = pd.to_datetime(df_train.pop('Timestamp'), format='%d.%m.%Y %H:%M:%S')

#print(datetime)
#print(df_train.head())
#print(df_train.describe().transpose())



X_train = None
y_train = None

X_test = None
y_test = None




#print to text file
#with open('df_train.txt', 'w') as f:
#    f.write(df.to_string())


timestamp_s = datetime.map(pd.Timestamp.timestamp)
day = 24*60*60
year = (365.2425)*day

df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
df['Year sin'] = np.sin(timestamp_s * (2 * np.pi / year))
df['Year cos'] = np.cos(timestamp_s * (2 * np.pi / year))
#plt.plot(np.array(df['Day sin'])[:])
#plt.plot(np.array(df['Day cos'])[:])
#plt.xlabel('Time [m]')
#plt.title('Time of day signal')

#plt.show()

column_indices = {name: i for i, name in enumerate(df.columns)}

n = len(df)
train_df = df[0:int(n*0.7)]
val_df = df[int(n*0.7):int(n*0.9)]
test_df = df[int(n*0.9):]

num_features = df.shape[1]

print('Data shapes: ', train_df.shape, val_df.shape, test_df.shape)

train_mean = train_df.mean()
train_std = train_df.std()

train_df = (train_df - train_mean) / train_std
val_df = (val_df - train_mean) / train_std
test_df = (test_df - train_mean) / train_std

df_std = (df - train_mean) / train_std
df_std = df_std.melt(var_name='Column', value_name='Normalized')
plt.figure(figsize=(12, 6))
ax = sns.violinplot(x='Column', y='Normalized', data=df_std)
_ = ax.set_xticklabels(df.keys(), rotation=90)
plt.show()

