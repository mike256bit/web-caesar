from flask import Flask, request
from caesar import rotate_string
import os
import cgi
import jinja2

#sets template path based on main.py path
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

#creates jinja environment for templates (load templates from here)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('caesar_form.html')
    return template.render(sample_text="Sample Text.", encrypted = "")
    
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    error = ""
    response = ""
    primer = "Sample text."

    if text == "":
        error = "<p class='error'>Please enter text to encrypt.</p>"
        response += error

    if rot == "":
        error = "<p class='error'>Please enter a number.</p>"
        response += error
        if not text == "":
            primer = text

    if not text == "" and not rot == "":
        rot = int(rot)
        text = cgi.escape(text)
        response = "<h3>Encrypted Text ("+str(rot)+")</h3>"+rotate_string(text, rot)
    
    template = jinja_env.get_template('caesar_form.html')
    return template.render(sample_text = primer, text_return = response)
    
app.run()