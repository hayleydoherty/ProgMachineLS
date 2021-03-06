import pandas as pd
import numpy as np
import tensorflow.keras as kr
#from power import value_1


# reading in the data with pandas
df = pd.read_csv("powerproduction.csv")
# deleting empty rows and rows that were thought to be outliers
df = df.dropna(how = 'all')
drop_rows = df[(df['power'] == 0) & (df['speed'] >= 5.0)].index
df.drop(drop_rows, inplace = True)

#saving x and y variables
x = df['speed']
y = df['power']


model = kr.models.Sequential()
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

mod = model.fit(x, y, epochs=500, batch_size=10)

def prediction(x):
    return model.predict(x)
    
#print(prediction([15.0]))
