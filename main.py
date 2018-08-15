from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/img1.html')
def img1():
    return render_template('img1.html')

if __name__ == '__main__':
    app.run(debug=True)
