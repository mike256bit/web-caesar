from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                body {{
                    font-family: 'Trebuchet MS', sans-serif;
                    text-align: center;
                }}

                h1 {{
                    font-size: 22px;
                    font-weight: lighter;
                    color: #864100;
                }}

                h3 {{
                    font-size: 16px;
                    color: #864100;
                    margin: -5px 0 5px;
                    text-transform: uppercase;  
                }}

                h2 {{
                    font-size: 14px;
                    margin: -12px 0 10px; 
                    font-style: italic;
                    font-weight: lighter;
                }}

                .box {{
                    background-color: #eee;
                    font-size: 14px;
                    padding: 20px;
                    margin: 10px auto;
                    width: 80%;
                    min-width: 260px;
                    border-radius: 10px;
                    text-align: center;
                }}

                .box:empty{{
                    display: none;
                }}

                .inputs {{
                    background-color: lightgray;
                    font-size: 18px;
                    width: 70%;
                    max-width: 400px; 
                    padding: 10px;
                    margin: 10px auto;
                    border-radius: 10px;
                }}

                .rotation {{
                    width: 20%;
                    margin-left: 10px;
                    padding-left: 10px;
                    color: gray;
                    display: inline-block;
                }}

                textarea {{
                    margin-top: 10px;
                    margin-bottom: 20px;
                    width: 80%;
                    height: 120px;
                }}

                button {{
                    width: 100px;
                    margin: 10px;
                    border: 1px solid #864100;
                    background-color: white;
                    padding: 10px;
                    border-radius: 10px;
                    font-size: 12px;
                    letter-spacing: 1.5px;
                    transition-duration: 0.2s
                    display: inline-block;
                }}

                button:hover {{
                    background-color: #864100;
                    color: white;
                    font-weight: bold;
                }}

            </style>
        </head>
        <body>
            <h1>Web-Caesar Encryption</h1>
            <h2>Michael Toth - LC101 Unit 2</h2>

            <form class="box" action="/" method="POST">
                <div class="inputs">

                    Encryption rotation (number): 
                    <input class="rotation" type="number"  name="rot" value="0">
                
                </div>

                <textarea name="text">{0}</textarea><br>

                <button type="submit">ENCRYPT</button>
                <button type="reset">RESET</button>
                
            </form>

            <div class="box">{1}</div>

        </body>
    </html>
    """

@app.route("/")
def index():
    return form.format("Sample Text.", "", "")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])

    return form.format("Sample Text.", "<h3>Encrypted Text ("+str(rot)+")</h3>"+str(rotate_string(text, rot)), rot)

app.run()