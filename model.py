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

input = data[:, 0:2]
output = data[:, 2]

model = Sequential()
model.add(Dense(256, input_dim=2))
model.add(Dense(256))
model.add(Activation("relu"))
model.add(Activation("relu"))
model.add(Dense(256))
model.add(Activation("softmax"))

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.fit(input, output, epochs=100, batch_size=32, validation_split=0.2)

def make_predictions(matches):
    for match in matches:
        predict = np.array([match["Team 1"], match["Team 2"]]).reshape(1, 2)
        print(list(team_codes.keys())[list(team_codes.values()).index(match["Team 1"])] + " - " +
            list(team_codes.keys())[list(team_codes.values()).index(match["Team 2"])]
            + "\nResult: " + str(match["Result"])
            + "\nPredict: " + str(model.predict_classes(predict)[0]) + "\n\n")
    print("\n\n")

make_predictions(first_week_matches())
make_predictions(second_week_matches())
make_predictions(third_week_matches())
make_predictions(fourth_week_matches())
make_predictions(fifth_week_matches())
make_predictions(seventh_week_matches())
make_predictions(eighth_week_matches())
make_predictions(nineth_week_matches())
make_predictions(tenth_week_matches())
make_predictions(eleventh_week_matches())
make_predictions(twelveth_week_matches())
make_predictions(thirteenth_week_matches())



# Trabzonspor - Galatasaray 4-0 2018
# If prediction equal to 2 Trabzon wins
# If prediction equal to 1 Tranbzon lose
# If prediction equal to 0 match is draw
# predict = np.array([7,5]).reshape(1,2)
# print(model.predict_classes(predict))
