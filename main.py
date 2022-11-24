import os
import cv2
from flask import Flask, render_template, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename
from PIL import Image
import numpy as np

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
	image = request.files['file']
	degree = int(request.form['angle'])
	filename = secure_filename(str(image))
	image.save(os.path.join('static/', filename))
	image_file = Image.open(image)
	rotated_image = image_file.rotate(degree)
	rotated_image.save(os.path.join('static/', 'rotated_image.jpg'))
	name = 'rotated_image.jpg'
	return render_template('upload.html', filename=name)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
