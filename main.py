from flask import Flask, request, render_template
from caesar import rotate_string
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('caesar_form.html', sample_text="Sample Text.")
    
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    primer = "Sample text."
    response = []
    encr_title = ""
    error_class = ""
    

    if text == "":
        error_class = "error"
        response.append("Please enter text to encrypt.") 

    if rot == "":
        error_class = "error"
        response.append("Please enter a number.")
        if not text == "":
            primer = text

    if not text == "" and not rot == "":
        encr_title = "Encrypted Text ("+rot+")"
        rot = int(rot)
        response.append(rotate_string(text, rot))
        
    return render_template('caesar_response.html', sample_text = primer, text_return = response, encrypted = encr_title, error_class = error_class)
    
app.run()
