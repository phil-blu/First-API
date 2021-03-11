from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>Hello</h1></body></html>'

@app.route('/table/<int:number>')
def index1(number):
    return render_template('index1.html', num = number)


if __name__ == "__main__":
    app.run(debug=True)