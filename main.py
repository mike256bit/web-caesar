from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 80%;
                    font: 16px sans-serif;
                    border-radius: 10px;
                    text-align: center;
                }

                textarea {
                    margin-top: 10px;
                    margin-bottom: 20px;
                    width: 80%;
                    height: 120px;
                }

                .inputs {
                    background-color: lightgray;
                    font-weight: bold;
                    width: 400px; 
                    padding: 10px;
                    margin: 10px;
                    border-radius: 10px;
                    display: inline-block;
                }

                .rotation {
                    width: 20%;
                    margin-left: 10px;
                    padding-left: 10px; 
                }

                button {
                    width: 100px;
                    margin: 10px auto;
                    border: 1px solid #864100;
                    background-color: white;
                    padding: 10px;
                    border-radius: 10px;
                    transition-duration: 0.2s
                    display: inline-block;
                    letter-spacing: 1px;
                }

                button:hover {
                    background-color: #864100;
                    color: white;
                    font-weight: bold;
                }

                h1 {
                    text-align: center;
                    font: 20px sans-serif;
                    color: #864100;
                }

                h2 {
                    text-align: center;
                    font: 14px sans-serif;
                    font-style: italic;
                    margin: -10px 0 10px 0; 
                }

            </style>
        </head>
        <body>
            <h1>Web-Caesar Encryption</h1>
            <h2>Michael Toth - LC101 Unit 2</h2>
            <form action="/" method="POST">
                <div class="inputs">

                    Encryption rotation (number): 
                    <input class="rotation" type="number"  name="rot" value="0">
                
                </div>

                <textarea name="text">Sample text.</textarea>

                <div style="text-align: center;">
                    <button type="submit">ENCRYPT</button> <button type="reset">RESET</button>
                </div>

            </form>

        </body>
    </html>
    """
encrypted = """
    <html>
        <head>
            <style>
                div {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 80%;
                    font: 16px sans-serif;
                    border-radius: 10px;
                    text-align: center;
                }

                h1 {
                    text-align: center;
                    font: 20px sans-serif;
                    color: #864100;
                    margin-top: 13px;
                }

                h2 {
                    text-align: center;
                    font: 14px sans-serif;
                    font-style: italic;
                    margin: -10px 0 10px 0; 
                }

            </style>
        </head>
        <body>
            <h1>Web-Caesar Encryption</h1>
            <h2>Michael Toth - LC101 Unit 2</h2>
            <div>


    """

encrypted_footer = """
            </div>
        </body>
    </html>
    """

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])

    return_text = encrypted+"<p>"+str(rotate_string(text, rot))+"</p>"+encrypted_footer

    return return_text


app.run()