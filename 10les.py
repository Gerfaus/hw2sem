# Нейронные сети:
# - сверточные (конволюционные) нейронные сети - компьютерное зрение, классификация изображений
# - реккурентные нейронные сети - распознование текста, обработка естесвенногшо языка
# - генеративные состязательные сети - создание художественных, музыкальных произведений
#  многослойные перцептрон - простейший тип

import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] == '0'

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image

from tensorflow.keras.applications.resnet50 import preprocessing_input
from tensorflow.keras.applications.resnet50 import ResNet50

img_path = './data/cat.png'
img = image.load_img(img_path, target_size = (224, 224))

TRAIN_DATA_DIR = './data/train_data/'
VALIDATION_DATA_DIR = '/data/val_data/'
TRAIN_SAMPLES = 500
VALIDATION_SAMPLES = 500
NUM_CLASSES = 2
IMG_WIDTH, IMG_HIGHT = 224, 224
BATCH_SIZE = 64

train_datagen = image.ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20
)

val_datagen = image.ImageDataGenerator(preprocessing_function=preprocessing_input)
train_generator = train_datagen.flow_from_directory(
    TRAIN_DATA_DIR,
    target_size=(IMG_WIDTH, IMG_HIGHT)
    batch_size=BATCH_SIZE
)

val_generator = val_datagen.flow_from_directory(
    VALIDATION_DATA_DIR,
    target_size=(IMG_WIDTH, IMG_HIGHT)
    batch_size=BATCH_SIZE
)


def model_maker():
    base_model = MobileNet(include_top=False, input_share=(IMG_WIDTH, IMG_HIGHT, 3))
    for layer in base_model.layers[:]:
        layer.trainable = False


from tensorflow.keras.optimizers import Adam

model = model_maker()
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['acc'])

import math

num_steps = math.ceil(float(TRAIN_SAMPLES) / BATCH_SIZE)

model.fit(
    train_generator,
    steps_per_epoch=num_steps, 
    epochs=10,
    validation_data=val_generator,
    validation_steps=num_steps
)

import numpy as np

img_array = image.img_to_array(img)

img_batch = np.expand_dims(img_array, axis=0)

img_processed = preprocess_input(img_batch)

model = ResNet50()
prediction = model.predict(img_processed)








# plt.imshow(img)
# plt.show()