#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:43:19 2019

@author: Mohammed Badsha Alamgir
"""

import numpy as np


def getBMI(height, weight):
    return weight / ((height / 100) * (height / 100))


class Person:

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.BMI = getBMI(height, weight)

    def printPerson(self):
        print("Name: " + self.name + " Age: " + repr(self.age) + " Height: " + repr(self.height) + " Weight: " + repr(
            self.weight) + " BMI:" + repr(self.BMI))


def generatePersonArray(N, p_array):
    random_age_array = np.random.randint(low=1, high=120, size=N, dtype='int32')
    random_weight_array = np.random.randint(low=1, high=120, size=N, dtype='int32')

    # for x in range(0,N)
    for age in random_age_array:

        heighest_weight = 1.0
        lowest_weight = 1.0

        lowest_height = 150.0  # cm
        heighest_height = 190.0

        if (age < 5):
            heighest_weight = 10.0
            lowest_weight = 5.0
            lowest_height = 80.0
            heighest_height = 110.0
        elif (age < 10):
            heighest_weight = 20.0
            lowest_weight = 12.0
            lowest_height = 85.0
            heighest_height = 115.0
        elif (age < 20):
            heighest_weight = 40.0
            lowest_weight = 20.0
            lowest_height = 100.0
            heighest_height = 120.0

        elif (age < 30):
            heighest_weight = 50.0
            lowest_weight = 30.0
            lowest_height = 105.0
            heighest_height = 130.0
        else:  # (age < 30)
            heighest_weight = 60.0
            lowest_weight = 50.0
            lowest_height = 115.0
            heighest_height = 135.0

        random_height = np.random.randint(low=lowest_height, high=heighest_height, size=1, dtype='int32')
        random_weight = np.random.randint(low=lowest_weight, high=heighest_weight, size=1, dtype='int32')

        p1 = Person(name="Razib", age=age, height=random_height[0], weight=random_weight[0])
        p1.printPerson()
        p_array.append(p1)


def generateTrainingArray(p_array_train, t_data, t_label):
    for p in p_array_train:
        t_data.append([p.height / 200.0, p.weight / 150.0])
        # t_data.append(p.height)
        # t_data.append(p.weight)
        if (p.BMI > 40):
            t_label.append(False)
        else:
            t_label.append(True)
        BMI_array.append(p.BMI)


########################
N_train = 10000
N_test = 100
person_array_train = []

BMI_array = []

generatePersonArray(N_train, person_array_train)

training_data = []
training_label = []

generateTrainingArray(person_array_train, training_data, training_label)

testing_data = []
testing_label = []
person_array_test = []
generateTrainingArray(person_array_test, testing_data, testing_label)

print("Person Array Size: " + repr(len(person_array_train)))
print("Training Data Array Size: " + repr(len(training_data)))
print("Training Label Array Size: " + repr(len(training_label)))

from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

model = Sequential([
    Dense(16, input_shape=(2,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(2, activation='softmax')
])

model.summary()
#
td = [(x, y) for x, y in training_data]
td = np.array(td, dtype='float32')
tl = [x for x in training_label]
tl = np.array(tl, dtype='bool')
model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#
model.fit(td, tl, batch_size=10, epochs=20)

#
loss = model.evaluate(td, tl)

predict = model.predict(td, batch_size=10, verbose=1)
