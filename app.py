import os

from flask import Flask, render_template

template_dir = os.path.abspath('./templates/templates')
app = Flask(__name__, template_folder=template_dir)


# r'C:\Users\kianp\Desktop\python scripts\JAL web application\bootstrap-4.5.3-examples\dashboard\index.html'
@app.route('/')
@app.route('/libary')
def index():
    return render_template('index.html')


@app.route('/libary')
def libary():
    return render_template('libary.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/spotify')
def spotify():
    return render_template('spotify.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
