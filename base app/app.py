from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<center style='color: blue;'>Hello, World!</center>"

#2 Dynamic route
@app.route('/greet/<Uname>')
def greet(Uname):
    return f"<center> Hello,<b style='color: blue;'>Hello, {Uname}!</b></center>"

#3 


if __name__ == '__main__':
    app.run(debug=True, port=4500)
