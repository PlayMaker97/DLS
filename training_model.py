# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:22:35 2020

@author: Souhail Moutaai
"""

# Importer Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Etape1:Utilisation De methode CNN pour l'aprentissage

# Inistialisasion du CNN
classifier = Sequential()

# First convolution layer and pooling
classifier.add(Convolution2D(32, (3, 3), input_shape=(64, 64, 1), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
# Second convolution layer and pooling
classifier.add(Convolution2D(32, (3, 3), activation='relu'))
# input_shape is going to be the pooled feature maps from the previous convolution layer
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening the layers
classifier.add(Flatten())

# Adding a fully connected layer
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=45, activation='softmax')) # softmax for more than 2

# Compilation du  CNN
classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy']) # categorical_crossentropy for more than 2


# Step 2 - Preparing the train/test data and training the model


from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('C:/Users/Souhail Moutaai/Desktop/Chatei/tr',
                                                 target_size=(64, 64),
                                                 batch_size=5,
                                                 color_mode='grayscale',
                                                 class_mode='categorical')

test_set = test_datagen.flow_from_directory('C:/Users/Souhail Moutaai/Desktop/Chatei/test',
                                            target_size=(64, 64),
                                            batch_size=5,
                                            color_mode='grayscale',
                                            class_mode='categorical') 
classifier.fit_generator(
        training_set,
        steps_per_epoch=1000,
        epochs=10,
        validation_data=test_set,
        validation_steps=30) 


# Enregistrement du  model
model_json = classifier.to_json()
with open("C:/Users/Souhail Moutaai/Desktop/PFA/model-bw.json", "w") as json_file:
    json_file.write(model_json)
classifier.save_weights('C:/Users/Souhail Moutaai/Desktop/PFA/model-bw.h5')
