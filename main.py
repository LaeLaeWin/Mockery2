from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/img1.html')
def img1():
    return render_template('img1.html')

@app.route('/img2.html')
def img1():
    return render_template('img2.html')

@app.route('/img3.html')
def img1():
    return render_template('img3.html')

@app.route('/img4.html')
def img1():
    return render_template('img4.html')

@app.route('/img5.html')
def img1():
    return render_template('img5.html')

@app.route('/img6.html')
def img1():
    return render_template('img6.html')

@app.route('/img7.html')
def img1():
    return render_template('img7.html')

@app.route('/img8.html')
def img1():
    return render_template('img8.html')

@app.route('/b.html')
def img1():
    return render_template('b.html')

@app.route('/delivery.html')
def img1():
    return render_template('delivery.html')

@app.route('/s2.html')
def img1():
    return render_template('s2.html')

@app.route('/sale.html')
def img1():
    return render_template('sale.html')

if __name__ == '__main__':
    app.run(debug=True)
