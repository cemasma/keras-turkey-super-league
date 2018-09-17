from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import keras
from keras.layers import Input, Dense
from keras.optimizers import SGD

from data import *

data = ft_to_numbers(teams_to_numbers(getdatalist()))
data = get_data_as_matrix(data)
data = transform_data(data)

input = data[:,0:1]
output = data[:,2]

model = Sequential()
model.add(Dense(64, input_dim=1))
model.add(Activation("relu"))
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dense(32))
model.add(Activation("softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(input, output, epochs=5, batch_size=32,validation_split=0.13)