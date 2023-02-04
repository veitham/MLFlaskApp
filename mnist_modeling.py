import numpy as np
from tensorflow import keras
from keras import layers
import pandas as pd

# Classes
id2class = {0: "T-shirt/top",
            1: "Trouser",
            2: "Pullover",
            3: "Dress",
            4: "Coat",
            5: "Sandal",
            6: "Shirt",
            7: "Sneaker",
            8: "Bag",
            9: "Ankle boot",}

# Load data
df1 = pd.read_csv("data/fashion-mnist-train-1.csv")
df2 = pd.read_csv("data/fashion-mnist-train-2.csv")
df_test = pd.read_csv("data/fashion-mnist_test.csv")
df_train = pd.concat([df1, df2],ignore_index=True)
df_train

# Train test split
x_train = df_train.drop(['label'], axis=1).values
y_train = df_train['label'].values
x_test = df_test.drop(['label'], axis=1).values
y_test = df_test['label'].values

x_train = np.reshape(x_train, (44998,28, 28))
x_test = np.reshape(x_test, (10000,28, 28))

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Normalize
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# verify shape
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        #layers.Conv2D(16, kernel_size=(1, 1), activation="relu"),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(x_train, y_train, batch_size=128, epochs=5, validation_split=0.1)

# Evaluate
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

model.save('model.h5')