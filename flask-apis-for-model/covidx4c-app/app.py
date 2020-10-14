import numpy as np
import tensorflow as tf
import os
import cv2
from flask import Flask, request, jsonify
import os


mapping = {'normal': 0, 'pneumonia': 1, 'COVID-19': 2}
inv_mapping = {0: 'normal', 1: 'pneumonia', 2: 'COVID-19'}

sess = tf.Session()
tf.get_default_graph()
saver = tf.train.import_meta_graph(os.path.join('models/COVIDNet-CXR4-C', 'model.meta' ))
saver.restore(sess, os.path.join('models/COVIDNet-CXR4-C', 'model-3090'))
global graph
graph = tf.get_default_graph()

image_tensor = graph.get_tensor_by_name("input_1:0")
pred_tensor = graph.get_tensor_by_name('norm_dense_1/Softmax:0')


# initialize our Flask application and the Keras model
app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():

    js = {'file-name':'No image'}

    if request.method == 'POST': 
        
        if request.files.get("image"):
            
            image = request.files["image"].read()
            
            x = cv2.imdecode(np.fromstring(image, np.uint8), 1)
            x = cv2.resize(x, (480, 480))
            x = x.astype('float32') / 255.0
            pred = sess.run(pred_tensor, feed_dict={image_tensor: np.expand_dims(x, axis=0)})

            #print(pred)

            js = {
                'filename': 'X-ray image',
                'probability': {
                    'normal': pred[0][0].item(),
                    'pneumonia': pred[0][1].item(),
                    'covid19': pred[0][2].item(),
                },
                'prediction':  '{}'.format(inv_mapping[pred.argmax(axis=1)[0]])

                }

            return jsonify(js)

            
            
    return jsonify(js)

    

    


# Model is very big so it's processing 1 request at a time
if __name__ == '__main__':
    app.run(host='0.0.0.0')


'''
            if(pred.argmax(axis=1)[0] == 2):
                print("Yes")
            else:
                print("No")
'''