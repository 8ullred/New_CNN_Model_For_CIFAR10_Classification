# -*- coding: utf-8 -*-
"""Copy of CNN Model

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18_5PxZVc79GTcu3IdBFW-VdBhgROOtYl
"""

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras import layers, regularizers
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout
from tensorflow.keras.optimizers.schedules import ExponentialDecay, PiecewiseConstantDecay, CosineDecay
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

# import tensorflow.keras.optimizers.schedules.ExponentialDecay
# import tensorflow.keras.optimizers.schedules.PiecewiseConstantDecay
# import tensorflow.keras.optimizers.schedules.CosineDecay

"""Load the CIFAR10 dataset"""

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
# x_train.shape
# y_train.shape
# y_train = np.reshape(y_train, (50000, ))

num_classes = 10
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)

# datagen = ImageDataGenerator(rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, zoom_range=0.2, horizontal_flip=True, vertical_flip=True)
# datagen.fit(x_train)
# num_augmented_samples = 2000
# augmented_data = []
# augmented_labels = []

# while len(augmented_data) < num_augmented_samples:
#  batch_x, batch_y = datagen.flow(x_train, y_train, batch_size = num_augmented_samples - len(augmented_data)).next()
#   augmented_data.extend(batch_x)
#   augmented_labels.extend(batch_y)

# Convert the lists to NumPy arrays
# augmented_data = np.array(augmented_data)
# augmented_labels = np.array(augmented_labels)

# Concatenate the original training data with the augmented data
# x_train_augmented = np.concatenate((x_train, augmented_data), axis=0)
# y_train_augmented = np.concatenate((y_train, augmented_labels), axis=0)

"""Normalizing the pixel values to the range [0, 1]"""

import numpy as np
np.shape(x_train)
np.shape(x_test)

x_train, x_test = x_train/255.0, x_test/225.0

"""Defining and Compiling the CNN Model"""

from tensorflow.keras.layers import Activation

def get_model():


  model = keras.Sequential([
      layers.Conv2D(32, (3, 3), input_shape = (32, 32, 3)),
      BatchNormalization(),
      Activation('relu'),
      layers.MaxPooling2D(2, 2),
      layers.Dropout(0.35),
      layers.Conv2D(64, (3, 3)),
      BatchNormalization(),
      Activation('relu'),
      layers.MaxPooling2D((2, 2)),
      layers.Dropout(0.35),
      layers.Conv2D(256, (3, 3)),
      Activation('relu'),
      layers.Dropout(0.35),
      layers.Flatten(),
      layers.Dense(64, activation='relu'),
      layers.Dropout(0.35),
      BatchNormalization(),
      layers.Dense(10, activation='softmax'),
  ])



  # Define a learning rate schedule
  learning_rate_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
      initial_learning_rate=0.01,
      decay_steps=10000,
      decay_rate=0.96
  )

  # Create an optimizer with the learning rate schedule
  optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate_schedule)

  model.compile(optimizer=optimizer, loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

  return model

"""Train

Increasing Validation Accuracy:



Batch Normalization: After the ReLUs of all convolutional layers.

DropOut:

Batch Size: 128.

Initial Learning Rate: 0.01.

Learning Rate Decay Scale: 0.1 , applied after [200, 250, 300] epochs.

Initialization for convolutional layers: He Initialization.

Weight Decay: L2-Regularization with scale=0.001.
"""

from keras.api._v2.keras import callbacks

from IPython.core import history


with tf.device('/device:GPU:0'):
  model = get_model()

  history = model.fit(x_train, y_train, epochs=200, batch_size=32, validation_data=(x_test, y_test))


model_path = '/content/drive/My Drive/Ronald/models/'
model.save(model_path+'model_categories.h5')

from matplotlib import pyplot as plt
plt.plot(history.history['loss'], 'r', label = 'training loss')
plt.plot(history.history['val_loss'], label = 'validation loss')

plt.title('Model Loss')
plt.ylabel('Loss')

plt.xlabel('Epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], 'r', label = "training accuracy")
plt.plot(history.history['val_accuracy'], label = "validation accuracy")

plt.title("Model Accuracy")
plt.ylabel("Accuracy")
plt.xlabel("Epochs")
plt.legend()
plt.show()

test_loss, test_accuracy = model.evaluate(x_test, y_test)

image_path = '/content/drive/My Drive/Research/Data/Classifier'
model_path = '/content/drive/My Drive/Ronald/models/'

import numpy as np
y_pred = [] #store predicted labels
y_true = [] #store true labels

for image_batch, label_batch in val_ds:
  y_true.append(label_batch)
  preds = saved_model.predict(image_batch)
  y_pred.append(np.argmax(preds, axis = -1))

import tensorflow
true_categories = tensorflow.concat([item for item in y_true], axis = 0)
predicted_categories = tensorflow.concat([item for item in y_pred], axis = 0)

from sklearn.metrics import confusion_matrix

cnf_matrix = confusion_matrix(true_categories, predicted_categories, normalize='pred')

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])