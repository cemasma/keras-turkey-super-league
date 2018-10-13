from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
import keras
from keras.layers import Input, Dense
from keras.optimizers import SGD

from data import *
from matches import *

data = ft_to_numbers(teams_to_numbers(getdatalist()))
data = get_data_as_matrix(data)
data = transform_data(data)

input = data[:,0:2]
output = data[:,2]

model = Sequential()
model.add(Dense(256, input_dim=2))
model.add(Activation("relu"))
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Dense(256))
model.add(Activation("softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(input, output, epochs=50, batch_size=32,validation_split=0.13)



# Trabzonspor - Galatasaray 4-0 2018
# If prediction equal to 2 Trabzon wins
# If prediction equal to 1 Tranbzon lose
# If prediction equal to 0 match is draw
# predict = np.array([7,5]).reshape(1,2)
# print(model.predict_classes(predict))