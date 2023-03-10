from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow import keras
app = Flask(__name__)
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
model = keras.models.load_model("model.h5")#,compile=False)
#model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
@app.route('/classify', methods=['POST'])
def predict():
    parameters = request.get_json(force=True)
    im = np.array(parameters['image'])
    out = id2class[np.argmax(model.predict(im))]
    return out
if __name__ == '__main__':
    app.run(host='0.0.0.0')
