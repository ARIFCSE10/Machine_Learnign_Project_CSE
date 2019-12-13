#################################
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:43:19 2019

@author: Mohammed Badsha Alamgir
"""

import numpy as np


def mapAge(x, l, h):
    return (x - l) / h


def rMapAge(p, l, h):
    return (p * h) + l


training_data_int = np.random.randint(low=13, high=80, size=10000, dtype='int32')
labels_arr = []
for x in training_data_int:
    if x > 45:
        labels_arr.append(True)
    else:
        labels_arr.append(False)

#
training_data = np.array([mapAge(x, 13, 80) for x in training_data_int], dtype='float64')
labels = np.array(labels_arr, dtype='bool')

#
testing_data_int = np.random.randint(low=13, high=80, size=10, dtype='int32')
test_labels_arr = []
for x in testing_data_int:
    if (x > 45):
        test_labels_arr.append(True)
    else:
        test_labels_arr.append(False)

#
testing_data = np.array([mapAge(x, 13, 80) for x in testing_data_int], dtype='float64')
test_labels = np.array(test_labels_arr, dtype='bool')
#
#
#
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam

#
model = Sequential([
    Dense(16, input_shape=(1,), activation='relu'),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.summary()
#
model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

#
model.fit(training_data, labels, batch_size=10, epochs=5, verbose=0)

#
loss = model.evaluate(testing_data, test_labels)

predict = model.predict(testing_data, batch_size=10, verbose=1)
