from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')


if __name__ == "__main__":
    app.run(debug=True)