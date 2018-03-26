from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form ="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method='POST'>
            <label for="rot">Rotate by:</label>
                <input name="rot" type="text" />
            <textarea name="text">{x}</textarea>
                <input type="submit"/>
        </form>  
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format(x='')

def is_integer(num):
   try:
       int(num)
       return True
   except ValueError:
       return False    

@app.route("/", methods=['POST'])
def encrypt():
    
    text = request.form['text']
    rot = request.form['rot']

    if not is_integer(rot):
        return form.format(x='')

    else:
        rot = int(rot)
        cipher = rotate_string(text, rot)
        return form.format(x=cipher)




app.run()