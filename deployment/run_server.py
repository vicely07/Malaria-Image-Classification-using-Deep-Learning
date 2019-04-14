from utils import generate_random_start, generate_from_seed
from flask import Flask, render_template, request
from keras.models import load_model
import tensorflow as tf
from keras import backend as K
from wtforms import Form, TextField, validators, SubmitField, DecimalField, IntegerField, FileField

#
from PIL import Image
from PIL import Image
import numpy as np
import os
import cv2

# Create app
app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class ReusableForm(Form):
    """User entry form for entering specifics for generation"""
    

    file = FileField("Upload your image here")

    # Submit button
    submit = SubmitField("Enter")


def load_keras_model():
    """Load in the pre-trained model"""
    global model
    model = load_model('../models/cells.h5')
    # Required for model to work
    global graph
    graph = tf.get_default_graph()


#
def convert_to_array(img):
    im = cv2.imread(img)
    img_ = Image.fromarray(im, 'RGB')
    image = img_.resize((50, 50))
    return np.array(image)

def get_cell_name(label):
    if label==0:
        return "Infected with Malaria", "Please visit a doctor"
    if label==1:
        return "Uninfected with Malaria", ""

def predict_cell(file):
    model = load_model('../models/cells.h5')
    print("Predicting Type of Cell Image.................................")
    ar=convert_to_array(file)
    ar=ar/255
    label=1
    a=[]
    a.append(ar)
    a=np.array(a)
    score=model.predict(a,verbose=1)
    
    K.clear_session()
    print(score)
    label_index=np.argmax(score)
    print(label_index)
    acc=np.max(score)
    Cell, msg=get_cell_name(label_index)
    print('The predicted Cell is a ' + Cell + " with accuracy = %.2f"%(acc*100) + "%")
    return Cell + "<br>" + "%.2f"%(acc*100) + "%", int(acc*100), msg#"bar bar-"+ str(int(acc*100)) + " cyan" #Cell,"The predicted Cell is a "+Cell+" with accuracy = "+str(acc)


# Home page
@app.route("/", methods=['GET', 'POST'])
def home():
    """Home page of app with form"""
    #predict_cell('../imagedata/data5.jpg')
    #predict_cell('../imagedata/data3.jpg')
    #predict_cell('../imagedata/data4.jpg')
    # Create form
    form = ReusableForm(request.form)

    ## On form entry and all conditions met
    if request.method == 'POST' and form.validate():
        #print("Loading image " + form.image.data+ " .")
        #print("Test" + os.path.join(UPLOAD_FOLDER, form.image.data))
        
        """
        if form.image.data:
            image_data = request.files[form.image.name].read()
            open(os.path.join(UPLOAD_FOLDER, form.image.data), 'w').write(image_data)
        else:
            print("img " + form.image.name + " not found")
        """

        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return render_template('index.html', form=form)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return render_template('index.html', form=form)
        
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)) 

        #path = app.config['UPLOAD_FOLDER']+"/" + file.filename;
        
        str, progress_style, msg = predict_cell(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return render_template('data.html', input = str, progress = progress_style, message = msg)
        """
        # Extract information
        seed = request.form['seed']
        diversity = float(request.form['diversity'])
        words = int(request.form['words'])
        # Generate a random sequence
        if seed == 'random':
            return render_template('random.html', input=generate_random_start(model=model, graph=graph, new_words=words, diversity=diversity))
        # Generate starting from a seed sequence
        else:
            return render_template('seeded.html', input=generate_from_seed(model=model, graph=graph, seed=seed, new_words=words, diversity=diversity))
        """
    # Send template information to index.html
    return render_template('index.html', form=form)


if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
           "please wait until server has fully started"))

    
    # Run app
    app.run(host="0.0.0.0", port=50000)
