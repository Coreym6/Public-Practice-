# this will be for some A.I. image recognition training
import pandas as pd
import numpy as np

# Load the data from CSV files
train_data = pd.read_csv('mental_health_finaldata_1.csv') # I'm assuming that this would be the kaggle csv dataset
#Need to probably have the csv data into this repo. 
test_data = pd.read_csv('output.csv') # maybe this is the output from the results of the kaggle dataset

# Split the data into features and labels
x_train = train_data.drop('label', axis=1).values
y_train = train_data['label'].values
x_test = test_data.values

# Preprocess the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Build the neural network model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(784,)))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model
predictions = model.predict(x_test)